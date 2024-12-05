import requests
import time

# Ganti dengan API Key Anda
API_KEY = "b7c4eea584b727d49c16e7e8f7b558a3"

# Contoh: Mengirim reCAPTCHA v2 dummy (harus disesuaikan dengan kasus nyata)
def send_dummy_captcha(api_key):
    payload = {
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': '6Lc_aCMTAAAAABxJvxCz6uM8M4fGr4lVo7Mzk1A4',  # Contoh site key
        'pageurl': 'https://www.google.com/recaptcha/api2/demo'  # Contoh URL
    }

    response = requests.post("http://2captcha.com/in.php", data=payload)
    if "OK" in response.text:
        task_id = response.text.split('|')[1]
        print(f"Tugas Terkirim. ID Tugas: {task_id}")
        return task_id
    else:
        print(f"Gagal mengirim tugas captcha: {response.text}")
        return None

def check_captcha_result(api_key, task_id):
    while True:
        res = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={task_id}&json=1")
        result = res.json()

        if result.get('status') == 1:
            captcha_text = result.get('request')
            print(f"Captcha Selesai: {captcha_text}")
            return captcha_text
        elif result.get('request') == "CAPCHA_NOT_READY":
            print("Captcha belum siap, menunggu 5 detik...")
            time.sleep(5)
        else:
            print(f"Terjadi kesalahan: {result.get('request')}")
            return None

if __name__ == "__main__":
    task_id = send_dummy_captcha(API_KEY)
    if task_id:
        captcha_result = check_captcha_result(API_KEY, task_id)
        if captcha_result:
            print(f"Hasil Captcha: {captcha_result}")
