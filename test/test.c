#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

string get_guess(int wordsize);

int main(int argc, string argv[])
{
    // ensure proper usage
    // TODO #1
    if (argc < 2 || argc > 2)
    {
        printf("%s\n", "Usage: ./wordle wordsize");
        return 1;
    }

    int wordsize = 0;
    // ensure argv[1] is either 5, 6, 7, or 8 and store that value in wordsize instead
    // TODO #2
    wordsize = strtol(argv[1], NULL, 10);
    if (wordsize < 4 || wordsize > 8)
    {
        printf("%s\n", "Error: wordsize  must be either 5, 6, 7, or 8");
        return 1;
    }
    string guess = get_guess(wordsize);
}

string get_guess(int wordsize)
{
    string guess = "";

    // ensure users actually provide a guess that is the correct length
    // TODO #3
    int length = strlen(guess);
    printf("%i\n", length);
    while (length < wordsize || length > wordsize)
    {
        guess = get_string("Input a %i-letter word: ", wordsize);
        length = 
    }
    return guess;
}