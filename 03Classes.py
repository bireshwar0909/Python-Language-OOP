#class inside a class

class Student:

    def __init__(self, rollNo, name):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()    # if we want to create an object of laptop we have to do it through the outer class
                                    #   since the Laptop is an inner class. 

    def show(self):
        print (self.rollNo, self.name)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student(1, "Bireshwar")
s2 = Student(2, "Upasana")

s1.show()
s2.show()

#creating a object for the inner class
lap1 = Student.Laptop()