import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# CONFIGURAZIONI
FOLDER_ID   = '18DFHupkYsKHbKnh_tf3ui321Ud8Ghrs8'
SCOPES      = ['https://www.googleapis.com/auth/drive.readonly']
KEY_FILE    = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'service_account.json'))
DESTINATION = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'videos', 'queue'))

# Assicura che esista la cartella di destinazione
os.makedirs(DESTINATION, exist_ok=True)

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

def list_mp4_files(service, folder_id):
    query = f"'{folder_id}' in parents and trashed=false and mimeType='video/mp4'"
    resp = service.files().list(q=query, fields="files(id, name)").execute()
    return resp.get('files', [])

def download_file(service, file_id, filename, dest_folder):
    request = service.files().get_media(fileId=file_id)
    filepath = os.path.join(dest_folder, filename)
    if os.path.exists(filepath):
        return False  # già presente
    fh = io.FileIO(filepath, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.close()
    return True

def main():
    drive = get_drive_service()
    files = list_mp4_files(drive, FOLDER_ID)
    if not files:
        print("Nessun file .mp4 trovato in Drive.")
        return

    for f in files:
        name = f['name']
        print(f"Verifico {name}...")
        try:
            downloaded = download_file(drive, f['id'], name, DESTINATION)
            if downloaded:
                print(f"Scaricato: {name}")
            else:
                print(f"Skip (già esistente): {name}")
        except Exception as e:
            print(f"❌ Errore scaricando {name}: {e}")

if __name__ == "__main__":
    main()
