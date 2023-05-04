# _Design Document_
# NYC Crime Visualization
##### Kuan-Lin Lee, Chan-Yu Cheng, Li-Yeh Yang, Mengqiao Cai
# 
### Introduction
Living in NYC one of the most important things to notice is safety. Our project is to visualize the happen of the criminal in New York City. Therefore, we make a program to show the happening location of the criminal which includes the area or even the longitude and latitude. People could visualize a location that has a lot of crime and avoid getting to this place. For this purpose, Google Map could add a function to navigate the user to their location without passing by this dangerous place. According to the dataset we found, the dataset includes information with the time, date, location, crime types, etc. In our project, we implemented the dashboard, therefore, the user can select the specific information they are more likely to see.

### Project Outline
- Getting data from NYC [OpenData](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Current-Year-To-Date-/5uac-w243)

- Build a timeline of selected areas to understand the safety change overtime and histogram of different types of crime by seaborn.
- Interact with map by using gmplot drop pin on google map api for user to select area.
- Using ipywidgets to design UI. let users select which result they want.


### Desired Code Functionality
- Read dataset from NYC OpenData: we can download crime information from NYC OpenData website. And reading this csv file is one of the functions our project has to achieve. 

- Visualize dataset: we plan to visualize the dataset in two ways. One is to show the number between different types of crime. One is to show case numbers change over time. We plan to visualize by matplotlib and seaborn tools.
- Data Analyst: From the data we show, we can know the safest place in New York, and the dangerous place we should avoid to attend. To do this we import sklearn to do k-cluster.
- Interact UI: to more easily understand, we decide to import google map UI to identify the information on the map.

### Scientific Background
##### K-mean clustering
K-mean clustering is one of the unlabeled, unclassified data and enables the algorithm to operate on that data without supervision, which is more convenient for us to reach a wider audience. K-mean clustering only needs the k value and the algorithm can show the result we want.
Here is how the specific algorithm works.

-  initial **cluster centroids** $$\mu_1, \mu_2,..., \mu_k \in R^n$$ randomly
- Repeat until convergence: \{
For every i, set 
$$c^{(i)} := arg min_j ||x^{(i)} - \mu_j||^2$$
 For each j, set  
$$\mu_j :=\frac {\sum_{i=1}^m 1\{c^{(i)} = j \}x^{(i)}} {\sum_{i=1}^m 1\{c^{(i)} = j\} }$$
\}
### UML Diagram



![](https://i.imgur.com/2kgqjwI.png)



### Timeline of Project

|date|content|
|:----:|:-|
|Apr 15|Project begin|
|Apr 21|Topic confirm| 
|Apr 26|Specific architecture confirm|
|Apr 28|Architecture confirm|
|Apr 30|Git setup|

### External Libraries
[ipywidgets](https://ipywidgets.readthedocs.io/en/stable/)
[Seaborn](https://seaborn.pydata.org/)
[Pandas](https://pandas.pydata.org/)
[Gmplot](https://pypi.org/project/gmplot/)
[Webbrowser](https://docs.python.org/3/library/webbrowser.html)
[Os](https://docs.python.org/3/library/os.html)
[Sklearn](https://scikit-learn.org/stable/)
[matplotlib](https://matplotlib.org/)
