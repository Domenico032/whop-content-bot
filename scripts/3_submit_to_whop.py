import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

VIDEO_FOLDER = "videos/queue"
WHOP_URL_FILE = "config/WHOP_URL.txt"

def submit_to_whop(video_path, reel_url):
    url = open(WHOP_URL_FILE).read().strip()

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)

        file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
        file_input.send_keys(os.path.abspath(video_path))
        print("📎 Video allegato.")

        link_input = driver.find_element(By.XPATH, '//input[@type="url" or @type="text"]')
        link_input.send_keys(reel_url)
        print("🔗 Link incollato.")

        submit_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Invia") or contains(text(), "Submit")]')
        submit_btn.click()
        print("✅ Inviato a Whop.")
    except Exception as e:
        print(f"❌ Errore durante invio a Whop: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    file = os.listdir(VIDEO_FOLDER)[0]
    submit_to_whop(os.path.join(VIDEO_FOLDER, file), "https://instagram.com/...")
