#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card_number = get_long("Input card number: ");
    printf("%d\n", card_number % 10000);
}