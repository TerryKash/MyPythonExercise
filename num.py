import random
for num in range(10):
    randum_num = random.randint(1,11)
    num = input('Guess a no between 1-10 ')
    num = int(num)
    if randum_num == num:
        print(f'You won you modafuker!  {num}  ')
    elif randum_num >num:
        print('The number is to low')
    elif randum_num <num:
        print('The number is to high')
    else:
        print('You loose')