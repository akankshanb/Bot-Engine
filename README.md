# CSC510-22

## Problem Description
Plotting graphs from all sorts of data is a necessitty among people with or without some sort of programming background. They first need to know what kind of data they have and the type of graph that can be generated from it. This in itself is a challenging task as not all types of graphs can be generated from any dataset. Then comes the part of which library in what language to use for plotting the said data into graphs. A plethora of options are available to choose from and can overwhelm the user. There is a need for a quick solution to map any dataset into a graph for people with little to no knowledge on plotting graphs.



## BOT Description
Tagline: **Plotbot**<br>
// Write about matplotlib and its uses. What kind of users use this.
// Using Python language matplotlib library.  
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


## Use cases
This is an example use case:
```
Use Case1: Give the user the right plot name with code snippet.
1 Preconditions
   User must have mattermost account.
2 Main Flow
   //User will request meeting and provide list of attendees [S1]. Bot will provide  possible meeting times and user confirms [S2]. Bot creates meeting and posts link [S3].
3 Subflows
  //[S1] User provides /meeting command with @username,@username list.
  //[S2] Bot will return list of meeting times. User will confirm time.
  //[S3] Bot will create meeting and post link to google calendar event.
4 Alternative Flows
  //[E1] No team members are available.
```
```
Use Case2: Plot the graph for the user with their sample data.
1 Preconditions
   User must have mattermost account.
   User must give the data in the format required by the bot.
2 Main Flow
   //User will request meeting and provide list of attendees [S1]. Bot will provide  possible meeting times and user confirms [S2]. Bot creates meeting and posts link [S3].
3 Subflows
  //[S1] User provides /meeting command with @username,@username list.
  //[S2] Bot will return list of meeting times. User will confirm time.
  //[S3] Bot will create meeting and post link to google calendar event.
4 Alternative Flows
  //[E1] No team members are available.
```
```
Use Case3: Provide admin with the ability to configure new plots into the server database.
1 Preconditions
  The admin must have a mattermost account.
  The admin must have permissions to configure the bot.
2 Main Flow
   //User will request meeting and provide list of attendees [S1]. Bot will provide  possible meeting times and user confirms [S2]. Bot creates meeting and posts link [S3].
3 Subflows
  //[S1] User provides /meeting command with @username,@username list.
  //[S2] Bot will return list of meeting times. User will confirm time.
  //[S3] Bot will create meeting and post link to google calendar event.
4 Alternative Flows
  //[E1] No team members are available.
```
