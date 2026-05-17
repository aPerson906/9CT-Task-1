
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
dataset_df = pd.read_csv(
    'Data/English improvements.csv',
    header=None,
    names=[
        'Gaming Hours',
        'English Improvement',
        'Perceived Impact on Grades'
    ]
)


# =========================
# DATA OVERVIEW
# =========================
def display_dataset_preview():

    print("\n=== Student Survey: Gaming and English Performance ===")
    print(dataset_df)


# =========================
# ANALYSIS FUNCTIONS
# =========================
def display_visualisation():

    print("\n=== Research Analysis Menu ===")
    print("1. Distribution of Gaming Hours")
    print("2. English Improvement Trends")
    print("3. Perceived Impact on Academic Results")
    print("4. Relationship: Gaming Hours vs English Improvement")
    print("5. In-depth: Students reporting gaming impact")

    choice = input("\nSelect analysis option (1-5): ")

    # 1. gaming hours distribution
    if choice == '1':

        data = dataset_df['Gaming Hours'].value_counts()
        
        print("\nDistribution of Gaming Hours:")
        print(data)

        data.plot(kind='bar')
        plt.title("Distribution of Weekly Gaming Hours")
        plt.xlabel("Hours")
        plt.ylabel("Number of Students")
        plt.show()


    # 2. english improvement trends
    elif choice == '2':

        data = dataset_df['English Improvement'].value_counts()

        print("\nEnglish Improvement Trends:")
        print(data)

        data.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Reported English Improvement Levels")
        plt.ylabel("")
        plt.show()


    # 3. perceived impact
    elif choice == '3':

        data = dataset_df['Perceived Impact on Grades'].value_counts()

        print("\nPerceived Academic Impact:")
        print(data)

        data.plot(kind='bar')
        plt.title("Student Perception of Gaming Impact on Grades")
        plt.xlabel("Response")
        plt.ylabel("Number of Students")
        plt.show()


    # 4. relationship analysis
    elif choice == '4':

        cross = pd.crosstab(
            dataset_df['Gaming Hours'],
            dataset_df['English Improvement']
        )

        print("\nRelationship Between Gaming Hours and English Improvement:")
        print(cross)

        cross.plot(kind='bar')
        plt.title("Gaming Hours vs English Improvement")
        plt.xlabel("Gaming Hours")
        plt.ylabel("Number of Students")
        plt.show()


    # 5. deeper insight
    elif choice == '5':

        impacted = dataset_df[
            dataset_df['Perceived Impact on Grades'].str.lower() == 'yes'
        ]

        print("\n=== Students Reporting Gaming Has Impacted Grades ===")
        print(impacted)

        print("\nTotal Students Reporting Impact:", len(impacted))

        print("\nGaming Hours Breakdown:")
        print(impacted['Gaming Hours'].value_counts())

        print("\nEnglish Improvement Breakdown:")
        print(impacted['English Improvement'].value_counts())


    else:
        print("Invalid selection")


# =========================
# SEARCH DATA
# =========================
def search_data():

    keyword = input("Enter keyword to search dataset: ")

    results = dataset_df[
        dataset_df.astype(str).apply(
            lambda row: row.str.contains(keyword, case=False).any(),
            axis=1
        )
    ]

    print("\n=== Search Results ===")

    if results.empty:
        print("No matching responses found.")
    else:
        print(results)

