#include <cs50.h>
#include <stdio.h>

int coleman(string text);

int main(void)
{
    // string text = get_string("Input text: ");
    string text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!";
    int grade = coleman(text);
}

int coleman(string text)
{
    int index = 0;
    int sentences = count_snetences();
    int letters = count_letters();
    int words = count_words();
    float l = letters / words * 100
    float s = sentences / words * 100
    index = 0.0588 * l - 0.296 * s - 15.8
    return index;
}

int count_sentences(stirng text)
{
    
}