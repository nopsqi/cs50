#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
int *decimal_to_binary(int ascii);
void encrypt(string message);

int main(void)
{
    // TODO
    // string message = "HI!";
    string message = get_string("Message: ");
    encrypt(message);
}

void encrypt(string message)
{
    for (int i = 0; i < strlen(message); i++)
    {
        int *binary = decimal_to_binary((int) message[i]);
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            // printf("%i", binary[j]);
            print_bulb(binary[j]);
        }
        printf("\n");
    }
}

int *decimal_to_binary(int ascii)
{
    static int result[BITS_IN_BYTE];
    for (int i = BITS_IN_BYTE - 1; i > 0; i--)
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
