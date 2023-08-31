#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int get_length(long card_number);
bool check_card(long card_number);
int sum_digit(int digit);
int get_digit(long card_number, int position);

int main(void)
{
    // long card_number = get_long("Input card number: ");
    long card_number = 4062901840;
    int card_length = get_length(card_number);
    int card_first_digit = get_digit(card_number, card_length-1);
    int card_second_digit = get_digit(card_number, card_length-2);
    bool is_card_valid = check_card(card_number);
    if (is_card_valid == 0)
    {
        printf("INVALID\n");
        return 0;
    }
    if (card_first_digit == 5 && (card_second_digit == 1 || card_second_digit == 2 || card_second_digit == 3 || card_second_digit == 4 || card_second_digit == 5))
    {
        printf("MASTERCARD\n");
        return 0;
    }
    if (card_first_digit == 3 && (card_second_digit == 4 || card_second_digit == 7))
    {
        printf("AMEX\n");
        return 0;
    }
    if (card_first_digit == 4)
    {
        printf("VISA\n");
        return 0;
    }
    else
    {
        printf("INVALID\n");
        return 0;
    }
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
        int number_now = get_digit(card_number, i);
        printf("=> %i\n", number_now);
        number_now *= 2;
        printf("%i\n", number_now);

        if (number_now % 10 != number_now)
        {
            number_now = sum_digit(number_now);
        }
        printf("%i\n", number_now);
        luhn_last_digit += number_now;
        // printf("%i\n", number_now);
        // printf("=> %i\n", number_now % 10);
    }
    for (int i = 0; i < card_length; i+=2)
    {
        int number_now = get_digit(card_number, i);
        luhn_last_digit += number_now;
    }
    printf("%d\n", luhn_last_digit);
    luhn_last_digit = luhn_last_digit % 10;
    return (luhn_last_digit == 0);
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

int get_digit(long card_number, int position)
{
    int digit = (card_number / (long)pow(10, position)) % 10;
    return digit;
}