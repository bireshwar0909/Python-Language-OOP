class A:  # A is a superclass since B is inheriting from A

    def __init__(self):
        print("From init Class A")

    def feature1(self):
        print("Feature 1A is working")

    def feature2(self):
        print("Feature 2 is working")


class B(A):  # B is a subclass

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


class C(A):  # C is a subclass

    def __init__(self):
        print("init from class C")

    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")

# for super function!


class D(A):  # D is a subclass

    def __init__(self):
        super().__init__()
        print("init from class C")

    def feature7(self):
        print("Feature 7 is working")

    def feature8(self):
        print("Feature 8 is working")

#


class E():

    def __init__(self):
        print("init from class E")

    def feature1(self):
        print("Feature 1E is working")

    def feature9(self):
        print("Feature 9 is working")

# for concept of MRO -> Method Resolution Order -> It will always start from left to right
class F(A, E):

    def __init__(self):
        super().__init__()          #although both A and E had constructor, it called the constructor of A
        print("init from class F")

    def feature11(self):
        print("Feature 11 is working")

    def feature12(self):
        print("Feature 12 is working")


a1 = A()
a1.feature1()

# here we can see that even though we have created an object a2 from class B it is still calling the constructor of A.
a2 = B()

# but what if a subclass has its own constructor??
a3 = C()

a4 = F()
a4.feature1()   # we have feature1 in both A and E but it will call the one from A

# we can see that it called its own constructor. So what we can conclude?
# if a subclass doesnt have its own constructor it will call its superclass constructor and
# if it has its own constructor it will call it.
# but what if we want to call both the constructor ?
# we can use the "super" function
