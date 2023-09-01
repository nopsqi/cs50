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
}

bool check_key(string key)
{
    
}