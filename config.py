import os

class Config(object):
    #special key that is used to protect the data transfer. Use that key to check against the cookie file.
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    
    MONGODB_SETTINGS = { 
        'db' : 'UTA_Enrollment'
        # ,'host' : 'mongodb://localhost:27017/UTA_Enrollment'
    }

