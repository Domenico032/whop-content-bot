from scripts import download_from_drive as step1
from script import post_to_instagram as step2
from script import submit_to_whop as step3
import os

def main():
    print("🚀 Avvio Whop Content Bot...")
    os.makedirs("videos/queue", exist_ok=True)

    video = step1.download_latest_video()
    if not video:
        print("⛔ Nessun video da usare. Fine.")
        return

    reel_link = step2.upload_to_instagram(video)
    if not reel_link:
        print("⛔ Errore nel caricamento Reel.")
        return

    step3.submit_to_whop(video, reel_link)
    print("✅ Tutto completato con successo.")

if __name__ == "__main__":
    main()