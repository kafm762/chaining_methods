class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.user_balance = 0

    def make_deposit(self,amount):
        self.user_balance += amount
        return self 

    def make_withdrawal(self,amount):
        self.user_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} ----- Balance: {self.user_balance}")
        return self 
        

    def transfer_money(self,other_user,amount):
        self.user_balance -= amount 
        other_user.user_balance += amount 
        self.display_user_balance()
        other_user.display_user_balance()


maria = User("Maria Mateo", "mariam2@gmail.com")
eva = User("Eva Mateo", "evam7@gmail.com")
diego = User("Diego Mateo", "diegom16@gmail.com")

maria.make_deposit(100).make_deposit(20).make_deposit(20).make_withdrawal(20).display_user_balance()


eva.make_deposit(100).make_deposit(50).make_withdrawal(10).make_withdrawal(50).display_user_balance()

diego.make_deposit(300).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

diego.transfer_money(eva,100)