import sys
import os

# Add 'scripts' to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from download_from_drive import step1
from post_to_instagram import step2
from submit_to_whop import step3

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