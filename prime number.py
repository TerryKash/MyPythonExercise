# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
# num = int(input("Enter number: "))
for num in range(0, 100):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
            # print(num, "is not prime number")
            # print(f"{i} times {num//i} is {num}")
                break
        else:
            print(num, end="\n")
