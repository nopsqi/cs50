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
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        return 1;
    }
    uint8_t *buffer = malloc(BLOCK_SIZE * sizeof(uint8_t));
    int total = 0;

    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        for (int i = 0; i < BLOCK_SIZE; i++)
        {
            printf("%x ", buffer[i]);
            if (i % 4 == 0)
                printf("\n");
            total++;
        }
        // printf("%li\n", sizeof(buffer[0]));
    }
    printf("total = %i\n", total);

    fclose(file);
    free(buffer);
}

bool isJpeg()
{
    return 0;
}