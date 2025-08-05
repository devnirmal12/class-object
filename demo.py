class Computer: #it is basically a design

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("config is: ", self.cpu,",", self.ram)


com1 = Computer('i5', '16gb') #it is object/instance of the design
com2 = Computer('Ryzen', 8)
com3 = Computer('i7','16gb')

Computer.config(com1)
Computer.config(com2)
com3.config()

#init: runs automatically for respective objects whenever a new object is created.