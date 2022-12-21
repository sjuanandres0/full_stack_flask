# Full Stack Web Development with Flask

**[LinkedIn Learning: Full Stack Web Development with Flask](https://www.linkedin.com/learning/full-stack-web-development-with-flask/)**

Stacks: `Flask`, `MongoDB`, `HTML`, `CSS`, `Bootstrap`

*`Notes taken during the course`*

---

## 1. Setting up the environment.
1. Create virtual environment. VENV already installed.
2. Create venv. Terminal: 
> py -m venv venv
3. Activate venv. Terminal: 
> venv\Scripts\activate
4. Install Flask. Terminal: 
> pip install flask 
5. Install Flask WTF. Terminal: 
> pip install flask-wtf
6. .flaskenv: FLASK_ENV=development, FLASK_APP=main.py
7. Install python-dotenv. Termianl: 
> pip install python-dotenv
8. Deactivate the environment. Termianal: 
> deactivate
9. Freeze requirements. Terminal:
> pip freeze > requirements.txt
10. Install requirements. Terminal:
> pip install -r requirements.txt
11. Run flask app. Terminal:
> flask run
12. __init__.py will be the initialization file. By default the app will look for this file to run it.
13. Creating a config.py module.
14. Creating a routes.py module for all routing patterns.
15. Modifying the __init__.py

---

## 2. Creating a Flask Project
#### 2.1 Creating th enrollment application
#### 2.2 Running and configuring the development server
#### 2.3 Creating the homepage
1. Creating the template for the home (index.html).
2. Importing the render_template function
3. Using Jinja template expression
4. Using the include directive to include external files.

#### 2.4 Creating navigation links and route patterns
1. Creating navigation menus
2. Using the url_for function to resolve links
3. Using the route() decorator to bind a function to one or more URL patterns
4. Jinja delimiters
5. Jinga if statement.
> url_for('index') returns the template for that function defined in route. Good practise to avoid defining it everywhere. 

---

## 3. Working with Templates
#### 3.1 Creating the base template
1. The Jinja template inheritance logic
2. Creating the base template
3. Using template inheritance to create child templates
4. Passing data to the view using props
5. Accessing data via de the request and response objects
> {{ self.content() }} to render again a block

#### 3.2 Creating child templates

#### 3.3 Passing data to the view
1. Passing data from the source to the view
2. Highlighting the active menu item
3. Using For directive
4. Building the course table with JSON data
>    courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

#### 3.4 Accesing data via request and response objects
1. URL variables
2. HTTP Methods (GET, POST)
3. The global objects: Request and Response
4. Requests and response are all JSON API format
![GET and POST](screenshots/GET_POST.png)

#### 3.5 URL Variables
1. Routing parameters
2. Creating a URL variable
3. Setting default data to a URL variable
4. Passing a URL variable to a template

#### 3.6 Working with the GET method
1. Creating the enrollment form using GET method
2. Creating the enrollment template
3. Creating the enrollment route (URL pattern)
4. Accessing form data via the GET method

#### 3.7 Working with the POST method
1. Updating the enrollment form using POST method
2. Adding the GET and POST methods to the route
3. Accessing form data using the form object

#### 3.8 Sending a JSON response
1. The Response Object
2. Creating two APIs to send JSON response
> Everything that comes from the URL will always be a string \
> http://127.0.0.1:5000/api/ \
> Inspect + Network \
> ![API Inspect Network](screenshots/api_inspect_network.png)

## 4. Working with Databases
#### 4.1 Installing database systems
1. Installing the MongoDB database system. [MongoDB Community Server](https://www.mongodb.com/try/download/community)
> mongodb://localhost:27017
2. Installing the MongoEngine extension for Flask
> pip list \
> pip install flask-mongoengine
3. Setting up the database
4. Connecting to the database
5. Creating documents and data
6. Creating the data model

#### 4.2 Working with Databases
1. Setting up a MongoDB database
> MONGODB_SETTINGS = { 'db': 'UTA_Enrollment' }
2. Importing the MongoEngine
> From flask_mongoengine import MongoEngine
3. Initializing the database object
> db = MongoEngine() \
> db.init_app(app)


<br/>
<br/>

---
## Useful Links
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Shortcut to preview .md file in Visual Studio Code: Cntrl+Shift+V
