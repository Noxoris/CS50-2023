#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <string.h>


int count_letters(string text);
int count_word(string text);
int count_sentences(string text);

int main(void)
{
    string input = get_string("Text: ");

    int grade = 0;

    //I used double instead of float, to resolve potential issues with truncation
    double L = count_letters(input) / (float)count_word(input) * 100;
    double S = count_sentences(input) / (float)count_word(input) * 100;

    //index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(0.0588 * L - 0.296 * S - 15.8);

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
        printf("Grade %d\n", grade);
    }
}

int count_letters(string text)
{
    int letter_count = 0;
    for (int i = 0; i < strlen(text); i++) {
        if (isalpha(text[i])) {
            letter_count++;
        }
    }
    return letter_count;
}

int count_word(string text)
{
    int word_count = 1;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            word_count++;
        }
    }
    return word_count;
}

int count_sentences(string text)
{
    int sentences_count = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences_count++;
        }
    }
    return sentences_count;
}
