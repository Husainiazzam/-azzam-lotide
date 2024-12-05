import requests
import time

API_KEY = "b7c4eea584b727d49c16e7e8f7b558a3"

def send_captcha(api_key, site_key, page_url):
    payload = {
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': page_url,
    }

    response = requests.post("http://2captcha.com/in.php", data=payload)
    if "OK" in response.text:
        task_id = response.text.split('|')[1]
        print(f"Tugas dikirim. ID Tugas: {task_id}")
        return task_id
    else:
        print(f"Gagal mengirim captcha: {response.text}")
        return None

def get_captcha_result(api_key, task_id):
    while True:
        response = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={task_id}&json=1")
        result = response.json()

        if result.get('status') == 1:
            return result.get('request')  # Hasil captcha
        elif result.get('request') == "CAPCHA_NOT_READY":
            print("Captcha belum siap, menunggu...")
            time.sleep(5)  # Tunggu sebelum mencoba lagi
        elif result.get('request') == "ERROR_CAPTCHA_UNSOLVABLE":
            print("Captcha tidak dapat diselesaikan. Mengirim ulang captcha...")
            return "CAPTCHA_UNSOLVABLE"
        else:
            print(f"Terjadi kesalahan: {result.get('request')}")
            return None

# Contoh penggunaan
if __name__ == "__main__":
    SITE_KEY = "6Lc_aCMTAAAAABxJvxCz6uM8M4fGr4lVo7Mzk1A4"
    PAGE_URL = "https://www.google.com/recaptcha/api2/demo"

    task_id = send_captcha(API_KEY, SITE_KEY, PAGE_URL)
    if task_id:
        captcha_result = get_captcha_result(API_KEY, task_id)
        if captcha_result == "CAPTCHA_UNSOLVABLE":
            print("Coba kirim ulang captcha atau periksa pengaturan.")
        elif captcha_result:
            print(f"Hasil Captcha: {captcha_result}")
