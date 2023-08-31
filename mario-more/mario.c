#include <cs50.h>
#include <stdio.h>

void print_row(int indent, int brick);

int main(void)
{
    int n = get_int("Input number: ");
    for (int i = 0; i < n; i++)
    {
        int indent = n - i - 1;
        int brick = n - indent;
        print_row(indent, brick);
        // printf("%i %i\n", indent, brick);
    }
}

void print_row(int indent, int brick)
{
    for (int j = 0; j < indent; j++)
    {
        printf(" ");
    }
    for (int j = 0; j < brick; j++)
    {
        printf("#");
    }
    printf(" ");
    for (int j = 0; j < brick; j++)
    {
        printf("#");
    }
    for (int j = 0; j < indent; j++)
    {
        printf(" ");
    }
    printf("\n");
}