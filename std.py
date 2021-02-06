class Student:
    def __init__(self,name,rno,phno):
        self.name=name
        self.rno=rno
        self.phonenumber=phno
    def display(self):
        print(self.name,self.rno,self.phonenumber)
std=Student("sai",289,88888888)
std.display()

