class Student:

    university = "Sri Sri University"

    def __init__(self, m1, m2, m3):     # what is self? It carries the information regarding the object through
        self.m1 = m1                    #                   which it was called.
        self.m2 = m2
        self.m3 = m3

    @staticmethod
    def normalPrint():
        print ("This is a static method as it is not related to any class or object")

    
    def avg(self):  #self because its a object function
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):  #class because its a class function
        return cls.university

s1 = Student(34,55,44)
s2 = Student(31,36,77)

print(s1.avg())
print(Student.info())