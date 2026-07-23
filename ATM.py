import json
class Atm:
    def __init__(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        self.pin = data["pin"]
        self.balance = data["balance"]
        self.menu()
    def menu(self):
        while True:
            user_input=input("""
                            How can i help you?
                            Press 1 to create pin
                            Press 2 to change pin
                            Press 3 to check balance
                            Press 4 to withdraw
                            Press 5 to 
                            Press anything else to exit""")
            if user_input == '1':
                self.create_pin()
                #create pin
            elif user_input=='2':
                self.change_pin()
                #change pin
            elif user_input=='3':
                self.check_balance()

                #check balance
            elif user_input=='4':
                self.withdraw()#withdraw 
            elif user_input == '5':
                self.deposit()

            else:
                break
            


    def create_pin(self):
        user_pin = int(input(" Please set a pin : "))
        self.pin = user_pin
        print("Thanks, your pin has been updated")
        self.save_data()
        user_balance = int(input("Please enter the deposit amount : "))
        if user_balance > 0:
            self.balance = user_balance
            print("Thanks, your pin has been updated")
            self.save_data()
        else:
            print("Invalid Amount")
        
        
        
    
    def change_pin (self):
        old_pin = int(input("enter your old pin : "))
        if old_pin == self.pin:
            new_pin = int(input("enter a new pin : "))
            self.pin = new_pin
            print("pin change successful")
            self.save_data()
            
        else:
            print("Enter the correct old pin : ")

    def check_balance(self):
        pin_check = int(input(" Enter your ATM pin: "))

        if pin_check == self.pin:
            print("Your Balance is", self.balance)
        else:
            print("Wrong pin, can't display balance")

    def withdraw(self):
        pin_check = int(input("Enter your ATM pin: "))
        
        if pin_check == self.pin:
            withdraw_amt = int(input("Enter the amount to withdraw : "))
            if withdraw_amt <= self.balance and withdraw_amt>0:
                self.balance = self.balance - withdraw_amt
                print ("Withdrawl of" , withdraw_amt , "is successful ")
                self.save_data()
            else:
                print("Poor you dont have this much in your account")
        else:
            print("Wrong pin , can't display balance")
    def deposit(self):
        pin_check = int(input("Enter your ATM pin: "))
                
        if pin_check == self.pin:
            dep_amount = int(input("Enter the amount you want to deposit : "))
            if dep_amount > 0:
                self.balance = self.balance + dep_amount
                print("deposit of" , dep_amount , "succesful")
                print(self.balance)
                self.save_data()
        else:
            print("Wrong pin")
    def save_data(self):
        data = {
            "pin": self.pin,
            "balance": self.balance
        }
        with open("data.json","w") as file:
            json.dump(data,file)
            
    


if __name__ == "__main__":
    obj = Atm()