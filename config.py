import os

class Config(object):
    #special key that is used to protect the data transfer. Use that key to check against the cookie file.
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xba\x191U7R2\xc6m\x85\x03\x8f\x8e\x0cL#'
    
    MONGODB_SETTINGS = { 
        'db' : 'UTA_Enrollment'
        # ,'host' : 'mongodb://localhost:27017/UTA_Enrollment'
    }

