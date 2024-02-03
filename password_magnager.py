from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)

def view():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_passw = fer.decrypt(passw.encode()).decode('utf-8')
            print(f"User: {user} | Password: {decrypted_passw}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open ("passwords.txt", "a") as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode('utf-8')
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Do you want to add a new password or retrieve an existing one? (view/add), press q to quit: ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")