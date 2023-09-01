#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

const int KEY_LENGTH = 26;
bool check_key(string key);
string encrypt(string plaintext, string key);

int main(int argc, string argv[])
{
    argc = 2;
    argv[1] = "YTNSHKVEFXRBAUQZcLWDMIPGJO";
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
    if (!check_key(argv[1]))
    {
        printf("Error: Input valid key (26 uppercase non repeated alphabetic character)\n");
        return 1;
    }
    string plaintext = get_string("Input plaintext: ");
}

bool check_key(string key)
{
    bool check = true;
    for (int k = 0; k < KEY_LENGTH; k++)
    {
        if (!check)
        {
            break;
        }
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
        for (int l = 0; l < KEY_LENGTH; l++)
        {
            if (key[k] == key[l] && k != l){
                check = false;
                break;
            }
        }
    }
    return check;
}

string encrypt(string plaintext, string key)
{
    for (int p = 0; p < strlen(plaintext); p++)
    {
        if (!isalpha(plaintext[p]))
        {
            continue;
        }
        bool is_upper = isupper(plaintext[p]);
        
    }
    return 0;
}