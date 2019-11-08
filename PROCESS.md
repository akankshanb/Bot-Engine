# Milestone: PROCESS

For this milestone, we worked on implementing our use cases and applying software processes and practices.

For each use case, we implemented the basic flow described by the use case. We implemented a minimal proof of concept (that covered all our use cases).

### Process
For building our software we went through careful planning and delegation of work by conducting two sprints of one week each, as part of our process milestone. Wherein, at the beginning of each sprint we discussed any remaining tasks and assigned them equally to each team member.

For both the sprints,
* We divided our use cases into stories/tasks. 
* Assigned story points (1,3,5,8) to each user story
* Assigned a team member, who is committed to complete the story by the end of the iteration.

We utilized the kanban board (Github project). We used notes to indicate the story points and developer assigned for each tasks

#### Sprint 1:
* Wed Oct 23-- Fri Nov 1 --> [First Iteration start meeting notes](https://github.ncsu.edu/csc510-fall2019/CSC510-22/projects/1#column-3515) <br/>
In this Sprint, we aimed at replacing our mocking functionality with the actual service and divided the tasks accordingly. 

<img width="365" alt="Screen Shot 2019-11-08 at 4 17 02 PM" src="https://media.github.ncsu.edu/user/13256/files/5a57f680-0243-11ea-9162-0e3986f47f90">

##### Description of Tasks
The tasks were divided equally among the students. Each member of the team created their branch and pushed their commits. The first iteration was aimed to be able to complete individual tasks as dicussed in the scrum meeting and documented in kanban. All the bugs and errors were being fixed in individual branch before integration into the main Flask app for the bot. The tasks were assigned with points where each member was allowed to subdivide their 8 points into sub tasks according to their anticipation of time needed for each subtask within the main task. The areas of concentration were - 
* Ability to have basic conversations with bot and let the bot know intent of user
* Ability to correctly parse the data from the commands assigned by the user for each use case
* Store and access data for each user (plot images for each plot type)
* Generate plots, samples from the parsed data and return to user

#### Sprint 2:
* Sat Nov 2--Fri Nov 8th --> [Second Iteration start meeting notes](https://github.ncsu.edu/csc510-fall2019/CSC510-22/projects/1#column-3598) <br/>
This sprint was aimed at completing the remaining tasks for the POC and assignations accordingly.

<img width="370" alt="Screen Shot 2019-11-08 at 4 17 07 PM" src="https://media.github.ncsu.edu/user/13256/files/6774e580-0243-11ea-9753-1e7451ea3005">

##### Description of Tasks
For the second iteration, the main objective was to integrate individual contibutions and resolve conflicts, if present with our main application. Whenever a team member's tasks got completed, him/her were mergind their code to the master and resolvinf conflicts. After a succesful merge, a different team member was assigned to review their merges and suggest any fixes, if required. This helped in code refinement and also prevented severe program crashes or bugs in the application with the help of a second pair of eyes. 
Testing the code with the bot on server and checking for any latency in response were main focuses in this sprint.

### Practices

#### Core practice: Scrumban methodology
For our software process, we followed a "scrumban" methodology, that is a blend of kanban and scrum practices.
We did this by holding biweekly scrum meetings and maintaining a Kanban board for our tasks.
![Kanban board](https://media.github.ncsu.edu/user/10383/files/490ceb00-023f-11ea-862f-0e6fd21d335c)

#### Corollary practice: Code Reviews (Pull Requests)
Another practice we followed were code reviews. Each of us created a seperate branch for our tasks, and once those tasks were complete, we created a PR and assigned it to one of our team members for review. Once the reviewer reviews the code, they will merge the code into the master branch.
![Pull Requests](https://media.github.ncsu.edu/user/10383/files/1bc03d00-023f-11ea-9b2f-48770d2a05dc)


### Consistency

Work was equally divided among the team. Also, the work was completed uniformly.
Each of the team member had approximately 12 Story points worth of work.
And these tasks were assigned at the beginning of each sprint


#### Scrum meeting notes:
![Scrum notes 1](https://media.github.ncsu.edu/user/10383/files/a9e8f300-0240-11ea-9752-10949b34b05e)



In your markdown, include:

* Documentation on story creation and assignment at EACH iteration (one option is to include screenshots of kanban board).
* Any scrum meeting notes/process notes
* Include documentation of EACH iteration end. Include status of completed and incomplete tasks, and a process reflection.
