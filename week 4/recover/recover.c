#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        //https://www.geeksforgeeks.org/command-line-arguments-in-c-cpp/
        printf("Usage: ./recover image\n");
        return 1;
    }

    FILE *inptr = fopen(argv[1], "r");

    if (inptr == NULL)
    {
        printf("Unable to open file %s\n", argv[1]);
        return 2;
    }

    FILE *outptr = NULL;

    BYTE buffer[512];

    char file_name[8];

    int file_count = 0;

    while (fread(buffer, sizeof(BYTE) * 512, 1, inptr) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (outptr != NULL)
            {
                fclose(outptr);
            }

            sprintf(file_name, "%03i.jpg", file_count);

            outptr = fopen(file_name, "w");

            file_count += 1;
        }

        if (outptr != NULL)
        {
            fwrite(buffer, sizeof(BYTE) * 512, 1, outptr);
        }
    }
    fclose(outptr);
    fclose(inptr);
}






