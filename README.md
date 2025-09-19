# OOP Python Example – Bank Account System

This project demonstrates **Object-Oriented Programming (OOP)** principles in Python using a simple **Bank Account system**.  
It covers the four major OOP concepts: **Encapsulation, Inheritance, Polymorphism, and Abstraction**.

---

## 📌 Features
- **Encapsulation** → Account details (balance, owner) are protected with controlled access.  
- **Inheritance** → `SavingsAccount` and `CurrentAccount` extend the base `BankAccount` class.  
- **Polymorphism** → Both account types implement `withdraw` differently (interest rules vs overdraft rules).  
- **Abstraction** → `BankAccount` is an abstract class enforcing a common interface for all account types.  

---

## 🏦 Example Classes
- `BankAccount` → Abstract base class (cannot be instantiated directly).  
- `SavingsAccount` → Allows deposits, withdrawals, and applies interest.  
- `CurrentAccount` → Allows overdraft up to a set limit.  

---

## ▶️ How It Works
1. Create accounts:
   ```python
   savings = SavingsAccount("Alice", 1000.0)
   current = CurrentAccount("Bob", 500.0)
2. Perform deposits and withdrawals:
   ```python
   savings.deposit(200)
   current.withdraw(700)   # allowed with overdraft
3. Apply interest to savings:
   ```python
   savings.apply_interest()
4. Print account details:
   ```python
   print(savings)   # Alice's account | Balance: ...
   print(current)   # Bob's account | Balance: ..

