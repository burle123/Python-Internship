# User defined exception 
# raise - used to raise an exception explicitly in the code

# InsufficientFundsError is a custom exception that inherits from the built-in Exception class

class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in the account."):
        self.message = message
        super().__init__(self.message)

    def withdraw(self, amount):
        balance = 1000  # Assuming the account balance is 1000
        if amount > balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount}. {self.message}")
        else:
            print(f"Withdrew {amount} successfully.")

        balance -= amount
        print(f"Remaining balance: {balance}")    
# Example usage
account = InsufficientFundsError()
try:
    account.withdraw(200)  # Attempting to withdraw more than the balance  
except InsufficientFundsError as e:
    print(e)
finally:
    print("Transaction complete.")
