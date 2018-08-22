<h1>BUPA Liver Disorders Data Set Project - Summer 2018</h1>

<h3>About this Project</h3>
<p>This project is part of the Programming and Scripting module taught by Dr Ian McLoughlin in a HDip in Data Analytics course in GMIT. The task is to research ways to tackle the BUPA Liver Disorders data set using the Python programming techniques we have learned in the course so far.</p>  

<hr>

<h3>Project Instructions</h3>

<ol><li>Research background information about the data set and write a summary about it.</li>
<li>Keep a list of references you used in completing the project.</li>
<li>Download the data set and write some Python code to investigate it.</li>
<li>Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. A Python script will quickly do this for you.</li>
<li>Write a summary of your investigations.</li>
<li>Include supporting tables and graphics as you deem necessary.</li></ol>

<hr>

<h3>BUPA Liver Disorders Dataset Background Info</h3>

The UCI BUPA Liver Disorders data set The BUPA Liver Disorders data set was created by BUPA Medical Research and Development Ltd. (hereafter “BMRDL”) during the 1980s as part of a larger health-screening database [10].

BUPA Medical Research and Development Ltd. created the BUPA Liver Disorders dataset in the 1980s and was donated to the UCI machine learning repository in 1990. It is frequently used as a benchmark for classification algorithms and should not be confused with the Indian Liver Patient Data Set which is also commonly used as a classification benchmark. 

The data set consists of 345 rows and 7 columns. Each row consists of data points representing one male subject. The data in the first 5 columns is integer-valued and shows the results of various blood-tests which can help researchers to deduce the likelihood of alcohol-related liver problems. Column 6 shows the number of alcoholic drinks consumed by the subject on a daily basis. Column 7, which has caused a degree of confusion in the past, is just a selector created by researchers to split the data into training and subsets. Previous researchers have misunderstood the data in column 7 to represent the presence or absence of liver disorder. 

The 7 columns of the data set represent the following data points:
1 mcv mean corpuscular volume 
2 alkphos alkaline phosphotase 
3 sgpt alamine aminotransferase 
4 sgot aspartate aminotransferase 
5 gammagt gamma-glutamyl transpeptidase 
6 drinks number of half-pint equivalents of alcoholic beverages drunk per day 
7 selector field used to split data into two sets

Source: [McDermott, J. & Forsyth, R.S. (2016). Diagnosing a disorder in a classification benchmark. Pattern Recognition Letters, 73, 41-43.]

<hr>

<h3>Methodology</h3>
Download data set from https://archive.ics.uci.edu/ml/datasets/liver+disorders 
Run Python Script to calculate mean, minimum, and max value of each column
Use Matplotlib to create charts from the data

<h3>Sources</h3>
Basic plots with Matplotlib tutorial https://www.youtube.com/watch?v=SiCyTcudoSE
Matplotlib intro https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF
Pandas tutorial http://www.datasciencemadesimple.com/get-minimum-value-column-python-pandas/
Pandas max value index https://stackoverflow.com/questions/39964558/pandas-max-value-index
DataFrame help https://stackoverflow.com/questions/26047209/what-is-the-difference-between-a-pandas-series-and-a-single-column-dataframe

