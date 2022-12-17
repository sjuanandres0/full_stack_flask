import os

class Config(object):
    #special key that is used to protect the data transfer. Use that key to check against the cookie file.
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_string"
    
