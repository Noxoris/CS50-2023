#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {   //3.0 instead of 3 to round average correctly
            int avg_pixel_value = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue)/3.0);
            image[i][j].rgbtRed = avg_pixel_value;
            image[i][j].rgbtGreen = avg_pixel_value;
            image[i][j].rgbtBlue = avg_pixel_value;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            //Sepia formula taken from official walkthrough video
            //https://youtu.be/m0_vouQLufc?list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut

            //Sepia Red
            int sepia_red = round(originalRed * 0.393 + originalGreen * 0.769 + originalBlue * 0.189);
            if (sepia_red > 255)
            {
                sepia_red = 255;
            }
            //Sepia Green
            int sepia_green = round(originalRed * 0.349 + originalGreen * 0.686 + originalBlue * 0.168);
            if (sepia_green > 255)
            {
                sepia_green = 255;
            }
            //Sepia Blue
            int sepia_blue = round(originalRed * 0.272 + originalGreen * 0.534 + originalBlue * 0.131);
             if (sepia_blue > 255)
            {
                sepia_blue = 255;
            }

           image[i][j].rgbtRed = sepia_red;
           image[i][j].rgbtGreen = sepia_green;
           image[i][j].rgbtBlue = sepia_blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE stored_image;
   for (int i = 0; i < height; i++)
    {
    // We need to divide by two, because otherwise we will reflect image twice and nothing will change
    for (int j = 0; j < width / 2; j++)
        {
            stored_image = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = stored_image;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE stored_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float counter = 0;
            int red = 0;
            int green = 0;
            int blue = 0;
            for (int x = i - 1; x <= i + 1; x++)
            {
                if (x < 0 || x >= height)
                {
                    continue;
                }
                for (int y = j - 1; y <= j + 1; y++)
                {
                    if (y < 0 || y >= width)
                    {
                      continue;
                    }
                red += image[x][y].rgbtRed;
                green += image[x][y].rgbtGreen;
                blue += image[x][y].rgbtBlue;
                counter += 1;
                }
            }
            stored_image[i][j].rgbtRed = round(red / counter);
            stored_image[i][j].rgbtGreen = round(green / counter);
            stored_image[i][j].rgbtBlue = round(blue / counter);
        }

    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = stored_image[i][j];
        }
    }

    return;
}
