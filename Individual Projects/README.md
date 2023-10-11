# Individual Projects ✍🏽

Each module had two mandatory individual mini-projects called "To-Do". The aim was to put into practice what we had learned and to prepare us for the final project, so there was no feedback, but we could discuss our doubts during the weekly mentoring sessions. In general, the second "To-Do" of each module was more challenging than the first one. 

## Table of Contents

* [Module 1](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#module-1)
  - [Todo1 - Python’s installation tutorial](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo1---pythons-installation-tutorial)
  -  [Todo2 - Automatic Sample Calculation](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo2---automatic-sample-calculation)
* [Module 2](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#module-2)
  - [Todo3 - It was a match! - Working with Python’s Lists](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo3---it-was-a-match---working-with-pythons-lists)
  - [Todo4 - You’re hired! - Working with Python’s Dictionaries](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo4---youre-hired---working-with-pythons-dictionaries)
 * [Module 3](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#module-3)
   - [Todo5 - ResiliaData - Data Modeling](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo5---resiliadata---data-modeling)
   - [Todo6 - Resilia Database](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo6---resilia-database)
* [Module 4](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#module-4)
  - [Todo7 - Weekly Revenue and Cost Reports](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo7---weekly-revenue-and-cost-reports)
   - [Todo8 - Exploratory Analysis of a Company’s Employees](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#todo8---exploratory-analysis-of-a-companys-employees)
 * [Module 5](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/tree/main/Individual%20Projects#module-5)
   - [Todo9 - Report with Graphs: Why are they leaving our company?](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/main/Individual%20Projects/README.md#todo9---report-with-graphs-why-are-they-leaving-our-company)
   - [Todo10 - Tableau Visualization - World Happiness Report](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/main/Individual%20Projects/README.md#todo10---tableau-visualization---world-happiness-report)
***
## Module 1

### Todo1 - Python’s installation tutorial 

> ***Briefing**: It’s often required to consult documentation while working with data projects and analysis. To start putting it into practice and also help the class, you must document the step-by-step installation process and environment preparation for working with Python (describing the operating system, software you used and so on). The submission must be a text file in Google Docs.*

:toolbox: **Google Docs, Python, VS Code**

:link:[**My Solution**](https://docs.google.com/document/d/1k8pvCAioDAefseshrdmHkABXBL0wdj7V2vhbnuhl5j8/edit) 


### Todo2 - Automatic Sample Calculation

> ***Briefing**: An NGO wants to understand Brazilians’ perceptions of local government action to protect the environment. The survey is to be conducted in each of Brazil’s state capitals. But first, it’s necessary to check how many people should be interviewed.* 
> -  *Your code has to calculate the optimal sample for each capital, taking into account the population of the city and the expected margin of error.*
>- *In the following link ([Calculadora de tamanho de amostra](https://pt.surveymonkey.com/mp/sample-size-calculator/)) you can study a similar calculator and also use it to test your final code.*
> - *Your work must be submitted in a single .py file.*

:toolbox: **Python, VS Code**
  
:link:[**My Solution**](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/36405f1bd6b143cef2f7eb791829af6970727b8b/ToDo2_Sample_Calculator.py) 

***

## Module 2

### Todo3 - It was a match! - Working with Python’s Lists

>***Briefing**: A startup is working on an application that verifies a candidate's compatibility with a vacancy according to their result in the selection process. For this purpose, they created a test that generates a string in the format eX_tX_pX_sX (in which every X corresponds to the individual's assessment in one of the stages of the process: e = the interview, t = theoretical exam, p = practical exam, and s = soft skills’ evaluation. We have the following list of candidates as an example, along with their results:*

 | Candidate | Results |
|:--------:| :------------|
|Candidate 1|e5_t10_p8_s8|
|Candidate 2| e10_t7_p7_s8|
|Candidate 3| e8_t5_p4_s9 |
|Candidate 4| e2_t2_p2_s1|
|Candidate 5|e10_t10_p8_s9|

>- *You must create a Python list to store these results (and any other results you want in the same format). Subsequently, create a function that searches for qualified candidates based on the user's desired criteria.*
>
>- *The user should enter the minimum score for e, t, p, and s that they want to search for, and our application will list all available candidates with scores greater than or equal to the ones the user has entered. If we search for a candidate with a score of 4,4,8,8, for instance, we will receive a notification that candidates 1 and 5 fulfill this requirement (they performed well in the practical assessment, and have an excellent level of soft skills!*
>- *The submission must be made in a single .py file*.

:toolbox: **Python, VS Code**
  
:link:[**My Solution**](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/36405f1bd6b143cef2f7eb791829af6970727b8b/ToDo3_It_was_a_mach!.py) 


### Todo4 - You’re hired! - Working with Python’s Dictionaries

> **Briefing**: *A company has received many CVs for data job vacancies and now needs to sort out how many applicants have the required profile and how many are applying for each role. Your task is to create a project that utilizes Python dictionaries that will record the quantity of individuals that possess one or more of the necessary keywords on their CV and the total number of CVs for each vacancy.*
>
>*Every job opportunity requires applicants to include in their CV at least one of the following keywords:*

 Opportunities | Keywords
-------- | ------------
Data Analyst|Python, Power BI, SQL, Good Communication
Data Scientist|Python, Database, Machine Learning, Statistics, Problem-Solving

>***In short, your Python code should check:***
>-  *The number of applicants;* 
>- *The candidate’s name;* 
>- *Which vacancy they are applyin*g for; 
>- *A short text summarizing the participant's CV;*
>
>***The code’s output should be:***
> - *How many people are registered for each vacancy;*
> - *How many people have a CV with the keywords we're looking for.*                                
>
>***Extra challenges:***
>- *Send the GitHub link with the commits properly documented;*
>- *Read the summaries from .txt files in a folder.*


:toolbox: **Python, VS Code**

:link:[**My Solution**](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/36405f1bd6b143cef2f7eb791829af6970727b8b/ToDo4_You_are_hired!.py)

***
## Module 3

### Todo5 - ResiliaData - Data Modeling

>***Briefing**: Resilia plans to introduce a new system to evaluate the technologies (languages and tools) utilized by our partner companies and make necessary adjustments to our tech stacks. We want to have a registration system for:*
>-   *our partner companies;*  
>-   *technologies that include the option to select the area of expertise such as: web development, data, marketing and more;*
>-   *which technologies the partner companies are currently using.*
>
>*You were assigned the responsibility of modeling this system and to answer some questions with our model:*
>-   *Are there other entities besides the ones mentioned?*
>-   *What are the main fields and types?*
>- *How are these entities related?*
>- *Use 2 records for each entity to check the information in our model.*
>
> *Provide a copy of the suggested model that addresses these inquiries.*

:toolbox: **[brModelo](https://www.sis4.com/brModelo/), Excel**

:link:**[**My Solution**](https://drive.google.com/file/d/1ww-qVhNGWfthkwwaTUk8APCS81MO91Mh/view?usp=sharing.)**



### Todo6 - Resilia Database

>***Briefing**: Do you recall our database model for ResiliaData (Todo5)? Our project has been approved with a few additional requests, so let’s adjust our model and have the database functioning! The only adjustments that were requested are:*
>-   *Create a new entity called "reports", to store when the data was collected and provide a history of which technologies companies were using at the time Resilia compiled the data. In other words, instead of indicating the technologies at the companies directly, we will refer to this table every six months to check their use of tech stacks.*
>  - *Next, you will populate this database with dummy data from four companies and two surveys (January 2022 and February 2021). You can also search for real companies (including the ones you are interested in for job openings) and use their information, even if it is not entirely accurate.*
>
>*After making changes to our model and creating a database with simulated data, let's consider these SQL queries:*
>1. *Which company uses the most technologies in the latest survey (Jan 2022)?*
>2. *Which company used the fewest technologies in the previous survey (Feb 2021)?*
>3. *How many companies currently use data technologies?*
>4. *How many businesses nowadays use technologies that do not involve data?*
>
>*You must submit a .SQL file with the database and the queries to answer the questions above.*

:toolbox: **PostgreSQL**

:link: [**My Solution**](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/main/ToDo6_Resilia_Database.sql) 
***

## Module 4

### Todo7 - Weekly Revenue and Cost Reports

> ***Briefing**: A shop would like to have weekly reports of its revenues and costs. You have been hired by the manager to produce a one-week report to show the shop owner how he can benefit from analyzing the data. The shop manager has provided you with a table of a week's expenses for reference:*

|  Day of Week |  Cleaning | Food |  Commuting | Other |
|   ---   |  ---   |  ---   |   ---    | ---   |
| Monday | 100,00 | 221,60 | 150,00 | 0,00 |
| Tuesday | 0,00 | 375,31 | 100,00  | 0,00 |
| Wednesday | 100,00 | 412,00 | 125,00  | 2310,00|
| Thursday | 0,00 | 495,20 | 300,00  | 500,00 |
| Friday | 100,00 | 411,53 | 275,00  | 0,00 |
| Saturday | 100,00 | 245,00 | 525,00 | 0,00|
| Sunday | 0,00 | 164,00 | 75,00 | 820,00|

> *In addition, he informed you that the earnings are not in this spreadsheet, but that he has the following list: R$2,200.00 ; R$2,420.50; R$3,391.50; R$5,322.00; R$4,898.50 ; R$4,200.00; R$3,893.00 respective to the days of the week.*
>
> *You have the freedom to include any statistics you wish in the report, but it must contain the following:*
> -  *The deduction of a 7% tax from daily earnings;*
> -  *The total earnings;*
> - *The average earnings per week;*
> - *The total expenses by category;*
> - *The weekly average of all expenses;*
> - *Provide the daily profits to determine the most profitable day of the week, as well as the total profit for the entire week;*
> - *Additionally, include explanations about how the amounts were obtained and present the results clearly.*
>
>*The final submission should be in the form of a Google Colab.ipynb notebook.*

:toolbox: **Python (Pandas), Google Colab**

:link: [**My Solution**:](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/main/ToDo7_Weekly_Reports.ipynb) 



### Todo8 - Exploratory Analysis of a Company's Employees

>***Briefing**: In this new task, you must conduct an exploratory analysis of the employee data for 'Milsa Company' to enable the company's leaders to obtain a better understanding of their current workforce. Prior to conducting the exploration, it is necessary to inspect the data quality, including outliers, and to perform cleaning if necessary. You should answer the following questions:*
>
>1.  *What is the average age of the staff?*
>2.  *Among the employees who have kids, what is the most common number of children?*
>3.  *What are the average and median salaries of the employees? What do these values suggest?*
>4.  *What is the educational level of the employees?*
>5.  *What is the average salary and age of married employees?*
>6.  *Which employee has the highest salary? Specify their attributes.*
>7.  *Which employee has the lowest age? Specify their attributes.*
>8.  *Who are the employees who are at most 35 years old, are from the capital and have a high school education?*
>9.  *Find a correlation between all the employees' attributes.*
>    
>*You may provide additional relevant information. You must submit a Google Colab.ipynb notebook file.*
>
>*Extra questions I suggested:*
>10: *According to the level of education, what is the maximum, minimum and average salary found?*
>11: *What is the variability found in the database in the salary and age categories?*
>12: *Where are the employees with higher education located?*
>
:toolbox: **Python (Pandas, Matplotlib, Seaborn), Google Colab**

:link: [**My Solution**](https://github.com/enilaester/Bootcamp-Data-Analytics-Resilia/blob/main/ToDo8_Exploratory_Analysis_Employees.ipynb): 
***

## Module 5

### Todo9 - Report with Graphs: Why are they leaving our company?

> ***Briefing**: The following bubble chart is taken from the book: "Storytelling with Data: Let's Practice!" by Cole Nussbaumer Knaflic. The scenarios proposed in the book can be utilized to help us comprehend and exercise several lessons related to data communication.*

**![](https://lh5.googleusercontent.com/bHwLuLsfV0j2tl7bftz87vdzBLZEgRXwOPzczC_CNOXQcO9WFDwy7J8B0zDzcXhiGpzzOpWhWm61UjJ9tmhGz7fsRlotMRi917AHrIXDNliQRFtRjMLuhLYLXIHLLU3ZPRaL9Wvj-5w77GwzDAEaYA)**

> *In terms of visualization, let’s consider the following scenario: imagine you're the Chief of Staff for the Chief Marketing Officer (CMO) of a big corporation. Your superior, the CMO, has requested that you collaborate with your Human Resources Business Partner (HRBP) to grasp the main reasons for employee turnover within the marketing department and report back with your discoveries. Your HRBP has analyzed the data and sent you the provided visualization. Take some time to become familiar with the graph and its data before continuing with the following instructions.*
>
  > *1.  What is being shown here? Write a text explaining the data. (Hint: imagine you need to explain this graph to the CMO. Write about how you would do this out loud (making assumptions as necessary). Is this data easy or complicated to talk about in its current form?)*
  > 
  > *2.  What observations can you make from this data? Put three specific conclusions into words (Write complete sentences).*
  > 
  > *3.  What is not ideal or could be avoided in the visualization in its current form? What questions would you ask, or what feedback would you give to whoever made the graph? (E.g. suppose your HRBP spent a lot of time creating this graph, how can you structure your feedback so that they don't get offended?)*
  > 
  > *4.  Let's visualize! Come up with three different ways of showing this data. What are some advantages and weaknesses of each? List them.* 
  > 
 > *5.  Which visualization best represents the data and why?*
  >
  > *6.  Download the data and create the visualization you think best represents it with the tool of your choice (Matplotlib, Tableau, etc.).*
  > 
  > *7.  The aim is to think beyond simply showing data. How can you turn this information into a data-driven story for your manager, the CMO? (What is the context of the story?)*
  > 
  > *8.  You'll need to send a report to the CMO, with all the questions above answered. Find the best way to present this information.*
>
>*The assignment can be sent as a link to a .pdf file with illustrations or as a link to a Google Colab.ipynb notebook. Both must contain all the answers.*

:toolbox: **Tableau, Google Docs**

:link: [**My Solution**](https://drive.google.com/file/d/1gN6YQT0d4ZGLyP5OjOzOjOPqZJp9V0FE/view?usp=drive_link)

### Todo10 - Tableau Visualization - World Happiness Report 

>***Briefing:** The World Happiness Report is a landmark study of the state of global happiness. Leading experts in all fields - economics, psychology, research analysis, national statistics, health, public policy and much more - describe how measures of well-being can be used effectively to assess the progress of nations. The happiness score was calculated according to various characteristics of the countries, such as GDP per capita, healthy life expectancy, social support, freedom to make life choices, generosity and corruption perception.*
>
>*You have received the World Happiness Report 2022: <[https://www.kaggle.com/datasets/mathurinache/world-happiness-report?select=2022.csv](https://www.kaggle.com/datasets/mathurinache/world-happiness-report?select=2022.csv)> and your task is to analyze the data and create a presentation for a conference. Focus on the most relevant points. Nonetheless, one of the conference's requirements is for your presentation to have different graphics. Using Tableau, make the following visualizations with the dataset:*
>1. *A simple bar chart*
>2. *A grouped bar chart*
>3. *A stacked bar chart*
>4. *A choropleth map*
>5. *A bubble map*
>6. *A line graph*
>7. *A scatter plot*
>
>*If needed, preprocess the data in a notebook or in Tableau. Then share your Tableau presentation with a link.*
>
:toolbox: **Tableau**

:link:[**My Solution**](https://public.tableau.com/views/Todo10_Aline_Relatrio_Mundial_Felicidade/RelatrioMundialdaFelicidade-2022?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
