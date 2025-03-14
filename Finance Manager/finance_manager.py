from transaction import Transaction
from storage import save_data

class FinanceManager:
    def __init__(self, user, data):
        self.user = user
        self.data = data
        self.transactions = data[user]['transactions']

    def add_transaction(self):
        from datetime import datetime
        date = datetime.today().strftime('%d/%m/%Y')
        category = input("Transaction Category(expense/income): ")
        description = input("Transaction Description: ")
        amount = float(input("Amount?(negative for expense, positive for income): "))

        new_transaction = Transaction(date, category, description, amount)
        self.transactions.append(new_transaction)

        save_data(self.data)  
        print("Transaction has been added!")

    def view_transactions(self):
        if not self.transactions:
            print("There are no transaction!")
            return
        print("\n Transaction List: ")
        print("=" * 50)
        for i, trans in enumerate(self.transactions, start=1):
            print(f"{i}. [{trans.date}] {trans.category} - {trans.description}: Rp{trans.amount}")
        print("=" * 50)

    def delete_transaction(self):
        self.view_transactions()
        try:
            trans_index = int(input("Input the number of the transaction you want to delete (0 to cancel): ")) - 1
            if trans_index == -1:
                return

            deleted_t = self.transactions.pop(trans_index)
            save_data(self.data)  
            print(f"Transaction on'{deleted_t.description}' has been deleted")
            self.view_transactions()
        except (IndexError, ValueError):
            print("The number input is not valid!")

    def edit_transaction(self):
        from datetime import datetime
        self.view_transactions()
        try:
            trans_index = int(input("Input the number from the transaction list that needs to be edited (0 to cancel): ")) - 1
            if trans_index == -1:
                return
            transaction = self.transactions[trans_index]
            print(f"Edit Transaction: {transaction.to_dict()}")

            field_map = ("date", "category", "description", "amount")
            for i, m in enumerate(field_map, start=1):
                print(f"{i}. {m}")
            
            field_choice = input("Choose the field you want to edit: ")
            match field_choice:
                case "1":
                    #date
                    new_date = input('Enter the new date (DD/MM/YYYY): ')
                    try:
                        formatted_date = datetime.strptime(new_date, "%d/%m/%Y").strftime("%d/%m/%Y")
                        transaction.date = formatted_date
                        save_data(self.data)
                        print("The current transaction has been updated!")
                        self.view_transactions()
                    except ValueError:
                        print("Invalid date format. Please use the format DD/MM/YYYY.")
                case "2":
                    #category
                    new_category = input("Enter the new category(expense/income): ")
                    if new_category not in ["expense", "income"]:
                        raise ValueError("Invalid category format. Please enter 'expense' or 'income'.")
                    elif new_category == transaction.category:
                        transaction.category = new_category
                        save_data(self.data)
                        print("The current transaction has been updated!")
                        self.view_transactions()
                    else: 
                        raise ValueError("Invalid category format. Please enter 'expense' or 'income'.")
                case "3":
                    #description
                    new_description = input("Enter the new description: ")
                    transaction.description = new_description
                    save_data(self.data)
                    print("The current transaction has been updated!")
                    self.view_transactions()    
                case "4":
                    #amount
                    new_amount = float(input("Enter the new amount: "))
                    transaction.amount = new_amount
                    save_data(self.data)
                    print("The current transaction has been updated!")
                    self.view_transactions()
        except (IndexError, ValueError):
            print("Input is not valid!")

    def get_balance(self):
        balance = sum(t.amount for t in self.transactions)
        print(f"Your Balance is: Rp{balance}")