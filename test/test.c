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
}