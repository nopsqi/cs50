#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int check_position(char c);
bool check_key(string key);

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    if (check_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int key = strtol(argv[1], NULL, 10);
    printf("%i\n", key);
}

bool check_key(string key)
{
    for (int i = 0; i < strlen(key); i++)
    {
        if (!isdigit(key[i]))
        {
            return false;
        }
    }
    return true;
}

int check_position(char c)
{
    char capital[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int position = -1;
    for (int i = 0; i < 26; i++)
    {
        if (toupper(c) == capital[i])
        {
            position = i;
            break;
        }
    }
    return position;
}