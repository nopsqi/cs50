#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("Input number: ");
    for (int i = 0; i < n; i++)
    {
        int indent = n - i - 1;
        int brick = n - indent;
        printf("%i %i\n", indent, brick);
        // for (int j = 0; j < n*2; j++)
        // {
        //     printf("#");
        // }
        // printf("\n");
    }
}