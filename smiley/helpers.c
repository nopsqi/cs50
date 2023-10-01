#include <stdio.h>
#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
        }
    }
    printf("%i\n", image[0][0].rgbtRed);
    printf("%i\n", image[0][2].rgbtRed);
}
