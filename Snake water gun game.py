import random

print('***SNAKE WATER GUN***\n')
print('You have 10 chance\n')

op = ['snake', 'water', 'gun']
choice = random.choice(op)
p = 0
c = 0
i = 0
a = 10
while i < 10:
    i += 1
    a -= 1
    print('Enter:\ns for snake\nw for water\ng for gun')
    g = input('Enter what you choose: ')
    print('Computer choose: ' + choice)

    if g == 's' and choice == 'snake':
        print("It's a tie\n")
    elif g == 's' and choice == 'water':
        p += 1
        print('You win\n')
    elif g == 's' and choice == 'gun':
        c += 1
        print('Comp win\n')
    elif g == 'w' and choice == 'snake':
        c += 1
        print('Comp win\n')
    elif g == 'w' and choice == 'water':
        print("It's a tie\n")
    elif g == 'w' and choice == 'gun':
        p += 1
        print('You win\n')
    elif g == 'g' and choice == 'snake':
        c += 1
        print('You win\n')
    elif g == 'g' and choice == 'gun':
        print("It's a tie\n")
    elif g == 'g' and choice == 'water':
        c += 1
        print('Comp win\n')
    else:
        print('Wrong input!!!\n')

    print(f'You have {a} chance left\n')

print(f'Your Score {p}')
print(f'Computer Score {c}')
if p > c:
    print('You Win!!!')
elif p < c:
    print('Computer Win!!!')
else:
    print("It's a Tie!!!")