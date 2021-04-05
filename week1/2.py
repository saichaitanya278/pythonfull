class User():
    def __init__(self, name, age, gender, accno):
        self.name = name
        self.age = age
        self.gender = gender
        self.accno = accno

    def ShowDetails(self):
        print(
            f"Account details\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nAccount No: {self.accno}"
        )


class Bank(User):
    def __init__(self, name, age, gender, accno):
        super().__init__(name, age, gender, accno)
        self.balance = 0

    def deposite(self, amount):
        self.amount = amount
        self.balance += amount

        print(f"Updated balance is: {self.balance}")

    def withdraw(self, amount):
        self.amount = amount

        if (self.amount > self.balance):
            print("Insufficente amount")
        else:
            print(
                f"{self.amount} is debited from your account ACCNo:{self.accno} and your Balance is {self.balance-self.amount}")
            self.balance -= self.amount

    def Viewbalance(self):
        print(f"Your current balance is {self.balance}")


class MobileBankAccount(User):
    def __init__(self, name, age, gender, accno):
        super().__init__(name, age, gender, accno)
        self.balance = 0

    def deposite(self, amount):
        self.amount = amount
        self.balance += amount

        print(f"Updated balance is: {self.balance}")

    def withdraw(self, amount):
        self.amount = amount

        if (self.amount > self.balance):
            print("Insufficente amount")
        else:
            print(
                f"{self.amount} is debited from your account ACCNo:{self.accno} and your Balance is {self.balance-self.amount}")
            self.balance -= self.amount

    def Viewbalance(self):
        print(f"Your current balance is {self.balance}")


class InternetBankAccount(User):
    def __init__(self, name, age, gender, accno):
        super().__init__(name, age, gender, accno)
        self.balance = 0

    def deposite(self, amount):
        self.amount = amount
        self.balance += amount

        print(f"Updated balance is: {self.balance}")

    def withdraw(self, amount):
        self.amount = amount

        if (self.amount > self.balance):
            print("Insufficente amount")
        else:
            print(
                f"{self.amount} is debited from your account ACCNo:{self.accno} and your Balance is {self.balance-self.amount}")
            self.balance -= self.amount

    def Viewbalance(self):
        print(f"Your current balance is {self.balance}")


user = Bank("amit", 34, 'M', 1234567123)
user.deposite(1234)
user.withdraw(123)
user.Viewbalance()


user = MobileBankAccount("amit", 34, 'M', 1234567123)
user.deposite(1234)
user.withdraw(123)
user.Viewbalance()


user = InternetBankAccount("amit", 34, 'M', 1234567123)
user.deposite(1234)
user.withdraw(123)
user.Viewbalance()
