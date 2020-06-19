from abc import ABC, abstractmethod

print("*** Area Printing for Quadrilateral ***")
print("Enter...\n1 for Rectangle\n2 for Square\n3 for Rhombus\n4 for Trapezium")
inp = int(input())

class Quadrilateral(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Quadrilateral):
    def __init__(self, length, base):
        self.length = length
        self.base = base

    def printarea(self):
        return self.length*self.base

class Square(Quadrilateral):
    def __init__(self, side):
        self.side = side
    def printarea(self):
        return self.side**2

class Rhombus(Quadrilateral):
    def __init__(self, diag1, diag2):
        self.diag1 = diag1
        self.diag2 = diag2
    def printarea(self):
        return (self.diag1*self.diag2)/2

class Trapezium(Quadrilateral):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    def printarea(self):
        return (self.base1 + self.base2) * self.height / 2

if inp == 1:
    rec = Rectangle(int(input("Enter length: ")), int(input("Enter base: ")))
    print("Calculating Area...")
    print("The Area is ", end="")
    print(rec.printarea())

elif inp == 2:
    sq = Square(int(input("Enter base: ")))
    print("Calculating Area...")
    print("The Area is ", end="")
    print(sq.printarea())

elif inp == 3:
    rhom = Rhombus(int(input("Enter 1st Diagonal: ")), int(input("Enter 2nd Diagonal: ")))
    print("Calculating Area...")
    print("The Area is ", end="")
    print(rhom.printarea())

else:
    trap = Trapezium(int(input("Enter 1st base: ")), int(input("Enter 2nd base: ")), int(input("Enter height: ")))
    print("Calculating Area...")
    print("The Area is ", end="")
    print(trap.printarea())