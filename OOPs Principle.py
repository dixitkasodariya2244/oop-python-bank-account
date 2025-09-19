from abc import ABC, abstractmethod

# ------------------------------
# Abstraction
# ------------------------------
# Abstract base class representing a generic bank account.
# This enforces a contract that all account types must follow.
class BankAccount(ABC):
    def __init__(self, owner: str, balance: float = 0.0):
        # Encapsulation: attributes are prefixed with _ to indicate "protected"
        self._owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        """Public read-only access to account balance"""
        return self._balance

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit money into the account"""
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account"""
        pass

    def __str__(self) -> str:
        return f"{self._owner}'s account | Balance: {self._balance:.2f}"


# ------------------------------
# Inheritance & Encapsulation
# ------------------------------
# SavingsAccount inherits from BankAccount and adds specific behavior.
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds in savings account")
        self._balance -= amount

    def apply_interest(self) -> None:
        """Adds interest to the balance"""
        self._balance += self._balance * self._interest_rate


# ------------------------------
# Another Derived Class
# ------------------------------
# CurrentAccount demonstrates polymorphism by implementing same methods differently.
class CurrentAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance + self._overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount


# ------------------------------
# Example Usage (Polymorphism in action)
# ------------------------------
if __name__ == "__main__":
    # Create different account types
    savings = SavingsAccount("Alice", 1000.0)
    current = CurrentAccount("Bob", 500.0)

    # Deposit money
    savings.deposit(200)
    current.deposit(300)

    # Withdraw money
    savings.withdraw(100)
    current.withdraw(700)  # allowed due to overdraft

    # Apply interest to savings
    savings.apply_interest()

    # Polymorphic behavior: both accounts respond to same methods differently
    accounts = [savings, current]
    for acc in accounts:
        print(acc)
