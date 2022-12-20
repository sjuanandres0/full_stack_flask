# Full Stack Web Development with Flask
* https://www.linkedin.com/learning/full-stack-web-development-with-flask/
> Notes taken during the course.

### 1. Setting up the environment.
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

### 2. Creating a Flask Project
#### 2.1 Creating th enrollment application
#### 2.2 Running and configuring the development server
#### 2.3 Creating the homepage
16. Creating the template for the home (index.html).
17. Importing the render_template function
18. Using Jinja template expression
19. Using the include directive to include external files.

#### 2.4 Creating navigation links and route patterns
20. Creating navigation menus
21. Using the url_for function to resolve links
22. Using the route() decorator to bind a function to one or more URL patterns
23. Jinja delimiters
24. Jinga if statement.
> url_for('index') returns the template for that function defined in route. Good practise to avoid defining it everywhere. 

### 3. Working with Templates
#### 3.1 Creating the base template
25. The Jinja template inheritance logic
26. Creating the base template
27. Using template inheritance to create child templates
28. Passing data to the view using props
29. Accessing data via de the request and response objects
> {{ self.content() }} to render again a block

#### 3.2 Creating child templates

#### 3.3 Passing data to the view
30. Passing data from the source to the view
31. Highlighting the active menu item
32. Using For directive
33. Building the course table with JSON data
>    courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

#### 3.4 Accesing data via request and response objects
34. URL variables
35. HTTP Methods (GET, POST)
36. The global objects: Request and Response
37. Requests and response are all JSON API format
![GET and POST](screenshots/GET_POST.png)

#### 3.5 URL Variables
1. Routing parameters
2. Creating a URL variable
3. Setting default data to a URL variable
4. Passing a URL variable to a template


