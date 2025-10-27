# Health Management System

import os
import datetime

def gettime():
    return datetime.datetime.now()

clients = {1: "Prince", 2: "Nitish", 3: "Yash"}
os.makedirs("data", exist_ok=True)

def safe_int(prompt, default=None):
    try:
        return int(input(prompt))
    except ValueError:
        return default

def log_data(client_name):
    activity = safe_int("Press 1 to log Exercise or 2 to log Food: ")
    if activity == 1:
        filename = os.path.join("data", f"{client_name}_exercise.txt")
        entry = input("Enter the Exercise: ")
    elif activity == 2:
        filename = os.path.join("data", f"{client_name}_food.txt")
        entry = input("Enter the Food: ")
    else:
        print("Invalid option")
        return
    with open(filename, "a") as f:
        f.write(f"[{gettime()}]: {entry}\n")
    print("Data Logged Successfully")

def retrieve_data(client_name):
    activity = safe_int("Press 1 to retrieve Exercise or 2 to retrieve Food: ")
    if activity == 1:
        filename = os.path.join("data", f"{client_name}_exercise.txt")
    elif activity == 2:
        filename = os.path.join("data", f"{client_name}_food.txt")
    else:
        print("Invalid option")
        return
    try:
        with open(filename, "r") as f:
            print(f"\n---- {client_name.capitalize()}'s {('Exercise' if activity == 1 else 'Food')} Log ----")
            print(f.read())
    except FileNotFoundError:
        print("No data found.")

def main():
    print("Welcome to the Health Management System")
    while True:
        action = safe_int("Press 1 to Log Data, 2 to Retrieve Data, 0 to Exit: ", default=-1)
        if action == 0:
            break
        print("Select Client:\n1. Prince\n2. Nitish\n3. Yash")
        client_choice = safe_int("Enter Client Number: ", default=-1)
        client_name = clients.get(client_choice)
        if not client_name:
            print("Invalid Client Selected")
            continue
        if action == 1:
            log_data(client_name)
        elif action == 2:
            retrieve_data(client_name)
        else:
            print("Invalid Action")

if __name__ == "__main__":
    main()
