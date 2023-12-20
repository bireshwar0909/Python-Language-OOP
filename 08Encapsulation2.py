class Customer:
    def __init__(self, name, membershipType):
        self.setName(name)
        self.membershipType = membershipType

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # a normal object function
    def updateMembership(self, newMembership):
        self.membershipType = newMembership

    def printAll(self):
        print(self.__name)
        print(self.membershipType)


customer1 = Customer("John", "Premimum")
customer1.printAll()
customer1.updateMembership("Gold")
customer1.printAll()

print()

customer2 = Customer("Tom", "Silver")
customer2.setName("Tommy")  # updating the value of name
print(customer2.getName())  # printing only the name of the customer
customer2.printAll()
