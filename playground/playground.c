#include <stdio.h>
#include <cs50.h>
#include <string.h>

int arr[5] = {3, 1, 2, 4, 1};
void sort_arr();

int main()
{
    sort_arr();
}

void sort_arr()
{
    bool swap = true;
    while(swap)
    {
        swap = false;
        for (int i = 0; i < 4; i++)
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