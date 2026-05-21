import pandas as pd
import matplotlib.pyplot as plt
import time

def back():
    while True:
        choice = input("Go back to main menu? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Ok, take your time")
            continue


def typewrite(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()


def display_dataset_preview():
    print()
    typewrite("Student Gaming Survey Data")
    print()
    print(dataset_df)

dataset_df = pd.read_csv(
    'Data/English improvements.csv',
    header=None,
    names=['Gaming Hours', 'English Improvement', 'Perceived Impact on Grades']
)


def display_visualisation():
    print()
    print("1. Does gaming affect grades")
    print("2. Heavy gamers english results")
    print("3. Gaming hours vs english")
    print("4. Overall english results")
    print("5. Most common gaming hours")
    print()
    choice = input("pick option: ")

    if choice == '1':
        data = pd.crosstab(
            dataset_df['Gaming Hours'],
            dataset_df['Perceived Impact on Grades']
        )
        print()
        print(data)
        data.plot(kind='bar', stacked=True)
        plt.title("Does Gaming Affect Grades")
        plt.xlabel("Gaming Hours")
        plt.xticks(rotation=45)
        plt.ylabel("Students")
        plt.show()
        

    elif choice == '2':
        heavy = dataset_df[
            dataset_df['Gaming Hours'].str.contains('8')
        ]
        data = heavy['English Improvement'].value_counts()
        print()
        print(data)
        data.plot(kind='bar')
        plt.title("Heavy Gamers English Results (8+ hours)")
        plt.xlabel("English Result")
        plt.xticks(rotation=20)
        plt.ylabel("Students")
        plt.show()

    elif choice == '3':

        cross = pd.crosstab(
            dataset_df['Gaming Hours'],
            dataset_df['English Improvement']
        )
        print()
        print(cross)
        cross.plot(kind='bar', stacked=True)
        plt.title("Gaming Hours vs English")
        plt.xlabel("Gaming Hours")
        plt.xticks(rotation=45)
        plt.ylabel("Students")
        plt.show()

    elif choice == '4':
        results = dataset_df['English Improvement'].value_counts()
        print()
        print(results)
        results.plot(kind='pie', autopct='%1.1f%%')
        plt.title("English Results")
        plt.ylabel("")
        plt.show()

    elif choice == '5':
        game = dataset_df['Gaming Hours'].value_counts()
        print()
        print(game)
        game.plot(kind='bar')
        plt.title("Most Common Gaming Hours")
        plt.xlabel("Hours")
        plt.xticks(rotation=45)
        plt.ylabel("Amount")
        plt.show()
    else:
        print("wrong option")

def search_data():
    print()
    keyword = input("Search word: ")
    results = dataset_df[
        dataset_df.astype(str).apply(
            lambda row: row.str.contains(keyword, case=False).any(),
            axis=1
        )
    ]
    print()
    if results.empty:
        print("Nothing found")
    else:
        print(results)

def data_summary():
    print()
    print(dataset_df.describe(include='all'))

def display_research_conclusion():
    print()
    print("Conclusion")
    print()
    print("- Students gaming for over 8 hours mostly had worse or no improvement.")
    print("- Students gaming 1-2 hours usually had slight improvement.")
    print("- 2-4 hour gamers had mixed results.")
    print("- Gaming for more than 8 hours seems to affect grades more.")
    print("- Most students only showed small changes in English.")
    print("- There is a correlation with grades affecting gaming but this does not mean there is causation.")
    print("- For a more clear answer a bigger survey group would be needed, to find the impaction of gaming on English grades.")

