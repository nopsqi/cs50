#include <cs50.h>
#include <stdio.h>

int get_number(string description);

int main(void)
{
    // TODO: Prompt for start size
    int start_size = get_number("Start size: ");
    // TODO: Prompt for end size
    int end_size = get_number("End size: ");
    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years

    printf("%i %i\n", start_size, end_size);
}

int get_number(string description)
{
    int n;
    do
    {
        n = get_int("%s", description);
    }
    while (n < 1);
    return n;
}
