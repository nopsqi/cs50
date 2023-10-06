// Implements a dictionary's functionality

#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
// const unsigned int N = 26;
// N = Σ_(i = 0)^(LENGTH) ('z' - 'A' + 1) * (i + 1) ≈ 60000;
const unsigned int N = 1000;

// Hash table
node *table[N] = {NULL};

FILE *dictionary_file = NULL;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int hashes_word = hash(word);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int hash = 0;
    printf("\n");
    // for (int i = 0, c = word[i]; c != '\0'; c = word[++i])
    for (int i = 0; word[i] != '\0'; i++)
    {
        char c = toupper(word[i])
        c = c > 'A' && <= 
        // hash += (toupper(c) - 'A' + 1) * (i + 1);
        // hash += pow((toupper(c) - 'A' + 1) / (i + 1), i + 1);
        hash += (toupper(word[i]) - 'A' + 1) * pow(i + 1, 2);
        // hash += toupper(c) - 'A' + 1;
        // hash += pow((toupper(c) - 'A' + 1) * (i + 1), 2);
        // hash += pow(toupper(c) - 'A' + 1, i + 1);
        // printf("%c,", c);
        if (i > 1)
            break;
    }
    return abs(hash - 1);
}

bool create_hash_table(void)
{
    int index = 0, words = 0;
    char word[LENGTH + 1];
    char c;
    while (fread(&c, sizeof(char), 1, dictionary_file))
    {
        // Allow only alphabetical characters and apostrophes
        if (isalpha(c) || (c == '\'' && index > 0))
        {
            // Append character to word
            word[index] = c;
            index++;

            // Ignore alphabetical strings too long to be words
            if (index > LENGTH)
            {
                // Consume remainder of alphabetical string
                while (fread(&c, sizeof(char), 1, dictionary_file) && isalpha(c));

                // Prepare for new word
                index = 0;
            }
        }

        // We must have found a whole word
        else if (index > 0)
        {
            // Terminate current word
            word[index] = '\0';

            // Update counter
            words++;

            unsigned int hashes_word = hash(word);
            node *ptr = malloc(sizeof(node));
            if (ptr == NULL)
            {
                return false;
            }
            strcpy(ptr->word, word);
            printf("linked list created %s %u\n", word, hashes_word);
            if (table[hashes_word] == NULL)
            {
                ptr->next = NULL;
                table[hashes_word] = ptr;
            }
            else
            {
                ptr->next = table[hashes_word];
                table[hashes_word] = ptr;
            }

            // Prepare for next word
            index = 0;
        }

        // if (words > 50)
        //     return false;
    }

    return true;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    dictionary_file = fopen(dictionary, "r");
    if (dictionary_file == NULL)
        return false;

    if (!create_hash_table())
        return false;

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
