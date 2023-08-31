#include <cs50.h>
#include <stdio.h>
#include <math.h>

int get_start_size(void);
int get_end_size(int start_size);

int main(void)
{
    // TODO: Prompt for start size
    int start_size = get_start_size();
    // TODO: Prompt for end size
    int end_size = get_end_size(start_size);
    // TODO: Calculate number of years until we reach threshold
    int year = 0;
    int end_size_calculate = start_size;
    while (end_size_calculate < end_size)
    {
        end_size_calculate = end_size_calculate + round(end_size_calculate / 3) - (end_size_calculate / 4);
        year++;
    }
    // TODO: Print number of years
        printf("Years: %i\n", year);

}

int get_start_size(void)
{
    int n;
    do
    {
        n = get_int("Enter start size: ");
    }
    while (n < 9);
    return n;
}

int get_end_size(int start_size)
{
    int n;
    do
    {
        n = get_int("Enter end size: ");
    }
    while (n < start_size);
    return n;
}
