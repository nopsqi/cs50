#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "helpers.h"
typedef struct
{
   int init_hw;
   int size;
   int x_start;
   int x_end;
   int y_start;
   int y_end;
} KERNEL;

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int value = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / (float) 3);
            image[i][j].rgbtRed = value;
            image[i][j].rgbtGreen = value;
            image[i][j].rgbtBlue = value;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        RGBTRIPLE *row = malloc(width * sizeof(RGBTRIPLE));
        for (int j = 0, k = width - 1; j < width; j++, k--)
            row[k] = image[i][j];

        for (int j = 0; j < width; j++)
        {
            image[i][j] = row[j];
        }
        free(row);
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE (*tmp)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j] = image[i][j];
        }
    }

    KERNEL kernel;
    kernel.init_hw = 3;
    RGBTRIPLE zeroed = {0, 0, 0};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int kernel_half = (kernel.init_hw - 1) / 2;
            if ((kernel.x_start = j - kernel_half) < 0)
                kernel.x_start = 0;
            if ((kernel.x_end = j + kernel_half + 1) > width)
                kernel.x_end = width;
            if ((kernel.y_start = i - kernel_half) < 0)
                kernel.y_start = 0;
            if ((kernel.y_end = i + kernel_half + 1) > height)
                kernel.y_end = height;
            kernel.size = (kernel.x_end - kernel.x_start) * (kernel.y_end - kernel.y_start);

            image[i][j] = zeroed;
            if (i == 0 && j == 0)
                printf("i(%i, %i, %i)\n\n", image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue);
            for (int k = kernel.y_start; k < kernel.y_end; k++)
            {
                for (int l = kernel.x_start; l < kernel.x_end; l++)
                {
                    image[i][j].rgbtRed += tmp[k][l].rgbtRed;
                    image[i][j].rgbtGreen += tmp[k][l].rgbtGreen;
                    image[i][j].rgbtBlue += tmp[k][l].rgbtBlue;
                    if (i == 0 && j == 0)
                    {
                        // printf("t(%i, %i, %i)\t", tmp[k][l].rgbtRed, tmp[k][l].rgbtGreen, tmp[k][l].rgbtBlue);
                        // printf("t(%p, %p, %p)\t", &tmp[k][l].rgbtRed, &tmp[k][l].rgbtGreen, &tmp[k][l].rgbtBlue);
                        printf("i(%i, %i, %i)\t", image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue);
                        // printf("i(%p, %p, %p)\t", &image[i][j].rgbtRed, &image[i][j].rgbtGreen, &image[i][j].rgbtBlue);
                    }
                }
                if (i == 0 && j == 0)
                    printf("\n");
            }
            if (i == 0 && j == 0)
                printf("\n");
            if (i == 0 && j == 0)
            {
                // printf("t(%i, %i, %i)\n", tmp[i][j].rgbtRed, tmp[i][j].rgbtGreen, tmp[i][j].rgbtBlue);
                printf("i(%i, %i, %i)\n", image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue);
                // printf("i(%p, %p, %p)\n", &image[i][j].rgbtRed, &image[i][j].rgbtGreen, &image[i][j].rgbtBlue);
            }
            image[i][j].rgbtRed = round(image[i][j].rgbtRed / (float) kernel.size);
            image[i][j].rgbtGreen = round(image[i][j].rgbtGreen / (float) kernel.size);
            image[i][j].rgbtBlue = round(image[i][j].rgbtBlue / (float) kernel.size);
            if (i == 0 && j == 0)
                printf("(%i, %i, %i)\n", image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue);
        }
    }
    free(tmp);
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
