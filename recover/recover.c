#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }
    FILE *raw = fopen(argv[1], "r");
    if (raw == NULL)
    {
        return 1;
    }
    uint8_t *buffer = malloc(BLOCK_SIZE * sizeof(uint8_t));
    int outname = 0;

    while (fread(buffer, 1, BLOCK_SIZE, raw) == BLOCK_SIZE)
    {
        if ((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff) && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            char 
            FILE *outfile = fopen()
            outname++;
        }
    }
    printf("total = %i\n", outname);

    fclose(raw);
    free(buffer);
}