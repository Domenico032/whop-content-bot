from scripts import download_from_drive as step1
from scripts import post_to_instagram as step2
from scripts import submit_to_whop as step3

if __name__ == "__main__":
    print("🚀 Avvio processo automatico Whop Content Bot...")
    step1.main()
    step2.main()
    step3.main()
    print("✅ Tutte le operazioni completate.")
