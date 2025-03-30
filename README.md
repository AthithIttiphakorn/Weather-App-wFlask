Hey,

To use this project you need to install some packages.

Commands will be for use in the bash terminal:

Installing Basic Packages Required:
  Installing requests (requests handles API and HTTP requests and is used to retrieve data from websites in general.)
  Installing python-dotenv (python-dotenv  loads environment variables from a .env file into a Python application, making it easy to manage configuration settings like API keys, database credentials, and other sensitive information.)
  Installing Flask (Flask is a lightweight web framework for building web applications in Python. It provides the tools and libraries to handle routing, templates, and HTTP requests, making it easy to create web services and APIs.)
 
 Installing all of them can be done on 1 line.                   
    >>>>           pip install requests python-dotenv Flask


Install Waitress for a production server
    >>>            pip install waitress

Common Q&As
      What is the difference between Flask and Requests?
        Flask handles your own web application's backend (internal) such as redirecting web pages or receiving API data, and requests allow you to interact with external services, such as making API calls.
        Both can work together, where Flask serves your app and requests fetch data or interact with other services.
        Flask also comes with a development server.


                    
Virtual Environment:
create a new virtual environment: py -m venv .venv
activate the virtual environment: source .venv/Scripts/activate

NOTE:
A virtual environment is used to create an isolated space for Python projects. This allows you to install specific packages and dependencies without affecting the system-wide Python installation or other projects.
