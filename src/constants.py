import os

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = "token.json"

def generate_credentials():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def get_authenticated_service():
    cred = None
    if os.path.exists(CREDENTIALS_FILE):
        cred = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            cred = generate_credentials()

        with open(CREDENTIALS_FILE, "w") as token:
            token.write(cred.to_json())

    return build("drive", "v3", credentials=cred)