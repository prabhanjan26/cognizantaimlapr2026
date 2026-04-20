# Banking Management System

## 📌 Overview

The **Banking Management System** is a console-based banking application developed using **Object-Oriented Programming (OOP)** principles in **Python**.  
The project demonstrates clean architecture, inheritance, encapsulation, aggregation, association, and separation of concerns.

The system allows:
- Customer registration (Individual & Corporate)
- Account management (Savings & Current)
- Secure login/logout
- Transaction processing
- CLI-based user interaction

This project is designed for **educational and architectural clarity**, not persistent storage or production deployment.

---

## 🏗️ Architecture Overview

The system follows a **layered architecture**:

main.py
   ↓
Menu (Controller / CLI)
   ↓
Business Domain
(Customer, Account, Transaction)
   ↓
Utilities (Validation & Helpers)
