import re

str = '''

'''
patt = re.compile(r'\w+@\S+\w')
# patt = re.compile(r'\B@+')

match = patt.finditer(str)
for matches in match:
    with open("Emails.txt", "a") as f:
        t = matches.group()
        print(t)
        f.write(t)
        f.write("\n")