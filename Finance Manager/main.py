from user_auth import login, register
from finance_manager import FinanceManager
from storage import load_data

def main():
    data = load_data()

    login_or_register = input('Login atau Register: ').lower()
    match login_or_register:
        case 'login':
            user, user_data = login(data)
        case 'register':
            register(data)
        case _:
            raise ValueError('Username atau password salah.')

    manager = FinanceManager(user, data)

    while True:
        menu_list = ("Adding Transaction", "View Transaction","Edit transaction list","Erase Transaction", "View Balance", "exit prgram")
        for i, m in enumerate(menu_list, start=1):
            print(f"{i}. {m}")

        choice = input("Input the number based on the list above: ")

        match choice:
            case "1":
                manager.add_transaction()
            case "2":
                manager.view_transactions()
            case "3":
                manager.edit_transaction()
            case "4":
                manager.delete_transaction()
            case "5":
                manager.get_balance()
            case "6":
                print("Exiting Program...")
                break
            case _:
                print("Input is not Valid")

if __name__ == "__main__":
    main()