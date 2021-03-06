# Design Milestone

## Problem Description

Visualizing data is an integral part for people to understand data literacy. Data literacy allows a learner to ask and answer meaningful questions by collecting, analyzing and making sense of the data encountered in real life. Many students, data analysts, data scientists and machine learning enthusiasts can analyze data using integrated plots and determine the most appropriate way to visualize information. As they visualize data as it moves through the types of plots, they formulate and discover meaning from the visual representation. As smoothly as they ace through comprehending the data, many find it difficult to write code to achieve this task, especially people without a programming background. Moreover, with a plethora of libraries available in the same language, it becomes a daunting task to go through the installation procedures and following lines of code step by step. Here comes PlotBot - a solution that helps user not to get overwhelmed. There is a need for a quick solution to map any dataset into a graph for people with little to no knowledge on plotting graphs. It is quick and easy with a friendly interaction platform which caters to a specific task instead of providing a million solutions.

## BOT Description
This library bot makes it easy for the users to choose the kind of plot and makes their work easy by also providing details of how to plot their data. One of the widely used library in Python for plotting graphs is **Seaborn in Matplotlib**. Matplotlib is a plotting library used in python programming language and it can be used in python scripts, shell, web application servers and other graphical user interface toolkits. Matplotlib contains many APIs for plotting different types of data. It also has modules that perform applicaiton specific functions. So for the users working with Python, it might be difficult to navigate through their extensive documentation to find just the right functions and library dependencies. Our bot provides the required libraries.Not only that, PlotBot will provide users with sample code for the kind of plot user wants to use to let them try it out on their own system. For users who want their plot to be made and do not want to go through the rigorous lines of code, Potblot provides an additional feature of plotting the graph for them with their data they provide.  
Therefore, to sum it up - 
* This bot provides users with correct function and libraries through sample source code.
* The user can also test the correctness of the plot by visualizing their data input on the plot generated by the bot.
* The types of plots the bot can plot are:
   * Line graph
   * Histogram
   * Scatterplot
   * Box-plot
   * Bar chart with facets
 <br>

Tagline: **Plotbot**

## Use cases
Below are some of the use cases for **PlotBot**
```
Use Case 1: Give the user with code snippet for the required type of graph.
1 Preconditions
   User must have mattermost account.
2 Main Flow
  User provides the bot with the type of graph it requires [S1].
  Bot returns the appropriate library packages with a usage [S2].
  Bot asks the user if they need a sample visualization. User responds [S3].
  Bot returns according to the response [S4].
3 Subflows
  [S1] User tells bot the graph type @graph_type. e.g. Histogram
  [S2] Bot returns the entire code snippet.
  [S3] Bot asks for plotting sample code provided. User confirms.
  [S4] Bot returns the sample plot.
4 Alternative Flows
  [E1] Requested graph data not available.
```
```
Use Case2: Plot the graph for the user with their data.
1 Preconditions
   User must have mattermost account.
   User must give the data in the format required by the bot.
2 Main Flow
   User requests bot to generate a graph of a type for their data [S1].
   Bot will provide a specific data format for the graph to be generated [S2].
   User provides its data in the specified format [S3].
   Bot generates the graph and returns it to the user [S4].
3 Subflows
  [S1] User gives a /plot command with @graph_type.
  [S2] Bot will return a sample data format, e.g. a comma separated list.
  [S3] User provides the data in the requested format.
  [S4] Bot returns the generated graph.
4 Alternative Flows
  [E1] Incorrect data format. Requested data format to be provided
  [E2] Requested graph type not available.
```
```
Use Case3: Provide user with the ability to view all his plots.
1 Preconditions
   User must have mattermost account.
2 Main Flow
   User requests to provide all his plotted graphs using this bot.
3 Subflows
  [S1] User asks to give all the plotted graphs.
  [S2] Bot will return the file of all user plotted graphs. 
4 Alternative Flows
  [E1] No plots available.
```


### Design Sketches

#### Wireframe  
![Issue1](https://media.github.ncsu.edu/user/13256/files/f077f900-e0a9-11e9-9d30-c3348e7971da)
![Issue2 and 3](https://media.github.ncsu.edu/user/13256/files/4e144180-e0ba-11e9-9578-6536d96073c3)
#### Storyboard
![PlotBot-storyBoard](https://media.github.ncsu.edu/user/13110/files/587c0e80-e0ad-11e9-9317-2cd3607b8e27)


## Architecture Design
PlotBot is a chat bot which helps in plotting graphs and viewing your history. The architecture follows a hybrid pattern, where repository pattern is used for storage section and pipe and filter for message parsing and plotting. The compute elements lie on EC2 instance, contanarized and deployed from scripts where as thee storage component is setup separately. The requested data is generated/fetched and saved by the compute elements into the storage unit and then passed to the Mattermost server to be then pushed to the user interfacing via client

### High-level architecture  
![SE_archi](https://media.github.ncsu.edu/user/13071/files/625a3d80-e0be-11e9-9e92-e9e9de2252d8)

### Architecture components
#### Mattermost server API endpoint: 
The server endpoint parses incoming request calls, fetches metadata, identifies the user and sends this information to message parsing engine. When the message parsing engine returns a piece of data for the user, the MM endpoint API pushes it to the specidied user.
#### Message parsing engine: 
The message parsing engine, as the name suggests take the requests from the marttermost server endpoint, analyzes it and classifies the request in one of the three specified scenarios. Once classified, it sends the request either to the plotting service or to the datastore depending on the usecase. The output from either is then encoded into human readable message and sent back to the the Mattermost server endpoint.
#### Poltter service:
The Plotter service, takes graph type and graph data as input, normalizes it and plots the data. It then converts this data into an image and sends it back to the message parsing engine. While doing this, the plotting service also tags this data and plot with the userID (user token) and a timestamp and pushes it to the postgress and storage to be saved for future use.
#### Postgress and storage unit:
The postgress and storage unit, takes input from Plotter service and stores the data into DB. The input consists of data, timestamp and tags which identifies a particular plot asked by a specific user at a specific time. The Message Parsing engine can also request data back from the Storage unit where it replies back with the saved plot(s) as requested


### Additional patterns

#### Repository 
We intend to use the datastore as a repository pattern, where the Message parsing engine can talk to the postgress service to query and fetch data that is requested by user i.e the sample graphs or the history of plots. The Plotting service will push the data that is has generated to the Data mapper agent which will push in the plot to the specified location as per the tags provided. Thus, if the Query contains the correct tags, the subset of plots stored on the datastore can be identified, fetched and returned to the user.

![image](https://media.github.ncsu.edu/user/13071/files/e4a12c80-e0d3-11e9-9425-a153a6294670)

#### Pipe-filter
We use a pipe and filter method to parse, analyze each component of the input message and respond accordingly.
The input message is parsed and classified into the three categories that the bot offers, else it returns a error in request. Once classified, the metadata and input data (plot data points) are used to fetch plots from datastore or generate plots as per the classification. Once the output is generated and saved (if required) it is then encoded back using the user token to be sent back to the Mattermost server whic replies to the user

![image](https://media.github.ncsu.edu/user/13071/files/0a323400-e0dc-11e9-846c-bf429df10f06)


