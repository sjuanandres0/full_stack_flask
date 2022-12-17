# Full Stack Web Development with Flask
* https://www.linkedin.com/learning/full-stack-web-development-with-flask/

## Setting up the environment.
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

