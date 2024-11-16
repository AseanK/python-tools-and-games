class Player:
    def __init__(self, initial_balance=None):
        if initial_balance is not None:
            self.balance = initial_balance
        else:
            self.balance = self.set_initial_balance()

    @staticmethod
    def set_initial_balance():
        while True:
            initial_balance = input('Your initial balance: $')
            if initial_balance.isdigit():
                initial_balance = int(initial_balance)
                if initial_balance > 0:
                    return initial_balance
                else:
                    print('Your balance must be greater than 0.')
            else:
                print('Enter numbers greater than 0.')

    def set_bet(self):
        while True:
            bet = input('How much would you like to bet?  $')
            if bet.isdigit():
                bet = int(bet)
                if 0 < bet <= self.balance:
                    return bet
                else:
                    print(f'Set your bet between 0 and {self.balance}')
            else:
                print('Enter numbers greater than 0.')

    def get_current_balance(self, dividend):
        self.balance += dividend


    @staticmethod
    def ask_continue():
        while True:
            continue_choice = input("Do you want to continue (y/n)? ").lower()
            if continue_choice == 'y':
                return True
            elif continue_choice == 'n':
                return False
            else:
                print("Please enter y or n")
