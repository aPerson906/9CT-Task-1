
import pandas as pd
import matplotlib.pyplot as plt

# reads the csv file
dataset_df = pd.read_csv(
    'Data/English improvements.csv',
    header=None,
    names=[
        'Gaming Hours',
        'English Improvement',
        'Gaming Affected Grades'
    ]
)


# shows the dataset
def display_dataset_preview():

    print("\n--- Dataset Preview ---")
    print(dataset_df)


# shows graphs
def display_visualisation():

    print("\n1. Gaming Hours")
    print("2. English Improvement")
    print("3. Gaming Affecting Grades")

    choice = input("Choose a graph (1-3): ")

    # gaming hours graph
    if choice == '1':

        gaming_data = dataset_df['Gaming Hours'].value_counts()

        gaming_data.plot(kind='bar')

        plt.title("Gaming Hours Per Week")
        plt.xlabel("Hours")
        plt.ylabel("Students")
        plt.xticks(rotation=15)

        plt.show()

    # english improvement graph
    elif choice == '2':

        improvement_data = dataset_df['English Improvement'].value_counts()

        improvement_data.plot(kind='pie', autopct='%1.1f%%')

        plt.title("English Improvement")
        plt.ylabel("")

        plt.show()

    # grades graph
    elif choice == '3':

        grades_data = dataset_df['Gaming Affected Grades'].value_counts()

        grades_data.plot(kind='bar')

        plt.title("Gaming Affecting Grades")
        plt.xlabel("Answer")
        plt.ylabel("Students")

        plt.show()

    else:
        print("Invalid option")


# searches data
def search_data():

    search = input("Search the dataset: ")

    results = dataset_df[
        dataset_df.astype(str).apply(
            lambda row: row.str.contains(search, case=False).any(),
            axis=1
        )
    ]

    print("\n--- Results ---")

    if results.empty:
        print("No results found")

    else:
        print(results)


# updates information
def update_data_entry():

    global dataset_df

    try:

        row = int(input("Enter row number: "))

        print("\nColumns:")
        for column in dataset_df.columns:
            print(column)

        column_name = input("Enter column name: ")

        if column_name not in dataset_df.columns:
            print("Column not found")
            return

        new_value = input("Enter new value: ")

        dataset_df.at[row, column_name] = new_value

        print("Data updated")

    except:
        print("Error updating data")


# saves changes
def save_changes():

    dataset_df.to_csv(
        'Data/English improvements.csv',
        index=False,
        header=False
    )

    print("Changes saved")
