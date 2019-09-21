# CSC510-22
## Problem Statement
### What is the problem? 
*  Everyone cannot know the usage of all libraries/api’s in all languages.
*  It’s a tedious task to search for the right documentation and to know when to use which library/api.
*  most of the time, while using a library/API, you open a lot of tabs on your browser for search results, this leads to counter productivity and confusion. 
*  The need for specific information. For example, steps to install a library in a Linux machine does not give results for only that machine but comes with additional information for different machines like Mac or Windows. 
* Another issue with using libraries is using a proper version of itself and all of its dependencies. Many times we need to upgrade some library, but are unaware or have difficulty knowing what other dependencies will have to be updated. This can cause conflicts if done manually leading to confusion when searched online.

Thus, a system is required where you can quickly query anything you want, and get results as per your need with specific information from an interface which is much easier to use with human like interaction


## BOT Description
Tagline: **Jarvis for APIs**

### What is a library bot?
* This is a chatbot interface that will provide details about any library or API a user wants to know about.
* Things like what does the API do, which version to use, what dependencies are required.
* The bot will be interactive with additional responses for edge cases, like information it hasn’t rendered or request additional information from the user, through text mining and keyword searching.
* It shall consist of additional functionality of giving suggestions for upgrading certain libraries, if available.

### What can it do?
* For a specified language, query on a package or library or api would 
  * Search the closest library name api to the query and search on that
  * return what methods are present if details are asked
  * return usage of a method, readme if present
  * return examples on that library/api
  * return a link to stack overflow top search results
  * return a link to that library/API’s official documentation
* Redirect search results to a specified user via an email.

### How can you use it?
Specify language && specify the library/api for its usage.
E.g. How can I use the socket api in python?

Ask to install a certain package.
E.g. : install pycryptodome on all of my X-level machines

Check for dependencies and update libraries:
E.g: check and upgrade all dependencies for pycryptodome
