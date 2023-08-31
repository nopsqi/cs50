#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <ctype.h>


int main(int argc, string argv[])
{
    if (!argv[1])
    {
        printf("%s\n", "null");
        return 1;
    }
    printf("%i\n", isdigit(argv[1]));
}