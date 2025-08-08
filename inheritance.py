class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B:
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")


class C(A,B):
    def feature5(self):
        print("This is feature 5")

    def feature6(self):
        print("This is feature 6")

a = A()
b = B()
c = C()

# Covered:
# 1) single level inheritance
# 2) multi-level inheritance
# 3) multiple inheritance



