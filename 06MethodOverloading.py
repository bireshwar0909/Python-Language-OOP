# although we dont have method overloading here like we see in java, c++ etc
# however we can achieve it through a different way.

class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a!= None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        elif a!= None:
            s = a
        print (s)

s1 = Student(10,12)
s1.sum(11,12,13)
s1.sum(12,12)
s1.sum(16)