// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
// const unsigned int N = 26;
const unsigned int N = 100000;

// Hash table
node *table[N] = {NULL};

FILE *dictionary_file = NULL;
unsigned int *words = NULL;

bool search_dictionary(node *n, const char *word)
{
    if (n == NULL)
        return false;
    if (strcmp(n->word, word) == 0)
        return true;
    if (n->next != NULL)
        return search_dictionary(n->next, word);
    return false;
}

char *sanitize(const char *word)
{
    char *sanitized_word = calloc(1, (LENGTH + 1) * sizeof(char));
    for (int i = 0; word[i] != '\0'; i++)
    {
        sanitized_word[i] = tolower(word[i]);
    }
    return sanitized_word;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    char *sanitized_word = sanitize(word);
    unsigned int hashes_word = hash(word);
    bool status = search_dictionary(table[hashes_word], sanitized_word);
    free(sanitized_word);
    return status;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // int n = 0;
    // int d = 0;
    long int h = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        char c = toupper(word[i]);
        c = c >= 'A' && c <= 'Z' ? c - 'A' + 1 : c;
        // long int tmp = 0;
        // for (int j = 0; word[j] != '\0'; j++)
        // {
        //     char c1 = toupper(word[j]);
        //     c1 = c1 >= 'A' && c1 <= 'Z' ? c1 - 'A' + 1 : c1;
        //     tmp += abs(c1 * (j + 1) - c * (1 + 1));
        // }
        // h += tmp * (c / 100);
        // h += tmp;
        // h += (c * pow(i + 1, 3));
        // h += round(pow(c, i + 1) / (float) pow(i + 1, i + 1));
        // h += pow(c, i + 1);
        h += c * (i + 1);
        // d += (c * pow(i + 1, 3));
        // h += pow(c, i + 1);
        // d += c * (i + 1);
        // n++;
    }
    return labs(h);
}

bool create_hash_table(void)
{
    int index = 0;
    words = malloc(sizeof(int));
    *words = 0;
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
                while (fread(&c, sizeof(char), 1, dictionary_file) && isalpha(c))
                    ;

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
            (*words)++;

            unsigned int hashes_word = hash(word);
            node *ptr = malloc(sizeof(node));
            if (ptr == NULL)
                return false;

            strcpy(ptr->word, word);
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
    return *words;
}

void free_hash_table(node *n)
{
    if (n == NULL)
        return;
    if (n->next != NULL)
        free_hash_table(n->next);
    free(n);
    return;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    fclose(dictionary_file);
    for (int i = 0; i < N; i++)
        free_hash_table(table[i]);
    free(words);
    return true;
}
