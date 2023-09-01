#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

char capital[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
char lower[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
const int KEY_LENGTH = 26;
bool check_key(string key);

int main(int argc, string argv[])
{
    argc = 2;
    argv[1] = "YTNSHKVEFXRBAUQZCLWDMIPGJO";
    if (argc < 2 || argc > 2)
    {
        printf("%s\n", "Usage: ./subtition key");
        return 1;
    }
    if (strlen(argv[1]) < KEY_LENGTH)
    {
        printf("%s\n", "Key length must be 26.");
        return 1;
    }
    printf("%s\n", argv[1]);
    bool is_key_valid = check_key(argv[1]);
    printf("%i\n", is_key_valid);
}

bool check_key(string key)
{
    bool check = true;
    for (int k = 0; k < KEY_LENGTH; k++)
    {
        if (!isalpha(key[k]))
        {
            check = false;
            break;
        }
        if (islower(key[k]))
        {
            check = false;
            break;
        }
        for (int l = 0; l < KEY_LENGTH; k++)
        {
            if (key[k] == key[l] && k != l){
                check = false;
                break;
            }
        }
    }
    return check;
}