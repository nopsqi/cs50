#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2)
    {
        printf("%s\n", "Usage: ./caesar key");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        printf("%c ", argv[1][i]);
        printf("%i\n", isdigit(argv[1][i]));
    }
    printf("\n");
    // int key = strtol(argv[1], NULL, 10);
    // printf("%i\n", key);
}