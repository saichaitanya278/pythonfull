class Cat:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def info(self):
        print(f"this is cat and my name is { self.name}. IAm {self.age} years old")
    def make_sound(self):
        print("neow")
class Dog:
    def __init__(self,name,age):
            self.name=name
            self.age=age
    def info(self):
            print(f"this is cat and my name is {self.name}. IAm {self.age} years old")
    def make_sound(self):
            print("woof")
cat1 =Cat("lully",2.5)
dog1=Dog("tommy",3)

for animal in (cat1,dog1):
            animal.info()
            animal.make_sound()