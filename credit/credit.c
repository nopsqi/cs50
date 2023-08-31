#include <cs50.h>
#include <stdio.h>

int get_length(long card_number);

int main(void)
{
    // long card_number = get_long("Input card number: ");
    long card_number = 123456789;
    int card_length = get_length(card_number);
    
    printf("%i\n", card_length);
}

int get_length(long card_number)
{
    int length = 0;
    while (card_number != 0)
    {
        card_number /= 10;
        length++;
    }
    return length;
}