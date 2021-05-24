from Module.Module12 import *


def main():
    file_name = 'Data/database.txt'
    journal = load_file(file_name)

    flag_chose = print_menu()
    while flag_chose != 0:
        if flag_chose == 1:
            print_journal(journal)
        elif flag_chose == 2:
            item = input_item()
            journal.append(item)
        flag_chose = print_menu()
    save_file(file_name, journal)


if __name__ == "__main__":
    main()