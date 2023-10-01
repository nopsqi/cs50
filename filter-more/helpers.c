#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "helpers.h"

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
        RGBTRIPLE (*row)[width] = malloc(width * sizeof(RGBTRIPLE));
        if (i < 5)
            printf("%p %p\n", image, row);

        for (int j = 0; j < width; j++)
        {
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
