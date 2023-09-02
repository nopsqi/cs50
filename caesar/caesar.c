#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2)
    {
        printf("%s\n", "Usage: ./caesar key");
        return 1;
    }
    int key = strtol(argv[1], NULL, 10);
    printf("%i\n", key);
}