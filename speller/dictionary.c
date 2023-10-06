// Implements a dictionary's functionality

#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
unsigned int get_bucket_size()
{
    unsigned int n = 0;
    for (int i = 0; i < LENGTH; i++)
        n += ('z' - 'A' + 1) * (i + 1);
    return n;
}
// const unsigned int N = 26;
const unsigned int N = get_bucket_size();

// Hash table
node *table[N];

FILE *dictionary_file = NULL;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int hashes_dictionary;
    unsigned int hashes_word = hash(word);
    printf("\n\n");
    printf("%lu\n", sizeof(node));
    printf("%u\n", hashes_word);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned int hash = 0;
    for (int i = 0, c = word[i]; c != '\0'; c = word[++i])
    {
        hash += (c - 'A' + 1) * (i + 1);
    }
    return hash;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    dictionary_file = fopen(dictionary, "r");
    if (dictionary_file == NULL)
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
