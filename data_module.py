
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
import time

def typewrite(text): 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()


# DATA OVERVIEW
def display_dataset_preview():

    typewrite("\n=== Student Survey: Gaming and English Performance ===")
    print(dataset_df)



# ANALYSIS FUNCTIONS
def display_visualisation():

    typewrite("\n=== Research Analysis Menu ===")
    print("1. Distribution of Gaming Hours")
    print("2. English Improvement Trends")
    print("3. Perceived Impact on Academic Results")
    print("4. Relationship: Gaming Hours vs English Improvement")
    print("5. In-depth: Students reporting gaming impact")

    choice = input("\nSelect analysis option (1-5): ")

    
    if choice == '1':

        data = dataset_df['Gaming Hours'].value_counts()
        
        print("\nDistribution of Gaming Hours:")
        print(data)

        data.plot(kind='bar')
        plt.title("Distribution of Weekly Gaming Hours")
        plt.xlabel("Hours")
        plt.ylabel("Number of Students")
        plt.show()


    #
    elif choice == '2':

        data = dataset_df['English Improvement'].value_counts()

        print("\nEnglish Improvement Trends:")
        print(data)

        data.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Reported English Improvement Levels")
        plt.ylabel("")
        plt.show()


    
    elif choice == '3':

        data = dataset_df['Perceived Impact on Grades'].value_counts()

        print("\nPerceived Academic Impact:")
        print(data)

        data.plot(kind='bar')
        plt.title("Student Perception of Gaming Impact on Grades")
        plt.xlabel("Response")
        plt.ylabel("Number of Students")
        plt.show()


    
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

#Search dataset for keywords
def search_data():

    keyword = input("Enter keyword to search dataset: ")
    

    results = dataset_df[
        dataset_df.astype(str).apply(
            lambda row: row.str.contains(keyword, case=False).any(),
            axis=1
        )
    ]

    typewrite("\n=== Search Results ===")

    if results.empty:
        print("No matching responses found.")
    else:
        print(results)



#Summary of dataset statistics
def data_summary():

    print("\n=== Data Summary ===")
    print(dataset_df.describe(include='all'))



#COnclusions based on data analysis
def display_research_conclusion():

    typewrite("\n=== Research Conclusion ===")
    print(" - Most participants who played games for 8+ hours reported either no improvement or that they performed slightly worse academically.")
    print(" - Only a small number of students who played for 8+ hours reported significant improvement, suggesting very long gaming hours may negatively affect school performance for many students.")
    print(" - Students who played for 1–2 hours were more likely to report slight or significant improvement compared to heavy gamers.")
    print(" - Moderate gaming times (2–4 hours) showed mixed results, with some students improving and others performing worse.")
    print(" - Very low gaming time (less than 1 hour) mostly resulted in slight improvement, although a few students still performed worse.")
    print(" - The majority of responses across all groups showed only slight changes in performance rather than major improvements or declines.")
    print(" - Students who answered “Yes” to being affected by gaming appeared more often in groups with higher gaming hours, suggesting heavy gaming may have a stronger impact on academic performance.")
    print(" - Overall, the data suggests that excessive gaming is linked to lower academic improvement, while moderate or limited gaming may have less negative impact.")
    print("\nHowever, this may be correlation and not causation, and other factors could influence both gaming habits and academic performance.")
    print("Further research with larger sample sizes and controlled variables would be needed to draw stronger conclusions about the relationship between gaming and English performance.")