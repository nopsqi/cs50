#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Declare a pointer to a 2D array of integers
    int (*a)[5] = calloc(3, 5 * sizeof(int));

    printf("%i\n", a[0][0]);

    // Fill in the 2D array
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 5; j++) {
            a[i][j] = i * 5 + j; // Assigning values to the elements
        }
    }

    // Access and print the values
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    int (*b)[5] = malloc(5 * sizeof(int));
    printf("%p\n", b);
    for (int i = 0; i < 5; i++)
    {
        // b[i] = a[0][i];
        printf("%i\n", (*b)[i]);
    }

    // Don't forget to free the allocated memory when done
    free(a);

    return 0;
}
