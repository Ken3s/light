# class Light:
#     def output(self):
#         printf("first")
#
# a1 = MyClass()
# a1.name = "Tanaka"
#
# a2 = MyClass()
# a2.name = "Suzuki"
#
# print a1.name                        #=> Tanaka
# print a2.name                        #=> Suzuki
class MainClass:
    x = 128
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x

class SubClass(MainClass):
    def __init__(self):
        self.x = 64
    def display(self):
        print self.x


obj = MainClass()
print obj.getX()
obj.setX(256)
print obj.getX()


obj = SubClass()
print obj.getX()
obj.setX(1024)
obj.display()
