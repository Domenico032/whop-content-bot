import subprocess

print("Eseguo: Scaricamento da Google Drive")
subprocess.run(["python", "scripts/1_download_from_drive.py"], check=True)

print("Eseguo: Pubblicazione su Instagram")
subprocess.run(["python", "scripts/2_post_to_instagram.py"], check=True)

print("Eseguo: Invio su Whop")
subprocess.run(["python", "scripts/3_submit_to_whop.py"], check=True)
