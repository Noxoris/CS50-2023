from cs50 import get_int

while True:
        height = get_int("Height: ")
        if height <= 8 and height >= 1:
            break

i = 1
spaces = height - 1
while i <= height:
    print(spaces * " " + i * "#")
    i += 1
    spaces -= 1

