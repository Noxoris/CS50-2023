from cs50 import get_float

quarter_count = 0
dimes_count = 0
nickel_count = 0
pennie_count = 0
while True:
    cents = get_float("Change owed: ")
    if cents > 0:
        break

#round to fix problems with inaccuracy

cents = round(cents * 100)
while cents >= 25:
    cents -= 25
    quarter_count += 1
while cents >= 10:
    cents -= 10
    dimes_count += 1
while cents >= 5:
    cents -= 5
    nickel_count += 1
while cents >= 1:
    cents -= 1
    pennie_count += 1
coin_count = quarter_count + dimes_count + nickel_count + pennie_count
print(coin_count)
