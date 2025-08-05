class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print("Name:",self.name,",","Rollno:",self.rollno)

    class Laptop:

        def __init__(self, name, cpu, ram):
            self.name = name
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(f"name: {self.name}, cpu: {self.cpu}, ram:{self.ram}")



s1 = Student('Dev', '21CE1157')
s2 = Student('Archana','24CA1024')

lap1 = s1.Laptop('Dell','i5',8)
lap2 = s2.Laptop('Hp','i5',16)

print(lap1.show())