import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# --- Configurazioni ---
WHOP_LOGIN_URL    = "https://whop.com/login"
WHOP_CONTENT_URL  = "https://whop.com/content-rewards"
LAST_POST_FILE    = os.path.join(os.path.dirname(os.path.dirname(__file__)), "last_post.txt")

# CSS selector (raw string) per i pulsanti e campi di Whop
BTN_INVIA_CANDIDATURA = r"#campaign-detail-container > div.border-stroke.bg-background.absolute.right-0.bottom-0.left-0.flex.items-center.justify-between.gap-2.border-t.p-4 > div.w-full.max-w-\[50\%\].sm\:max-w-52 > button"
BTN_UPLOAD_FILE       = r"#radix-«ru» > form > div.flex.w-full.flex-1.flex-col.gap-4.overflow-y-auto.p-4.pt-2.sm\:pt-4 > div:nth-child(4) > div > button"
INPUT_REEL_LINK       = r"#radix-«ru» > form > div.flex.w-full.flex-col.gap-1 > div > input"
BTN_SUBMIT            = r"#radix-«ru» > form > div.border-stroke.bg-panel-solid.sticky.right-0.bottom-0.left-0.flex.w-full.gap-2.border-t.p-4 > button"

def whop_login(driver):
    """
    Effettua il login a Whop. Attende l'inserimento manuale dell'OTP.
    """
    driver.get(WHOP_LOGIN_URL)
    print("➤ Inserisci username/password e OTP su Whop nella finestra aperta.")
    # Attendi 60 secondi per completare il login + OTP
    time.sleep(60)

def submit_to_whop(driver, video_path, reel_url):
    """
    Carica il video e il link del reel nella sezione 'Invia candidatura'.
    """
    driver.get(WHOP_CONTENT_URL)
    time.sleep(5)

    # 1) Clicca "Invia candidatura"
    driver.find_element(By.CSS_SELECTOR, BTN_INVIA_CANDIDATURA).click()
    time.sleep(2)

    # 2) Carica il file video (.send_keys sul <input type="file">)
    upload_btn = driver.find_element(By.CSS_SELECTOR, BTN_UPLOAD_FILE)
    upload_btn.send_keys(video_path)
    time.sleep(2)

    # 3) Inserisci il link del reel
    reel_input = driver.find_element(By.CSS_SELECTOR, INPUT_REEL_LINK)
    reel_input.send_keys(reel_url)
    time.sleep(1)

    # 4) Clicca "Submit"
    driver.find_element(By.CSS_SELECTOR, BTN_SUBMIT).click()
    time.sleep(3)
    print("✅ Candidatura Whop inviata con successo.")

def main():
    # Leggi ultimo video + link postato
    if not os.path.exists(LAST_POST_FILE):
        print(f"Errore: file {LAST_POST_FILE} non trovato. Esegui prima lo script Instagram.")
        return

    with open(LAST_POST_FILE, "r") as f:
        content = f.read().strip()
    try:
        video_file, reel_link = content.split("|", 1)
    except ValueError:
        print("Errore nel formato di last_post.txt; atteso 'file.mp4|https://...'.")
        return

    # Percorso assoluto del video
    project_root = os.path.dirname(os.path.dirname(__file__))
    video_path = os.path.join(project_root, "videos", "posted", video_file)

    if not os.path.exists(video_path):
        print(f"Errore: video {video_path} non trovato.")
        return

    # Avvia browser
    driver = webdriver.Chrome()
    try:
        whop_login(driver)
        submit_to_whop(driver, video_path, reel_link)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
