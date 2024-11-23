from firebase_admin import credentials
import firebase_admin
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables for Firebase credentials
private_key = os.getenv('FIREBASE_PRIVATE_KEY').replace("\\n", "\n")
project_id = os.getenv('FIREBASE_PROJECT_ID')
client_email = os.getenv('FIREBASE_CLIENT_EMAIL')
private_key_id = os.getenv('FIREBASE_PRIVATE_KEY_ID')
client_x509_cert_url = os.getenv('FIREBASE_CLIENT_X509_CERT_URL')

# Firebase-specific URIs
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"

# Initialize Firebase App
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate({
            "type": "service_account",
            "project_id": project_id,
            "private_key_id": private_key_id,
            "private_key": private_key,
            "client_email": client_email,
            "auth_uri": auth_uri,
            "token_uri": token_uri,
            "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
            "client_x509_cert_url": client_x509_cert_url,
        })
        firebase_admin.initialize_app(cred)
        print("Firebase app initialized successfully.")
    except Exception as e:
        print("Error initializing Firebase app:", e)
