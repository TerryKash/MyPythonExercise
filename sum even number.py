def add_even_number():

    total = 0
    for number in range(0, num):
        if number % 2 == 0:
            total += number

    return total


num = int(input("Enter the range: "))
print(add_even_number())