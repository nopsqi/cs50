#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // long card_number = get_long("Input card number: ");
    long card_number = 123456789;
    printf("%ld\n", (card_number /= 1000000000));
}