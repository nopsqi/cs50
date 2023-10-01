#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
        // First statement
    int *arr = malloc(5 * sizeof(int));

    // Initialize the elements of the array
    for (int i = 0; i < 5; i++) {
        arr[i] = i;
    }

    // Print the elements of the array
    for (int i = 0; i < 5; i++) {
        printf("%d\n", arr[i]);
    }

    // Second statement
    int (*arr1)[5] = malloc(5 * sizeof(int));

    // Initialize the elements of the array
    for (int i = 0; i < 5; i++) {
        (*arr1)[i] = i;
    }

    // Print the addresses of the elements of the array
    for (int i = 0; i < 5; i++) {
        printf("%p\n", &(*arr1)[i]);
    }

}
