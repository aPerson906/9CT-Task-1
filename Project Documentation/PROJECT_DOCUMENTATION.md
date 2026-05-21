
# **Assessment Task 1**

## **Phase 1 - Identifying and Defining**

### *Mind map*

![Computing Tech Mind Map](Images/mindmap.png)

### *Purpose*

Hypothesis:
“Students who spend more time gaming are more likely to have lower academic results.”

### *Requirements*

#### *Functional requirements*

The system must allow users to load and view a preloaded .csv dataset about gaming habits and academic performance. Users must be able to search or filter the dataset based on categories such as gaming hours, English improvement, or perceived impact on grades. The system must analyse the relationship between gaming time and academic results to help investigate the hypothesis that students who spend more time gaming are more likely to have lower academic results. It must generate visualisations such as bar charts and pie charts to display trends, comparisons, and patterns in the data. The program must also provide data summaries and research conclusions based on the analysed survey responses and display error messages if the user enters an invalid menu option.

#### *Non-functional requirements*

The system must be user-friendly and easy to navigate through a clear and organised interface. The user interface must include labelled menus, simple instructions, readable text, and consistent formatting so users can easily access the dataset, visualisations, and analysis tools. A README document must be included to explain the purpose of the program, how to run the system, how to use each feature, and how to troubleshoot common issues. The system must also be reliable by detecting errors such as invalid menu selections, missing files, or incorrect data formats and displaying clear error messages to the user. It must ensure data integrity by correctly loading and processing the dataset, preventing crashes during analysis, and ensuring that any data displayed or exported is accurate and consistent with the original dataset.

#### *Use Case*

Actor: User
Goal: To access and interact with existing gaming and English performance data through the program’s interface.
Preconditions:
The .csv dataset has already been preloaded into the system.
The user has access to the program interface.
The system has successfully loaded the dataset without errors.
Main Flow:
The user opens the program and is presented with a text-based menu.
The user selects one of the available options:
 a. View dataset preview
 b. View visualisation (charts and graphs of the dataset)
 c. Search or filter data using keywords
 d. View data summary (statistical overview of the dataset)
 e. View research conclusion (findings based on analysis)
The system performs the selected action.
The system outputs the requested data, analysis, or visualisation to the user.
Postconditions:
The user has successfully viewed or interacted with the dataset.
No changes are made to the dataset unless explicitly handled by a function.
The data remains available for further analysis, searching, and visualisation.

## **Phase 2 - Research and Planning**

### *Research*

There are many studies and articles discussing the relationship between gaming and academic performance. Some research suggests that excessive gaming can negatively affect school performance because students may spend less time studying or sleeping. Other studies argue that moderate gaming can improve skills such as problem-solving, reaction time, and teamwork.
Several news articles and education websites have discussed concerns about students spending long hours gaming, especially late at night, which may reduce concentration and homework completion. However, some students believe gaming helps them relax and reduce stress after school.

Sources:

