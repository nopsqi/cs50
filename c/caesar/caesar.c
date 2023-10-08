#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char capital[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
int get_position(char c);
bool check_key(string key);
string encrypt(string plaintext, int key);

int main(int argc, string argv[])
{
    // argc = 2;
    // argv[1] = "13";
    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    if (!check_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int key = strtol(argv[1], NULL, 10);
    string plaintext = get_string("plaintext: ");
    string ciphertext = encrypt(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);
}

string encrypt(string plaintext, int key)
{
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (!isalpha(plaintext[i]))
        {
            continue;
        }
        int position = get_position(plaintext[i]);
        int caesar = (position + key) % 26;
        bool is_upper = isupper(plaintext[i]);
        plaintext[i] = is_upper ? toupper(capital[caesar]) : tolower(capital[caesar]);
    }
    return plaintext;
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

int get_position(char c)
{
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