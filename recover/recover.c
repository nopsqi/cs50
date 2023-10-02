#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512;

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    uint8_t buffer;

    while (fread(&buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {

    }
}

bool isJpeg()
{

}