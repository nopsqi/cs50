#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
string decimal_to_binary(int ascii);

int main(void)
{
    // TODO
    string message = "HI!";
    string binary = decimal_to_binary((int)'H');
    printf("%s\n", binary);

}

string decimal_to_binary(int ascii)
{
    string result = "00000000";
    for (int i = BITS_IN_BYTE; i > 0; i--)
    {
        // printf("%i ", ascii);
        int reminder = ascii % 2;
        result[i] = 'a';
        // printf("%i\n", reminder);
        ascii = ascii / 2;
    }
    printf("\n");
    return result;
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
