#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
int* decimal_to_binary(int ascii);

int main(void)
{
    // TODO
    string message = "HI!";
    int *binary = decimal_to_binary((int)'H');
    for (int i = 0; i < 8; i++)
    {
        printf("%i", binary[i]);
    }
    printf("\n");

}

int* decimal_to_binary(int ascii)
{
    static int result[BITS_IN_BYTE];
    for (int i = BITS_IN_BYTE-1; i > 0; i--)
    {
        // printf("%i ", ascii);
        int reminder = ascii % 2;
        result[i] = reminder;
        // printf("%i\n", reminder);
        ascii = ascii / 2;
    }
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
