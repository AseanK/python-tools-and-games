class Player:
    """
    Player class manages the player behavior.
    - Set an initial balance
    - Set a bet amount
    - Update player's balance
    - Decide whether to continue the game or not
    """
    def __init__(self, initial_balance=None):
        """
        Initialise the new player with the given initial balance.

        Args:
            initial_balance (int): The initial balance for the new player.
        """
        if initial_balance is not None:
            self.balance = initial_balance
        else:
            self.balance = self.set_initial_balance()

    @staticmethod
    def set_initial_balance():
        """
        Prompts the user to input the initial balance.
        The method will ask for input until the user enters a valid balance.

        Returns:
            int: The valid initial balance greater than 0.
        """
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
        """
        Prompts the user to input the bet amount.
        Validates that the bet amount is greater than 0 and less than or equal to the current balance

        Return:
            int: The valid bet amount between 0 and the current balance.
        """
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
        """
        Updates the current balance with the given dividend.

        Args:
            dividend (int): The result is calculated by the role condition.
        """
        self.balance += dividend

    @staticmethod
    def ask_continue():
        """
        Asks the player to continue or exit the game.

        Returns:
            bool: True if the player choose 'y' to continue, otherwise False('n').
        """
        while True:
            continue_choice = input("Do you want to continue (y/n)? ").lower()
            if continue_choice == 'y':
                return True
            elif continue_choice == 'n':
                return False
            else:
                print("Please enter y or n")
