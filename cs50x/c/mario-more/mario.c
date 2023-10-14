#include <cs50.h>
#include <stdio.h>

void print_row(int indent, int brick);

int main(void)
{
    int n;
    do
    {
        n = get_int("Input number: ");
    }
    while (n < 1 || n > 8);
    for (int i = 0; i < n; i++)
    {
        int indent = n - i - 1;
        int brick = n - indent;
        print_row(indent, brick);
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
    printf("  ");
    for (int j = 0; j < brick; j++)
    {
        printf("#");
    }
    printf("\n");
}