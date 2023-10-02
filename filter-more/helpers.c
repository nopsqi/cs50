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

void get_kernel(int height, int width, int i, int j, KERNEL *kernel)
{
    int kernel_half = ((*kernel).init_hw - 1) / 2;
    if (((*kernel).x_start = j - kernel_half) < 0)
        (*kernel).x_start = 0;
    if (((*kernel).x_end = j + kernel_half + 1) > width)
        (*kernel).x_end = width;
    if (((*kernel).y_start = i - kernel_half) < 0)
        (*kernel).y_start = 0;
    if (((*kernel).y_end = i + kernel_half + 1) > height)
        (*kernel).y_end = height;
    (*kernel).size = ((*kernel).x_end - (*kernel).x_start) * ((*kernel).y_end - (*kernel).y_start);
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
            get_kernel(height, width, i, j, &kernel);

            int r = 0, g = 0, b = 0;
            for (int k = kernel.y_start; k < kernel.y_end; k++)
            {
                for (int l = kernel.x_start; l < kernel.x_end; l++)
                {
                    r += tmp[k][l].rgbtRed;
                    g += tmp[k][l].rgbtGreen;
                    b += tmp[k][l].rgbtBlue;
                }
            }
            image[i][j].rgbtRed = round(r / (float) kernel.size);
            image[i][j].rgbtGreen = round(g / (float) kernel.size);
            image[i][j].rgbtBlue = round(b / (float) kernel.size);
        }
    }
    free(tmp);
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    typedef struct
    {
        int r;
        int g;
        int b;
    } pixel;

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

    int8_t (*Mx)[kernel.init_hw] = calloc(kernel.init_hw, kernel.init_hw * sizeof(int8_t));
    Mx[0][0] = -1;
    Mx[0][1] = 0;
    Mx[0][2] = 1;
    Mx[1][0] = -2;
    Mx[1][1] = 0;
    Mx[1][2] = 2;
    Mx[2][0] = -1;
    Mx[2][1] = 0;
    Mx[2][2] = -1;

    int8_t (*My)[kernel.init_hw] = calloc(kernel.init_hw, kernel.init_hw * sizeof(int8_t));
    My[0][0] = -1;
    My[0][1] = -2;
    My[0][2] = -1;
    My[1][0] = 0;
    My[1][1] = 0;
    My[1][2] = 0;
    My[2][0] = 1;
    My[2][1] = 2;
    My[2][2] = 1;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            get_kernel(height, width, i, j, &kernel);
            pixel p = {0, 0, 0};
            int gx = 0, gy = 0, euclid = 0;

            for (int k = kernel.y_start; k < kernel.y_end; k++)
            {
                for (int l = kernel.x_start; l < kernel.x_end; l++)
                {
                    p.r = image
                }
            }

        }
    }

    free(tmp);
    return;
}