- [Oxford Internet Institute – Gaming and Well-Being](https://www.oii.ox.ac.uk/news-events/news/video-gaming-can-be-good-for-your-mental-health-findings-from-a-large-scale-study/)
- [American Psychological Association – Video Games and Cognitive Skills](https://www.apa.org/monitor/2014/02/video-game)
- [National Library of Medicine (PubMed) – Gaming Addiction and Academic Performance](https://pmc.ncbi.nlm.nih.gov/articles/PMC6037427/)
- [ScienceDirect – Online Gaming and Academic Achievement](https://www.sciencedirect.com/science/article/pii/S0747563213000787)
- [The Conversation – Gaming and School Performance](https://theconversation.com/do-video-games-harm-childrens-education-heres-what-the-evidence-says-122633)
- [ABC News Australia – Screen Time and Students](https://www.abc.net.au/news/2023-10-11/screen-time-impact-on-children-learning-development/102956418)
- [Common Sense Media – Teens and Video Games](https://www.commonsensemedia.org/articles/healthy-gaming-habits-for-teens)

### *Discussion*

Research into gaming and academic performance shows mixed findings about how gaming affects students. Some studies suggest that excessive gaming can negatively affect academic results because students may spend less time studying, sleeping, or completing homework. Research from PubMed and articles from ABC News Australia discuss how long gaming hours and increased screen time may reduce concentration and school performance. This supports the hypothesis that students who spend more time gaming are more likely to have lower academic results. In the collected survey data, students who reported gaming for longer periods were more likely to state that gaming negatively affected their grades or resulted in little academic improvement.
However, other research suggests that gaming does not always have negative effects on students. Studies from the Oxford Internet Institute and the American Psychological Association explain that moderate gaming may improve problem-solving, teamwork, and stress relief. Some students may use gaming as a way to relax after school, which could improve wellbeing and reduce stress levels. This suggests that gaming itself may not directly cause poor academic performance, and that other factors such as time management, sleep habits, and study routines may also influence results. Overall, the findings show that moderate gaming may have limited negative impact, while excessive gaming appears more strongly linked to lower academic performance.

### *Acquire data*

The data for this project was collected through a Google Forms survey created to investigate the relationship between gaming habits and academic performance. Participants answered questions about their gaming hours, English improvement, and whether they believed gaming affected their grades.
Survey Link:

- [Google Sheets survey data](https://docs.google.com/spreadsheets/d/1s1HmXkDKfTVtlYArIlFzf7CWeCgT-Yivz8kXy46GtKA/edit?usp=sharing)

### *Planning*

Field|Datatype|Format for Display|Description|Example|Validation
-|-|-|-|-|-
Gaming Hours|str|X-X Hours or X+|Number of hours students spend gaming on average in a week|8 hours +|Must contain a valid gaming hour category and cannot be left blank.
English Improvement|str|XX...XX|Describes how the student believes their English performance has changed|I've slightly improved|Must match one of the survey response options.
Perceived Impact on Grades|str|Yes/No|Indicates whether the student believes gaming has affected their academic grades.|Yes|Must only contain "Yes" or "No".

## **Phase 3 - Producing and Implementing**

Read the README to find out how the program works.

## **Phase 4 - Testing and Evaluating**

### *Analyse and conclude*

The survey results showed that students who spent excessive amounts of time gaming were more likely to experience lower English improvement results. Students who gamed for 8 or more hours often reported responses such as “I have not improved” or “I performed slightly worse,” while students who gamed for fewer hours more commonly reported slight or significant improvement in their English marks. This suggests that high gaming hours may negatively influence academic performance because students may spend less time studying or focusing on schoolwork. For example, several students in the “8 hours +” category stated that gaming affected their grades and also reported little or no academic improvement, while many students in the “1–4 hours” categories reported positive improvement in English. These findings support the hypothesis that excessive gaming can negatively impact English performance, although the data also showed that moderate gaming does not always lead to poor academic grades,suggesting that other factors such as study habits,time management,and personal discipline may also influence student performance. This suggests that there is a correlation between gaming hours and English performance, but the data does not directly prove any causation that gaming affected the academic results of GHS students.

### *Peer Verification*

Reviewer: Rachael Mackinnon
|Plus|Minus|Implications|
|-|-|-|
|Box design for the outer user Interface is very unique and visually appealing|Data is inconclusive and information cannot be drawn from the raw dataset (CSV → Option 1)|In regard to the actual data correlation to the hypothesis and information provided, you could possibly change your data to instead prove impact instead of improvement|
|Animated text is well paced in a way that offers some differentiation without making it long and draw out|Could add some other functions to improve you’re codes efficiency and convenience for the user|You could possibly add other functions like [Clear Screen] to clear the terminal and give your code a sleeker/cleaner look|
|Program itself is quite organised in a way that the user can mostly understand how to make their way around the system|Does not account for the difference in systems for OS and Mac, causing errors in different devices|For the search engine, a prior line of text that explains how to use the search engine would be much more convenient for the user in order to better understand the function|
|Charts usually show text seperate from the plt on the actual terminal, allowing comparison of raw data to visualisation|Search engine feature is incredibly confusing, with no specific guideline or options to know HOW to search for data.||
|There are many graphs/charts/options that provide a range of things the user can interact with and extract data from|||

### *Evaluate your project*

The system successfully achieved most of the functional and non-functional requirements outlined at the beginning of the project. Users were able to load and view the preloaded CSV dataset about gaming habits and academic performance using the dataset preview feature. The search function worked slightly well, allowing users to filter and explore information related to gaming hours, English improvement, and whether students believed gaming affected their grades, although has some minor bugs.
The system analysed the relationship between gaming time and academic performance through graphs and comparison features such as “Gaming Hours vs English” and “Does Gaming Affect Grades.” These visualisations helped make trends and patterns in the survey data easier to understand and supported the hypothesis that excessive gaming may negatively affect academic improvement. The program also included research conclusions that summarised the results of the analysis. Error messages appeared when invalid menu options were entered, which improved reliability and reduced user confusion.
Most of the non-functional requirements were also achieved. The interface was simple and easy to navigate because of the organised menu structure, clear labels, and readable formatting. The typewriter effect made the program feel more interactive and engaging while still remaining user-friendly. The code was separated into functions, which improved readability and made debugging and testing easier during development. The system was reliable because it consistently loaded and processed the dataset without crashing during normal use.
There are still some areas that could be improved. Data security is limited because the dataset could potentially be edited directly without restrictions or backup protection. However, since the system is only designed for research and classroom use, this was not a major issue. Another limitation is that the survey data was self-reported, meaning some responses may not have been fully accurate or completely unbiased. Even with these limitations, the system successfully fulfilled its purpose as a research and analysis tool investigating the relationship between gaming habits and English performance.
