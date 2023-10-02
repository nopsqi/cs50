#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "helpers.h"
typedef struct
{
   int init_size;
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
    kernel.size = 3;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int kernel_half = (kernel.size - 1) / 2;
            if ((kernel.x_start = j - kernel_half) < 0)
                kernel.x_start = 0;
            if (i == 0 && j == 5)
                printf("%i\n", kernel.x_start);
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
