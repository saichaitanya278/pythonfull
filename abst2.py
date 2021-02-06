from abc import ABC,abstractmethod
class X(ABC):
    @abstractmethod
    def hi(self):
        pass
    @abstractmethod
    def hello(self):
        pass
class Y(X):
    def hi(self):
        print("Hello Iam Robot")
class Z(Y):
    def hello(self):
        print("Hello Iam Jamesbond")
z=Z()
z.hi()
z.hello()