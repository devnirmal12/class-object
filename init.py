class Computer:

    def __init__(self):
        self.name = 'Dev'
        self.age = 21

    def update(self):
        self.age = 25

    def compare(self, other):
         if self.age == other.age:
             return True
         else:
            return False

c1 = Computer()
c1.update()
c2 = Computer()

if c1.compare(c2):
    print("They are same!")
else:
    print("They are different!")

print(c1.name)
print(c2.name)