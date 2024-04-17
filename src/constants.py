import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = "token.pickle"

def generate_credentials():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def get_authenticated_service():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "rb") as token:
            credentials = pickle.load(token)
    else:
        credentials = generate_credentials()
        with open(CREDENTIALS_FILE, "wb") as token:
            pickle.dump(credentials, token)

    return build("drive", "v3", credentials=credentials)