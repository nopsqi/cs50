#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int coleman(string text);
int count_sentences(string text);
int count_words(string text);
int count_letters(string text);
bool is_alphabet(char c);

int main(void)
{
    string text = get_string("Input text: ");
    // string text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!";
    int grade = coleman(text);
    if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int coleman(string text)
{
    int sentences = count_sentences(text);
    int words = count_words(text);
    int letters = count_letters(text);
    float l = (float)letters / (float)words * (float)100;
    float s = (float)sentences / (float)words * (float)100;
    float index = 0.0588 * l - 0.296 * s - 15.8;
    return round(index);
}

int count_sentences(string text)
{
    int counter = 0;
    int length = strlen(text);
    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            counter++;
        }
    }
    return counter;
}

int count_words(string text)
{
    int counter = 1;
    int length = strlen(text);
    for (int i = 0; i < length; i++)
    {
        if (text[i] == ' ')
        {
            counter++;
        }
    }
    return counter;
}

int count_letters(string text)
{
    int counter = 0;
    int length = strlen(text);
    for (int i = 0; i < length; i++)
    {
        if (is_alphabet(text[i]))
        {
            counter++;
        }
    }
    return counter;
}

bool is_alphabet(char c)
{
    char alphabet[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    bool check = false;
    for (int i = 0; i < 52; i++)
    {
        if (c == alphabet[i])
        {
            check = true;
            break;
        }
    }
    return check;
}