import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

FOLDER_ID = "18DFHupkYsKHbKnh_tf3ui321Ud8Ghrs8"
SAVE_PATH = "videos/queue"

def download_latest_video():
    creds = service_account.Credentials.from_service_account_file("config/service_account.json")
    service = build("drive", "v3", credentials=creds)
    results = service.files().list(
        q=f"'{FOLDER_ID}' in parents and mimeType contains 'video/'",
        orderBy="createdTime desc",
        pageSize=1
    ).execute()
    files = results.get("files", [])
    if not files:
        print("❌ Nessun video trovato su Drive.")
        return None

    file = files[0]
    file_id = file["id"]
    file_name = file["name"]
    save_path = os.path.join(SAVE_PATH, file_name)

    if os.path.exists(save_path):
        print(f"⚠️ {file_name} già presente.")
        return save_path

    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(save_path, "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    print(f"✅ Video scaricato: {file_name}")
    return save_path

if __name__ == "__main__":
    os.makedirs(SAVE_PATH, exist_ok=True)
    download_latest_video()

if __name__ == "__main__":
    main()
