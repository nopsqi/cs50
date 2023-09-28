#include <stdio.h>
#include <cs50.h>
#include <string.h>
#define N 7
int arr[N] = {3, 1, 1, 2, 4, 2, 5};

void sort_arr();
bool return_true();

int main()
{
    sort_arr();
    for (int i = 0; i < N; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");
    printf("%i\n", return_true());
}

bool return_true()
{
    return 1;
}

void sort_arr()
{
    bool swap = true;
    while(swap)
    {
        swap = false;
        for (int i = 0; i < N-1; i++)
        {
            if (arr[i] > arr[i+1])
            {
                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swap = true;
            }
        }
    }
    return;
}