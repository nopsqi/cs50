#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    fread(&bf, sizeof(WAVHEADER), 1, input);

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
    fwrite(&bf, sizeof(WAVHEADER), 1, output);

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(bf);

    // Write reversed audio to file
    // TODO #8
    uint8_t *data = malloc(block_size * sizeof(uint8_t));
    fseek(input, block_size, SEEK_END);
    while (ftell(input) > sizeof(WAVHEADER) + block_size)
    {
        fseek(input, -(2 * block_size), SEEK_CUR);
        fread(data, 1, block_size, input);
        fwrite(data, 1, block_size, output);
    }

    fclose(input);
    fclose(output);
    free(data);
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