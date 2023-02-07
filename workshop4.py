

#Task1
#declare class and def with class instance attributes

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

        
#Task2
    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password  


#Task3 
class BankUser(User):

    def __init__(self, name, pin, password, balance):
        super().__init__(name, pin, password)

        self.balance = balance

#Task4
    def show_balance(self):
        
        print(self.name,"has an account balance of: ", float(self.balance))

    
    def withdraw(self, amount):
        #amount = float(input("Withdraw amount: "))
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough money!")
       
      

    def deposite(self, amount):
        #amount = float(input("Deposite amount: "))
        self.balance += amount
        
       

       
#Task5 create Transfer and request money

    def transfer_money(self, amount):

        self.balance = self.balance - amount
        #self.amount = self.balance
        print("\n" "You are transfering:", amount, "to Bob")

            
        print("User authentication is required...")

        pin = input("Enter your PIN: ")
        password = input("Enter your Password: ")

        if pin == self.pin and password == self.password:
            print("Transfer authorized")
            
        else:
            print("Invalid PIN. Transaction canceled")
            return False

         
    def request_money(self, amount):

        self.balance = self.balance + amount
        self.amount = self.balance

        print("\n" "You are requesting", amount, "from Bob")
        
        print("User authentication is required...")

        pin = input("Enter your PIN: ")
        password = input("Enter your Password: ")

        if pin == self.pin and password == self.password:
            print("Request authorized")   
            
        else:
            print("Invalid PIN. Transaction canceled")
            return False

   
# drive code

    """ Drive Code for Task 1 """

""" user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)  """



""" Drive Code for Task 2 """

""" change_name = User("Bobby", 4321, "newpassword")
print(change_name.name, change_name.pin, change_name.password)  """
 
""" Drive Code for Task 3 """

""" BankUser = BankUser("Bob", 1234, "newpassword", 0)
print(BankUser.name, BankUser.pin, BankUser.password, BankUser.balance) """

""" Drive Code for Task 4 """

""" BankUser = BankUser("Bob", 1234, "newpassword", 0)
BankUser.show_balance()
BankUser.deposite(BankUser.balance + 1000)
BankUser.show_balance()
BankUser.withdraw(BankUser.balance - 500)
BankUser.show_balance()  """


""" Drive Code for Task 5 """



second_account = BankUser("Alice", 5678, "alicepassword", 5000)
first_account = BankUser("Bob", 1234, "newpassword", 0)

second_account.show_balance()
first_account.show_balance()
second_account.transfer_money(500)
first_account.deposite(500)
second_account.show_balance()
first_account.show_balance()

second_account.show_balance()
first_account.show_balance()
second_account.request_money(250)
second_account.show_balance()
first_account.withdraw(250)
first_account.show_balance()



 

 