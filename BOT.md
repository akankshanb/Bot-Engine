# MILESTONE: Library BOT

## Index
1. [Installation Steps](<a id=install https://github.ncsu.edu/csc510-fall2019/CSC510-22/blob/master/BOT.md>) 
1. [Use Cases](#usecase)
	* [Use Case 1](#usecase1)
	* [Use Case 2](#usecase2)
	* [Use Case 3](#usecase3)
2. [Mocking](#mocking)
3. [Bot Implementation](#implement)
	* [Bot Platform](#platform)
	* [Bot Integration](#integration)
4. [Selenium Testing](#test)
	* [Use Case 1](#test1)
	* [Use Case 2](#test2)
	* [Use Case 3](#test3)
5. [Task Tracking](#track)
6. [Screencast](#screencast)

## <a name="install"></a> INSTALLATION STEPS:
* sudo apt-get update
* sudo apt-get -y install python3-pip
* pip3 install flask
* pip3 install mattermostdriver
* pip3 install -U PyYAML
In this milestone, you will begin developing your bot based on your accepted design proposal.

# PLotBot
The primary focus of this milestone will be to integrate with the bot platform for your bot and develop the interaction component of your bot.
There are also several techniques (such as testing and mocking) that you will be required to perform as part of this milestone.

## <a name="usecase"></a> USECASES

### Bot Implementation

In implementing your bot, you will have to primary tasks:

* **Bot Platform**: Implement hooks into platform. You should be able to have a fully operational bot within your platform (Slack/Github) that can response to basic commands.
* **Bot Integration**: Implement basic conversation/interaction with bot. You need to support the ability to fully have a conversation with an bot as defined by your use cases.

### Use Case Refinement

Based on the feedback from your design milestone and your initial implementation, improve the use cases for your bot. This should be your final iteration of your use case design, it will be very difficult to change past this point.

Describe the changes you made to improve the design of your use cases.

### Selenium Testing

To support testing of your bot, you will use Selenium to verify that the bot is returning the correct response based on a input message.

[See full example Selenium test for Slack](https://gist.github.com/chrisparnin/e3ee1a96c681f12ae11246cfe3225182)

```java
@Test
public void postMessage()
{
	driver.get("https://csc510-fall16.slack.com/");

   ...

	// Find email and password fields.
	WebElement email = driver.findElement(By.id("email"));
	WebElement pw = driver.findElement(By.id("password"));

   ...
```

Create a selenium test that demonstrates each use case. Demonstrate at least one "happy path" and one "alternative" path for each use case.

### Mocking Service Component

Because the focus on your milestone is platform integration and bot interaction, you will not yet have a working service implementation. Implement mock services and data to support service integration. For example, if you were implementing a meeting bot that helps set up meetings, use mock calendar data to determine available meeting time, rather than integrate with a user's Google calendar. A proper mocking infrastructure would allow you to swap real and testing information in a single place, instead of hard-coded throughout your code base.

**Failure to use appropriate mocking/injection techniques will result in 0 credit**. Do not do this:

```javascript
bot.hears("command", function(){ bot.replys("fake answer");});
```

### Screencast

Create a screencast of your bot performing your three primary use cases. Demonstrate your selenium tests being executed.

## Deliverables

Add your code, and BOT.md document describing the following materials.

* Bot Platform Implementation (20%)
* Use Cases Refinement (10%)
* Mocking infrastructure (30%)
* Selenium testing of each use case (30%)
* Screencast (10%)

**Contribution requirements**: Each team member must make contributions on a milestone (e.g., committing code, being assigned and completing tasks). Failure to perform any work will result in no credit for a team member for the milestone.

**Secrets**: Including secrets (passwords, tokens, etc.) in your source code or checked into repository, will result in significant deductions to your grade.

DUE: Tuesday, October 22, before midnight.
