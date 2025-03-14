from storage import save_data, load_data

def login(data):
    username = input('Username: ')
    password = input('Password: ')

    if username in data and data[username]['password'] == password:
        print(f'Login Success, welcome {username}')
        return username, data[username]
    else:
        raise ValueError('login failed, username/password is incorrect or not registered')

def register(data):
    username = input('Username: ')
    password1 = input('Password: ')
    password2 = input('Confirm Password: ')

    if password1 == password2 and username not in data:
        data[username] = {"name": username, "password": password1, "transactions": []}
        save_data(data)
        exit("Account has been registered")
    else:
        raise Exception('username/password did not match or have been registered')