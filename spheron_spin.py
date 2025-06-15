import requests
import time
import logging

# Pengaturan logging ke file
logging.basicConfig(filename='spheron.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fungsi untuk membaca cookies dari file sid.txt
def load_cookies(file_path="sid.txt"):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        logging.error("File %s tidak ditemukan!", file_path)
        return []
    except Exception as e:
        logging.error("Error saat membaca %s: %s", file_path, str(e))
        return []

# Fungsi untuk melakukan spin untuk satu cookie
def spin_for_account(spheron_sid, account_index):
    logging.info("Menggunakan cookie untuk akun %d: %s", account_index, spheron_sid)
    url = "https://tge.spheron.network/api/user/spin"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://tge.spheron.network",
        "priority": "u=1, i",
        "referer": "https://tge.spheron.network/missions",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
    }
    cookies = {
        "_ga_QGP7CXNREE": "GS2.1.s1748022379$o1$g0$t1748022379$j0$l0$h0",
        "_ga": "GA1.1.1937733712.1748022380",
        "spheron.sid": spheron_sid
    }
    payload = {}

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=payload)
        if response.status_code == 200:
            logging.info("Spin berhasil untuk akun %d: %s", account_index, response.json())
            print(f"Spin berhasil untuk akun {account_index}: {response.json()}")
        else:
            logging.error("Spin gagal untuk akun %d, status %s: %s", 
                         account_index, response.status_code, response.text)
            print(f"Spin gagal untuk akun {account_index}, status {response.status_code}")
    except Exception as e:
        logging.error("Error saat spin untuk akun %d: %s", account_index, str(e))
        print(f"Error saat spin untuk akun {account_index}: {str(e)}")

# Fungsi untuk melakukan spin untuk semua akun
def spin_all_accounts():
    cookies = load_cookies()
    if not cookies:
        logging.error("Tidak ada cookie yang ditemukan untuk spin.")
        print("Tidak ada cookie yang ditemukan untuk spin.")
        return
    for index, spheron_sid in enumerate(cookies, 1):
        logging.info("Memproses spin untuk akun %d", index)
        print(f"Memproses spin untuk akun {index}")
        spin_for_account(spheron_sid, index)
        time.sleep(2)  # Jeda 2 detik antar akun

# Langsung jalankan sekali
spin_all_accounts()

print("Semua spin selesai.")
