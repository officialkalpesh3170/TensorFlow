class Atm:
    #function vs method
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()

    def menu(self):
        user_input = input("Welcome to the ATM! Please enter your pin: ")
        if user_input == self.pin:
            print("Access granted.")
            self.account_menu()
        else:
            print("Incorrect pin. Please try again.")
            self.menu()