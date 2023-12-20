class Customer:
    def __init__(self, membershipType):
        # we will make self.name private.
        self.__name = "Default Name"
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


customer1 = Customer("Premimum")
customer1.printAll()
customer1.setName("John")
customer1.updateMembership("Gold")
customer1.printAll()

print()

customer2 = Customer("Silver")
customer2.setName("Tom")
customer2.printAll()
