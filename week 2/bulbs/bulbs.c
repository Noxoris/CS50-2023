#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string input = get_string("Message: ");
    for (int i = 0; i < strlen(input); i++) {
       //https://stackoverflow.com/questions/6660145/convert-ascii-number-to-ascii-character-in-c
        int dec = input[i];
        int bin[BITS_IN_BYTE];
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
        //How to get binary conversionn: i / 2
        //Get the integer quotient for the next iteration.
        // Remmainder = binary digit
        //Repeat the steps until the quotient is equal to 0.
            bin[j] = dec % 2;
            dec = dec / 2;
        }
        for (int light = BITS_IN_BYTE - 1; light >= 0; light--)
        {
            print_bulb(bin[light]);
        }

        printf("\n");
    }

}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
