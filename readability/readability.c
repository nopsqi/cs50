#include <cs50.h>
#include <stdio.h>
#include <string.h>

int coleman(string text);
int count_sentences(string text);
int count_words(string text);
int count_letters(string text);

int main(void)
{
    // string text = get_string("Input text: ");
    string text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!";
    int grade = coleman(text);
    printf("%i\n", grade);
}

int coleman(string text)
{
    int index = 0;
    int sentences = count_sentences(text);
    int words = count_words(text);
    int letters = count_letters(text);
    // float l = letters / words * 100
    // float s = sentences / words * 100
    // index = 0.0588 * l - 0.296 * s - 15.8
    return letters;
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
        if (text[i] == '.' || text[i] == '!' || text[i] == '?' || text[i] == ' ')
        {
            counter++;
        }
    }
    return length - counter;
}