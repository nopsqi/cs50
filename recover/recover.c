#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SZE 512;

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }
    char *filename = argv[1];
    uint8_t 

    while (fread(buffer, 1, BLOCK_SIZE, filename) == BLOCK_SIZE)
    {

    }
}