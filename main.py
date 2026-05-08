
def main_menu():
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. View dataset")
        print("2. View visualisation")
        print("3. Search or filter data")
        print("4. Update a data entry")
        print("5. Save changes")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            print('View dataset')
        elif choice == '2':
            print('View Visualisation')
        elif choice == '3':
            print('Search data')
        elif choice == '4':
            print('Update')
        elif choice == '5':
            print('Save changes')
            print("Changes saved.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")
main_menu()