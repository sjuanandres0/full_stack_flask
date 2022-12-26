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

---

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

#### 4.3 Connecting to the database
1. Connecting to the MongoDB via the MongoEngine object
2. Hooking up a user collection using a simple user model class
3. Inserting sample user document (data) to a collection
4. Displaying the collection to the view

#### 4.4 Creating documents and data
1. Creating collections to store documents (data)
2. Inserting documents into our collections
3. Using MongoDB shell commands
> db.createCollection( `collection` ) \
> db.`collection`.insert( { ... } ) \
> db.`collection`.insertMany( { ... } )
4. Inserting JSON data using the mongoimport.exe via command line
> mongoimport --db `DB` -collection `collection` --file `file` \
> mongoimport -d `DB` -c `collection` --file `file`
https://www.mongodb.com/docs/database-tools/mongoimport/

#### 4.5 Creating the data models
1. Creating the models module
2. Creating the **User** model
3. Creating the **Course** model
4. Creating the **Enrollment** model
> class ModelName(db.Document): \
>   field1 = db.IntField() \
>   field2 = db.StringField() \
>   ... \
>   fieldn = db.StringField()

---

## 5. Working with Web Forms and Flask-Security
#### 5.1. Installation and configuration
1. Installing and configuring Flask-WTF (Web Template Form) amd Flask-Security extensions
2. Creating the login and registration pages
3. Processing form data and updating the database
4. Creation the courses and enrollment pages
5. Creating sessions and authentication
![Flask-WTF Extension](screenshots/Flask-WTF_Extension.png)
> pip install flask-wtf flask-security 

#### 5.2. Creating the login and registration pages
1. Creating the login and registration pages
2. Creating form classes and updating the templates using WTForms librarie
3. Creating alert messages using the flash() method

#### 5.3. Updating the login route and ogin template
1. Updating the login route to capture form data
2. Updating the login template using WTForms library

#### 5.4. Flashing messages
1. Creating alert messages using the flash() method (source)
2. Retrieving flash messages suing the get_flashed_mesages() (view)

#### 5.5. Displaying form validation error messages
1. Validating form data
2. Showing inline error messages fo form fields
3. Styling and formatting error messages

#### 5.6. Processing form data and updating the database
1. Form data validation
2. Processing form data for database update
3. Hashing password using Werkzeug library (a WSGI web application library)
> `Hashing`: generate_password_hash('password') \
> `Unhashing`: check_password_hash(password, 'password')

#### 5.7. Updating login route to interact with database
1. Form data validation
2. Validatin email addresses
3. Hashing password using Werkzeug library (a WSGI web application library)
> `Hashing`: generate_password_hash('password') \
> `Unhashing`: check_password_hash(password, 'password')

#### 5.8. Updating registration route to interact with database
1. Validating form data
2. Hashing password using Werkzeug library (a WSGI web application library)
3. Inserting data into the database
4. Verifying data in the database using Compass interface

#### 5.9. Creating the courses page
1. 



<br/>
<br/>

---
## Useful Links
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Shortcut to preview .md file in Visual Studio Code: Cntrl+Shift+V
