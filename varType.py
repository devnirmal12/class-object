class Car:

    wheel = 4  #class variable

    def __init__(self):
        self.com = 'BMW'     #instance variables
        self.mil = 10

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheel = 5
   
print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil, c2.wheel)