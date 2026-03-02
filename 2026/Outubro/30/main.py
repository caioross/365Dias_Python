"""
monitor_espaco_google_drive.py

Script para consultar o espaço restante no armazenamento do Google Drive usando a API do Google Drive.
"""

import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def authenticate_google_drive():
    """
    Autentica o usuário no Google Drive e retorna as credenciais.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_drive_space(creds):
    """
    Obtém o espaço restante no Google Drive usando as credenciais fornecidas.

    Args:
        creds (google.oauth2.credentials.Credentials): Credenciais do Google Drive.

    Returns:
        dict: Dicionário contendo o espaço total e o espaço usado.
    """
    service = build('drive', 'v3', credentials=creds)
    # Call the Drive v3 API
    about = service.about().get(fields="storageQuota").execute()
    quota = about.get('storageQuota', {})
    total_space = quota.get('limit', 0)
    used_space = quota.get('usage', 0)
    return {
        'total_space': total_space,
        'used_space': used_space,
        'free_space': total_space - used_space
    }

def main():
    """
    Função principal que autentica o usuário e exibe o espaço restante no Google Drive.
    """
    creds = authenticate_google_drive()
    space_info = get_drive_space(creds)
    print(f"Total Space: {space_info['total_space']} bytes")
    print(f"Used Space: {space_info['used_space']} bytes")
    print(f"Free Space: {space_info['free_space']} bytes")

if __name__ == '__main__':
    main()