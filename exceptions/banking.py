

class BankAccount():

  def __init__(self):
    self.balance = 0

  def add_money(self, amount):
    """Add money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will increase
    """
    try:
        if amount >= 1:
            self.balance += amount
            print("Your deposit was successful")
            return self.balance
        else:
            raise ArithmeticError("Amount needs to be a positive number")

    except TypeError:
        print('(Error): The add_money method requires a numeric value')
        raise
    except ArithmeticError as err:
        print(f"Your deposit was not successful. Error: {err}")
        raise

my_account = BankAccount()
my_account.add_money(1)
