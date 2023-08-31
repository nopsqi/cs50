#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    // ensure proper usage
    // TODO #1
    if (argc < 2 || argc > 2)
    {
        printf("%s\n", "Usage: ./wordle wordsize");
    }

    // ensure argv[1] is either 5, 6, 7, or 8 and store that value in wordsize instead
    // TODO #2
    
    if (!argv[1])
    {
        printf("%s\n", "Usage: ./wordle wordsize\n");
        return 1;
    }
    else if (argv[1] < 4 || argv[1] > 8)
    {
        printf("%s\n", "Error: wordsize  must be either 5, 6, 7, or 8\n");
        return 1;
    }
    wordsize = argv[1];
}