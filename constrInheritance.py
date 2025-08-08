class A:

    def __init__(self):
        print("init for class A")

    def feature1(self):
        print("It has feature 1")

    def feature2(self):
        print("It has feature 2")

class B:

    def __init__(self):
        super().__init__()
        print("init for class B")

    def feature3(self):
        print("It has feature 3")

    def feature4(self):
        print("It has feature 4")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("init for class C")
    
c = C()

print(c)
