# 0 1 1 2 3 5 8 13 21

def feb(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return feb(n-1) + feb(n-2)

n = int(input('Enter the no.: '))
print(feb(n))