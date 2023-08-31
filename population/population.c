#include <cs50.h>
#include <stdio.h>

int get_number(void);

int main(void)
{
    // TODO: Prompt for start size
    int start_size = get_number("Start size: ");
    // TODO: Prompt for end size
    printf("%i\n", start_size);
    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}

int get_number(string description)
{
    int n;
    do
    {
        n = get_int(description);
    }
    while (n < 1);
    return n;
}
