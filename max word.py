name = input('enter file: ')
fil = open(name)
words = fil.read().split()

b = (max(words , key = len))
print(b)