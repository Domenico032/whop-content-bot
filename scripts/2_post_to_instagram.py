import json, os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

VIDEO_FOLDER = "videos/queue"
COOKIES_FILE = "config/INSTAGRAM_COOKIES.json"
UPLOAD_URL = "https://www.instagram.com/reels/upload"

def upload_to_instagram(video_path):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.instagram.com/")
    time.sleep(3)

    cookies = json.load(open(COOKIES_FILE, "r"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(UPLOAD_URL)
    time.sleep(5)

    try:
        upload_input = driver.find_element(By.XPATH, '//input[@type="file"]')
        upload_input.send_keys(os.path.abspath(video_path))
        print("📤 Video caricato su Instagram.")
        time.sleep(10)  # Attendi l'upload
        caption_area = driver.find_element(By.TAG_NAME, 'textarea')
        caption_area.send_keys("#affiliate #viral #whop")
        driver.find_element(By.XPATH, '//button[text()="Share"]').click()
        print("✅ Reel pubblicato.")
        time.sleep(5)
        profile_url = "https://www.instagram.com/"
        driver.get(profile_url)
        time.sleep(5)
        link = driver.find_element(By.XPATH, '//article//a').get_attribute("href")
        print(f"🔗 Reel link: {link}")
        return link
    except Exception as e:
        print(f"❌ Errore nel caricamento su Instagram: {e}")
        return None
    finally:
        driver.quit()

if __name__ == "__main__":
    files = os.listdir(VIDEO_FOLDER)
    if not files:
        print("❌ Nessun video da caricare.")
    else:
        video_path = os.path.join(VIDEO_FOLDER, files[0])
        upload_to_instagram(video_path)
