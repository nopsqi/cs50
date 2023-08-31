#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);
int get_index(char array[]);
int get_size(char array[]);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    printf("%i\n", array_size);
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    char capital[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char lower[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    int array_size = get_size(word);
    for (int i = 0; i < array_size; i++)
    {
        int index = get_index(word[i], word)
    }
    return 0;
}

int get_index(char c, char array[])
{
    int array_size = get_size(array)
    int index = -1;
    for (int i = 0; i < array_size; i++)
    {
        if (c == array[i])
        {
            index = i;
            break;
        }
    }
    return index;

}

int get_size(char array[])
{
    int array_size = sizeof(array) / sizeof(array[0]);
    return array_size;
}