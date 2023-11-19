#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start;
    int end;
    int years;

    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    for (years = 0; start < end; years++)
    {
        start = start + (start / 3) - (start / 4);
    }

    printf("Years: %i\n", years);
}
