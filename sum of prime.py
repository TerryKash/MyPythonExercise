# sum of prime
n = int(input("Enter the number: "))
l1 = []
for i in range(1, n+1):
    c=0
    for j in range(1, i+1):
        if i%j==0:
            c+=1
    if c==2:
        l1.append(i)
        print(l1)

for i in range(0, len(l1)):
    for j in range(i, len(l1)):
        if l1[i]+l1[j]==n:
            # print('{0} + {1}'.format(l1[i], l1[j]), end=", ")
            print(f'{l1[i]} + {l1[j]}', end=', ')