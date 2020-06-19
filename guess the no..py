print('*** GUESS THE NUMBER***')
n = 18
a = 1
while a <= 5:
    user = int(input('Enter the Number: '))
    a = a + 1
    if user > n:
        print('Your Number is Larger!!')
        print(f'You have only {6-a} chance left')
        continue
    elif user < n:
        print('Your Number is Smaller!!')
        print(f'You have only {6-a} chance left')
        continue
    elif user == n:
        print('You Won!!')
        print(f'You took {a-1} no. of guesses!!')
        break


if a > 5:
    print('Game Over!!')
    print('You Lost!!')