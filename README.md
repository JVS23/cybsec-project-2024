## LINK

Repository link: https://github.com/JVS23/cybsec-project-2024

After cloning the project into your chosen directory,
you can start the project with the following command:

``` 
python3 manage.py runserver
```

Depending on your configuration, you might need to use the command "py" or "python" instead of "python3".

The application is a simple Todo-app, which serves as a way to showcase different security flaws. In the section below we'll be assessing the implementations of these security flaws, and also their solutions. The solutions are commented out, and by uncommenting them the vulnerabilities can be fixed.

You need to log in to access user view for the todo-lists.
Here are test users and passwords for the application:

| Name        | Password    |
| ----------- | ----------- |
| tester1     | Mooc2024    |
| tester2     | Mooc2024    |
| jvs         | password    |




## Flaw 1 - A01:2021, Broken Access Control
LINK: https://github.com/JVS23/cybsec-project-2024/blob/686a38972db50136791aa8ac86f30b07b177ea73/src/todo/views.py#L19

Broken access control is the occurrance of a security flaw where users can access data that they are unauthorized to access, or even use functionalities that are meant to be for authorized personnel only.

These flaws can be fixed by requiring stricter authorization for accessing the functionalities. 

In this project, we can fix a broken access control by adding a Django decorator "@login_required" in functions that need to have authorization for access. As can be seen, by accessing a page without authorization you can encounter unplanned functionality, which can appear even in the form of serious security issues. In the example we can just see that the greeting works unexpectedly if there's no logged in user when there should be.

The technical implementation of the fix differs based on the used stack for building the application, but the principle remains the same. 


## Flaw 2 - A03:2021, Injection
LINK: https://github.com/JVS23/cybsec-project-2024/blob/main/src/todo/views.py#L63

There are multiple ways for developers to run into SQL injection vulnerabilities, and it's truly a classic security vulnerability. Nowadays there are many safety nets for developers to avoid the most common SQL injection fumbles, but they still happen due to avoiding these safety nets and/or more complex exploits.

This example has an SQL injection due to not using the Django prebuilt functionality for accessing data, and rather using classic SQL commands to the database. This leads to the SQL not being sanitized which allows funky things to happen. In this case you can use the query "getItemsVulnerable/?owner=' OR '1'='1" to override the "WHERE" statement, changing the designed functionality. This is technically a SQL injection, but also a lot worse things can happen due to them, for example the dreaded "DROP TABLES".


## Flaw 3 - A04:2021, Insecure Design
LINK: https://github.com/JVS23/cybsec-project-2024/blob/686a38972db50136791aa8ac86f30b07b177ea73/src/todo/views.py#L40

By creating applications with insecure design, there might often be unwanted consequences due to users accessing functionality that isn't meant for them to be used. There are countless ways to run into these problems, so following proper clean code & safety standards when developing applications is a must.

This example showcases a vulnerability due to insecure design in the Todo-list of a user, where users shouldn't be able to delete their Todo-list items for reasons only known by the admins. The 'Delete'-button should be invisible to users, but if the users manipulate the form HTML-element in browser console they can turn the button back on by switching visibility to "true". This is due to the button visibility only being hidden by CSS, which is can not be fully depended on. The Delete-button should check user validity in the backend to make sure of the request being valid (in this case the user needs to be "admin" to delete their todo's).


## Flaw 4 - A05:2021, Security Misconfiguration
LINK: https://github.com/JVS23/cybsec-project-2024/blob/686a38972db50136791aa8ac86f30b07b177ea73/src/config/settings.py#L91

Security misconfigurations are a very common vulnerability in applications, with OWASP reporting 90% of tested applications having a vulnerability regarding this area in 2021. Common misconfigurations are for example incorrectly configured authorizations, default settings or wrong configs regarding security settings and having wrong kinds of features enabled for the specific application.

In this application we have a few examples of security misconfigurations. In the settings.py file, there are examples of three bad configurations, which should definitely be fixed to avoid vulnerabilities. They span the lines 91-111, and have comments explaining their fixes. The first one is misconfigured password validations caused by not having validation options for them, which would lead to possibly insecure passwords. The second one leads to way too long of a session lifetime, which is a vulnerability in itself. The last one is the "SESSION_COOKIE_HTTPONLY"-setting, which can lead to stored data from Javascript being accessed.


## Flaw 5 - A06:2021, Vulnerable and Outdated Components
LINK: https://github.com/JVS23/cybsec-project-2024/blob/686a38972db50136791aa8ac86f30b07b177ea73/requirements.txt#L1

Most projects rely on often a large library of dependencies, which is pretty much the industry standard nowadays. While most well known open-source projects can be used safely, there is always a chance of them having security issues, and by using them in your projects you might be exposing your own projects to the same security issues too. 

In this example we have a requirements.txt file, which is a typical way to configure python project dependencies.

When cloning the project, users can install the dependencies with the command "pip install -r requirements.txt", but it's not recommended for this project since there is no use for it which is why both the items in reqs file are commented out to not have anyone accidentally install them. 

If the requirements file contains outdated dependencies, there is a risk of the software being insecure due to problems in older versions, for a good recent example see the XZ utils case: https://pentest-tools.com/blog/xz-utils-backdoor-cve-2024-3094
