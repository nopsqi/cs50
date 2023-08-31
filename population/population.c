#include <cs50.h>
#include <stdio.h>
#include <math.h>

int get_number(string description);

int main(void)
{
    // TODO: Prompt for start size
    int start_size = get_number("Start size: ");
    // TODO: Prompt for end size
    int end_size = get_number("End size: ");
    // TODO: Calculate number of years until we reach threshold
    int year = 0;
    int end_size_calculate = start_size;
    while (end_size_calculate > end_size)
    {
        end_size_calculate = end_size_calculate + round(end_size_calculate / 3) - (end_size_calculate / 4);
        year++;
        printf("%i %i\n", year, end_size_calculate);
    }
    // TODO: Print number of years

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
