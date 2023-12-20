class A:

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

#mentioning A in brackets makes it a child class of Class A
class B(A):

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C():

    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")

class D(A,C):   #here the class is inheriting from class A as well as from class C --> this is called multiclass inheritance

    def feature7(self):
        print("Feature 7 is working")

    def feature8(self):
        print("Feature 8 is working")

A1 = A()
A1.feature1()
A1.feature2()

A2= B()         #after making B child class of A, methods of A are available to B
A2.feature3
