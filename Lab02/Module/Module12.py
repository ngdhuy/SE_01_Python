from datetime import datetime


def load_file(file_name):
    journal = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                lst = line.split('|')
                lst[2] = lst[2].split('\n')[0]
                item = {"datetime": lst[0], "username": lst[1], "content": lst[2]}
                journal.append(item)
    except:
        print(f"Cannot access (Read) file: {file_name}")
    finally:
        file.close()
    return journal


def save_file(file_name, journal):
    try:
        with open(file_name, "w") as file:
            for item in journal:
                string = item["datetime"] + "|" + item["username"] + "|" + item["content"] + "\n"
                file.write(string)
        print("Data is storage")
    except:
        print(f"Cannot access (Write) file: {file_name}")
    finally:
        file.close()


def input_item():
    item = {"datetime": str(datetime.now()), "username": input("Enter username: "), "content": input("Enter content: ")}
    print("=> Journal entry is storage")
    return item


def print_journal(journal):
    print("-" * 160)
    print("| {:<30} | {:<20} | {:<100} |".format('Datetime', 'User name', 'Content'))
    print("|", "-" * 30, "|", "-" * 20, "|", "-" * 100, "|")
    for item in journal:
        print("| {:<30} | {:<20} | {:<100} |".format(item['datetime'], item['username'], item['content']))
    print("-" * 160)


def print_menu():
    print("----- MENU -----")
    print("\t 1. Print list of journal entry")
    print("\t 2. Add new entry")
    print("\t 0. Exit")
    flag_chose = int(input("=> Chose: "))
    return flag_chose
