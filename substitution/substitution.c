#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

const int KEY_LENGTH = 26;
bool check_key(string key);

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2)
    {
        printf("%s\n", "Usage: ./subtition key");
        return 1;
    }
    bool is_key_valid = check_key(argv[1]);
    printf("%i\n", is_key_valid);
}

bool check_key(string key)
{
    char capital[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    bool check = true;
    for (int k = 0; k < KEY_LENGTH; k++)
    {
        if (!check)
        {
            break;
        }
        for (int c = 0; k < KEY_LENGTH; k++)
        {
            if (key[k] == capital[c])
            {
                break;
            }
        }
        check = false;
    }
    return check;
}