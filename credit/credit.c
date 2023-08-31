#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int get_length(long card_number);
bool check_card(long card_number);
int sum_digit(int digit);

int main(void)
{
    // long card_number = get_long("Input card number: ");
    long card_number = 123456789;
    int card_length = get_length(card_number);
    bool is_card_valid = check_card(card_number);
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

bool check_card(long card_number)
{
    int luhn_last_digit = 0;
    int card_length = get_length(card_number);
    for (int i = 1; i < card_length; i+=2)
    {
        int number_now = (card_number / (long)pow(10, i)) % 10;
        number_now *= 2;

        if (number_now % 10 != number_now)
        {
            number_now = sum_digit(number_now);
        }
        luhn_last_digit += number_now;
        // printf("%i\n", number_now);
        // printf("=> %i\n", number_now % 10);
    }
    for (int i = 0; i < card_length; i+=2)
    {
        luhn_last_digit += 
    }
    return true;
}

int sum_digit(int digit)
{
    int sum = 0;
    while (digit != 0)
    {
        sum = sum + (digit % 10);
        digit /= 10;
    }
    return sum;
}