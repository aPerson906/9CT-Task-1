
from data_module import (
    display_dataset_preview,
    display_visualisation,
    search_data,
    update_data_entry,
    save_changes
)


import time

def typewrite(text): 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()


typewrite("╔══════════════════════════════════════════════╗")
typewrite("║ Welcome to English improvements                      ")
typewrite("║                                                ")
typewrite("║                                                ")
typewrite("║                                                    ")

def main_menu():

    while True:

        typewrite("╔═════════════════════════════════════╗")
        typewrite("║    Data Viewer Interface            ║")
        typewrite("║                                     ║")
        typewrite("║   1. View dataset                   ║")
        typewrite("║   2. View visualisation             ║")
        typewrite("║   3. Search or filter data          ║")
        typewrite("║   4. Update a data entry            ║")
        typewrite("║   5. Save changes                   ║")
        typewrite("║   6. Exit                           ║")
        typewrite("╚═════════════════════════════════════╝")
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            display_dataset_preview()

        elif choice == '2':
            display_visualisation()

        elif choice == '3':
            search_data()

        elif choice == '4':
            update_data_entry()

        elif choice == '5':
            save_changes()

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid selection")


if __name__ == "__main__":
    main_menu()