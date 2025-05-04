import pyrebase
import os 
from decouple import config
from dotenv import load_dotenv


load_dotenv()
# Firebase configuration
firebaseConfig = {
  "apiKey": os.getenv('apiKey'),
  "authDomain": os.getenv('authDomain'),
  "databaseURL":os.getenv('databaseUR') ,
  "projectId": os.getenv('projectId'),
  "storageBucket":os.getenv('storageBucket') ,
  "messagingSenderId": os.getenv('messagingSenderId') ,
  "appId": os.getenv('appId') ,
  "measurementId": os.getenv('measurementId')
};

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

if auth :
  print("🔥 Firebase is connected successfully!")
else:
  print("not connected...")
