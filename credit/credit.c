#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

// int get_length(long card_number);
bool check_card(long card_number);

int main(void)
{
    // long card_number = get_long("Input card number: ");
    long card_number = 123456789;
    int card_length = get_length(card_number);
    bool is_card_valid = check_card(card_number);

    printf("%i\n", card_length);
    printf("%d\n", is_card_valid);

}

bool check_card(long card_number)
{

    int card_length = get_length(card_number);
    // for (int i = 0; i < card_length)

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
    return true;

}