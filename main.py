
from data_module import (
    display_dataset_preview,
    display_visualisation,
    search_data,
    data_summary,
    display_research_conclusion
)


import time

def typewrite(text): 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()

name = input('Hello user, please enter your name: ')

typewrite("╔══════════════════════════════════════════════════════════════╗")
typewrite("║  Welcome " + name + " to English performance data            ║") 
typewrite("║  Look through various datasets and visualisations.           ║")    
typewrite("║  To gain insights into the performance of English students   ║")         
typewrite("║  And how gaming impacts their performance.                   ║")                                           
typewrite("╚══════════════════════════════════════════════════════════════╝")                                                                                   

def main_menu():
    while True:

        typewrite("╔═══════════════════════════════════════╗")
        typewrite("║    Data Viewer Interface              ║")
        typewrite("║                                       ║")
        typewrite("║   1. View dataset                     ║")
        typewrite("║   2. View visualisation               ║")
        typewrite("║   3. Search or filter data            ║")
        typewrite("║   4. Data Summary                     ║")
        typewrite("║   5. Research conclusion              ║")
        typewrite("║   6. Exit                             ║")
        typewrite("╚═══════════════════════════════════════╝")
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            display_dataset_preview()

        elif choice == '2':
            display_visualisation()

        elif choice == '3':
            search_data()

        elif choice == '4':
            data_summary()

        elif choice == '5':
            display_research_conclusion()

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid selection")


if __name__ == "__main__":
    main_menu()