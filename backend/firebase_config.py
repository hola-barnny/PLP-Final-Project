import firebase_admin
from firebase_admin import credentials

# Path to the Firebase Admin SDK credentials JSON file
cred = credentials.Certificate("firebase-adminsdk.json")

# Initialize the Firebase Admin SDK
firebase_admin.initialize_app(cred)
