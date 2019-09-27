# CSC510-22

## Problem Description
Plotting graphs from all sorts of data is a necessitty among people with or without some sort of programming background. They first need to know what kind of data they have and the type of graph that can be generated from it. This in itself is a challenging task as not all types of graphs can be generated from any dataset. Then comes the part of which library in what language to use for plotting the said data into graphs. A plethora of options are available to choose from and can overwhelm the user. There is a need for a quick solution to map any dataset into a graph for people with little to no knowledge on plotting graphs. Also, plotting graphs for data visualization is a frequent task for data engineers and machine learning enthusiasts. Even the data engineers get confused which plot to use and how to plot their data.

## BOT Description
This Library bot makes it easy for the users to choose the kind of plot and makes their work easy by also providing details of how to plot their data. Data visualization by plotting graphs is most common task for Data engineers, Machine learning enthusiasts and commonly preferred way to see the statistics of any study. One of the widely used library in Python for plotting graphs is **matplotlib**. matplotlib is a plotting library used in python programming language and it can be used in python scripts, shell, web application servers and other graphical user interface toolkits. There are many kinds of plots available in this library, but user might not be aware of which kind of plot to use for his data. So for the users working with Python, this bot will suggest the library to use for  plotting and also help users choose the right kind of plot based on the type of data user wants to visualize. Also, this bot will provide him with sample code for the kind of plot user wants to use and also lets him try out the code and see the way plot looks like by providing some sample data.  
* This is a chatbot interface that will help the user to get the right graph for their data.
* This bot will not only provide with correct function but also its usage by providing a sample source code.
* The user can also test the correctness of the plot by visualizing their data input on the plot generated by the bot.
* The types of plots the bot can plot are:
   * Line graph
   * Histogram
   * Scatterplot
   * Piechart
   * Box-plot
   * 3D plot
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

#### Storyboard
![PlotBot-storyBoard](https://media.github.ncsu.edu/user/13110/files/587c0e80-e0ad-11e9-9317-2cd3607b8e27)


## Architecture Design


### High-level architecture  


### Architecture components  


### Additional patterns

#### Blackboard


#### Object Oriented  


#### Implicit and Explicit Invocation
//TODO
