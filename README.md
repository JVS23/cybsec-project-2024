## LINK

Repository link: https://github.com/JVS23/cybsec-project-2024

After cloning the project into your chosen directory,
you can start the project with the following command:

``` 
python3 manage.py runserver
```

Depending on your configuration, you might need to use the command "py" or "python" instead of "python3".

The application is a simple Todo-app, which serves as a way to showcase different security flaws. In the section below we'll be assessing the implementations of these security flaws, and also their solutions. The solutions are commented out, and by uncommenting them the vulnerabilities can be fixed.

You need to log in to access user-specific Todo-lists.
Here are test users and passwords for the application:

| Name        | Password    |
| ----------- | ----------- |
| tester1     | Mooc2024    |
| tester2     | Mooc2024    |
| jvs         | password    |




## Flaw 1 - A01:2021, Broken Access Control
LINK: TBA

Broken access control is the occurrance of a security flaw where users can access data that they are unauthorized to access, or even use functionalities that are meant to be for authorized personnel only.

These flaws can be fixed by requiring stricter authorization for accessing the functionalities. 

In this project, we can fix a broken access control by adding a Django decorator "@login_required" in functions that need to have authorization for access. As can be seen, by accessing a page without authorization you can encounter unplanned functionality, which can appear even in the form of serious security issues. In the example we can just see that the greeting works unexpectedly if there's no logged in user when there should be.

The technical implementation of the fix differs based on the used stack for building the application, but the principle remains the same. 


## Flaw 2 - A04:2021, Insecure Design
LINK: TBA

By creating applications with insecure design, there might often be unwanted consequences due to users accessing functionality that isn't meant for them to be used. There are countless ways to run into these problems, so following proper clean code & safety standards when developing applications is a must.

This example showcases a vulnerability due to insecure design in the Todo-list of a user, where users shouldn't be able to delete their Todo-list items for reasons only known by the admins. The 'Delete'-button should be invisible to users, but if the users manipulate the form HTML-element in browser console they can turn the button back on by switching visibility to "true". This is due to the button visibility only being hidden by CSS, and also the Delete-button not checking user validity in the backend (in this case the user needs to be "admin" to delete their todo's).


## Flaw 3 - A06:2021, Vulnerable and Outdated Components

## Flaw 4 - A03:2021, Injection

## Flaw 5 -

