class Computer:

    #constructor
    def __init__(self, cpu, ram):
        self.cpu = cpu;
        self.ram = ram;
    
    def config(self):
        print (self.ram)
        print (self.cpu)

computer1 = Computer("i5", 8)
computer1.config() 