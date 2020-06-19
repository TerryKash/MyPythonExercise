print('This is your shopping cart')

shopping_list = {}

k = "y"
while k != "n":
    shopping_list[input('Enter Item: ')] = int(input('Enter price: '))
    k = input('Add more? (y/n): ')

for k,v in sorted(shopping_list.items()):
    print(f'{k} is of Rs {v}')

values = sum(shopping_list.values())
print(f'The total of price is Rs{values}')