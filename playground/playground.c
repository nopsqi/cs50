#include <stdio.h>
#include <cs50.h>
#include <string.h>

int arr[5] = {3, 1, 2, 4, 1};
void sort_arr(int array[]);

int main()
{
    sort_arr(arr);
}

void sort_arr(int array[])
{
    bool swap = true;
    while(swap)
    {
        swap = false;
        for (int i = 0; i < 4; i++)
        {
            if (array[i] > array[i+1])
            {
                int temp = array[i];
                array[i] = array[i+1];
                array[i+1] = temp;
                swap = true;
            }
        }
    }
    return;
}