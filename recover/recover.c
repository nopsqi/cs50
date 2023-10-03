#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

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
    FILE *outfile;
    char outname[8];
    uint8_t *buffer = malloc(BLOCK_SIZE * sizeof(uint8_t));
    int image_counter = 0;

    while (fread(buffer, 1, BLOCK_SIZE, raw) == BLOCK_SIZE)
    {
        if ((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff) && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            if (image_counter > 0)
                fclose(outfile);
            sprintf(outname, "%03d.jpg", image_counter);
            outfile = fopen(outname, "w");
            image_counter++;
        }
        if (image_counter > 0)
            fwrite(buffer, BLOCK_SIZE, 1, outfile);
    }

    fclose(raw);
    fclose(outfile);
    free(buffer);
}