# (all’inizio)
from selenium.webdriver.common.by import By

# ...

def post_video(path):
    d = setup_driver()
    # 1) Clicca sul "+" per aprire menu upload
    plus_selector = "#mount_0_0_XJ > div > div > div.x9f619.x1n2onr6.x1ja2u2z >  div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div:nth-child(2) > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xixxii4.x1ey2m1c.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.xg7h5cd.xh8yej3.xhtitgo.x6w1myc.x1jeouym"
    d.find_element(By.CSS_SELECTOR, plus_selector).click()
    time.sleep(2)

    # 2) Seleziona “Reel”
    reel_selector = "#mount_0_0_XJ > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div:nth-child(2) > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xixxii4.x1ey2m1c.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.xn3w4p2 > a:nth-child(1)"
    d.find_element(By.CSS_SELECTOR, reel_selector).click()
    time.sleep(2)

    # 3) Carica il file
    file_input = d.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 ... > button")
    file_input.send_keys(path)
    time.sleep(2)
    # … e via così per gli altri passi
