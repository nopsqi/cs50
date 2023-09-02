#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2)
    {
        printf("%s\n", "Usage: ./caesar key");
        return 1;
    }
    printf("%i\n", isdigit(argv[1]));

}