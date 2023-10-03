#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc < 3)
    {
        printf("Usage: ./reverse input output\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        return 1;
    }


    // Read header
    // TODO #3
    WAVHEADER bf;
    fread(&bf, 1, sizeof(WAVHEADER), input);

    // Use check_format to ensure WAV format
    // TODO #4
    if (!check_format(bf))
    {
        printf("File is not WAV.\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&bf, 1, sizeof(WAVHEADER), output);

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(bf);

    // Write reversed audio to file
    // TODO #8
    int *data = malloc(block_size)
    while()

    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    char *wave = "WAVE";
    for (int i = 0; i < 4; i++)
    {
        if (header.format[i] != wave[i])
            return 0;
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return round(header.numChannels * (header.bitsPerSample / (float) 8));
}