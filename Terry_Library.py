print("**** WELCOME TO TERRY LIBRARY ****")

lb = open("Library book.txt", "w")
lb.write("50 Shades of Grey\nSacred Games\n13 Reasons Why\nHarry Potter and the Philosopher's Stone\n"
         "The Intelligent Investor\nRich Dad Poor Dad\nHalf Girlfriend\n2 States\n"
         "The Immortal Meluha\nWhite Tiger\nNectar in a Sieve\nThe Great Indian Novel\n"
         "A Fine Balance\nThe Book thief\nThe Lord of the Rings\nRomeo and Juliet\n"
         "The Guide\nThe Glass Palace\nGitanjali\nIn Custody\n")
lb.close()

class TerryLibrary:
    user = input("Enter your Name: ")
    print(f'Hi {user}! What do you wanna do?')
    lb = open("Library book.txt")
    b = lb.read()
    book_list = b.split("\n")

    def display_book(self):
        for books in self.book_list:
            print(books)

class LendBook(TerryLibrary):
    def __init__(self, lend1):
        self.lend1 = lend1

    def lend_book(self):
        if self.lend1 in self.book_list:
            self.book_list.remove(self.lend1)
            print('OK you can lend it.')
            with open("Library book.txt") as f:
                lines = f.readlines()
            with open("Library book.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != self.lend1:
                        f.write(line)
            # print(books_list)
        elif self.lend1 not in self.book_list:
            print(f"Do you wanna know who lend {self.lend1} book? Press y for Yes and n for No. ")
            i = input()
            if i == "y":
                lend_dic = {}
                lend_dic[self.user] = self.lend1
                print(lend_dic)
                for k, v in lend_dic.items():
                    print(f'{k} lend {v} book')
            else:
                print("You can exit")
        else:
            print(f"SORRY!\n{self.lend1} book is not available.")

class ReturnBook(TerryLibrary):
    def return_book(self):
        if self.book_list in user:
            
            while True:
                ret = input("Enter which book do you want to return? Press done to exit. ")
                if ret == "done":
                    break
            self.book_list.append(ret)
            with open("Library book.txt", "a") as f:
                f.write(ret)
                f.write("\n")


class DonateBook(TerryLibrary):
    def donate_a_book(self):
        while True:
            don = input("Enter the book name. Type done to exit. ")
            if don == "done":
                break
            self.book_list.append(don)
            with open("Library book.txt", "a") as f:
                f.write(don)
                f.write("\n")


q = "y"
while q != "n":
    print('Enter\n1 for Display books\n2 for Lend a book\n3 for Donate a book\n4 for Return a book')
    inp = int(input("Enter Here: "))
    if inp == 1:
        user = TerryLibrary()
        user.display_book()
    elif inp == 2:
        user = LendBook(lend1 = input("Which book do you want to lend? "))
        user.lend_book()
    elif inp == 3:
        user = DonateBook()
        user.donate_a_book()
    elif inp == 4:
        user = ReturnBook()
        user.return_book()

    q = input("Press y to continue & n to exit: ")
