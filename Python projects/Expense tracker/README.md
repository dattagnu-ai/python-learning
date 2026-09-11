# 💰 Expense Tracker

A command-line Expense Tracker application built with Python.

This project allows users to manage their daily expenses through a simple
menu-driven interface. Expense data is stored in a JSON file, allowing the
data to persist even after the application is closed.

---

## 📌 About the Project

The Expense Tracker was developed as a Python learning project to practice
Object-Oriented Programming, exception handling, file handling, JSON
serialization/deserialization, and Git/GitHub workflow.

The application started as an in-memory expense tracker and was improved
with JSON-based data persistence.

---

## ✨ Features

- ➕ Add new expenses
- 👀 View all expenses
- 🔍 Search expenses by category or description
- 💰 Calculate total expenses
- 🗑️ Delete expenses
- 💾 Automatically save expenses to a JSON file
- 📂 Automatically load saved expenses when the application starts
- 📅 Automatically use the current date when no date is entered
- ⚠️ Handle invalid menu input
- ⚠️ Handle invalid delete input
- 🧹 Handle empty search input
- 📊 Display expenses in a formatted table
- 🔄 Convert Python objects to dictionaries for JSON storage
- 🔄 Convert JSON data back into Python objects

---

## 🛠️ Technologies Used

- **Python 3**
- **Object-Oriented Programming (OOP)**
- **JSON**
- **File Handling**
- **Exception Handling**
- **datetime**
- **os**
- **Git**
- **GitHub**

---

## 📂 Project Structure

```text
Python projects/
│
├── expense_tracker.py
├── expense.txt
├── Expense_tracker.json
└── README.md