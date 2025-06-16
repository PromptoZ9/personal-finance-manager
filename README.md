# 💼 Personal Finance Manager (CLI-Based, Modular Python Project)

A command-line based **Personal Finance Manager** app built with Python.  
Designed to help users track income and expenses, view transaction history, and manage financial data efficiently.

This project focuses on **structured and maintainable code** by implementing **functions and modular file separation**.

---

## 🎯 Features

- 🔐 Login & registration (multi-user system)
- 🧾 Add, edit, and delete transactions
- 📅 Track date, category, description, and amount
- 📊 View transaction history and balance
- 💾 Data saved persistently in `data.json`
- 🧩 Modular structure using multiple `.py` files

---

## 🛠 Tech Stack

- Python 3.x
- Built-in modules only: `json`, `datetime`
- CLI interface (no external packages needed)

---

## 📂 File Structure
```
├── main.py # Main entry point for running the program
├── user_auth.py # Handles login and registration logic
├── transaction.py # Core transaction features (add/edit/delete/view)
├── storage.py # Read/write data to JSON file
├── finance_manager.py # Menu system and user interaction flow
├── data.json # Persistent storage of users and transactions
├── README.md # Documentation (this file)
```

## 🚀 How to Run
1. Clone this repository:
    ```
    git clone https://github.com/PromptoZ9/expense-tracker.git
    cd expense-tracker
    ```
2. Create a dt.json file (if it doesn't exist yet), and add this as empty JSON:
    ```
    {}
    ```
3. Run the app:
   ```
   python main.py
   ```

🧑‍💻 User Flow

Choose Login or Register

Login Success, welcome user
1. Adding Transaction        
2. View Transaction
3. Edit transaction list
4. Erase Transaction
5. View Balance
6. exit prgram

💡 Example Transaction Format
```
{
    "admin1": {
        "name": "admin1",
        "password": "admin1",
        "transaction": [
            {
                "date": "30/06/2025",
                "category": "expense",
                "description": "beli hp",
                "amount": -2000000.0
            },
            {
                "date": "14/03/2025",
                "category": "income",
                "description": "Monthly Salary",
                "amount": 8000000.0
            }
        ]
    }
}
```

📄 License This project is open-source and intended for learning and personal use.

🔗 Author Built with Python by PromptoZ9

