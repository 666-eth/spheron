# 🔄 Spheron Auto Spin Bot

Skrip Python untuk mengotomatiskan proses **spin harian di Spheron** (`https://tge.spheron.network/api/user/spin`) setiap 24 jam, untuk banyak akun secara bersamaan, menggunakan `spheron.sid` dari file `sid.txt`.

---

## ✨ Fitur Utama

- 🔁 Spin otomatis setiap 24 jam untuk seluruh akun
- 📝 Logging hasil ke `spheron.log`
- ⏱️ Delay 2 detik antar akun untuk menghindari rate limit
- 🔧 Bisa berjalan di latar belakang menggunakan `tmux`

---

## 🧰 Persyaratan

- **Termux** (disarankan dari F-Droid)
- **Python** 3.7+
- **Git** & **tmux**
- **Koneksi internet stabil**
- **Cookie `spheron.sid`** dari akun masing-masing

---

## 🚀 Cara Penggunaan

### 1. Kloning Repositori
```bash
git clone https://github.com/daimun29/spon.git
cd spon
````

### 2. Siapkan Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
pip install requests schedule
```

### 3. Buat File `sid.txt`

```bash
nano sid.txt
```

Masukkan satu `spheron.sid` per baris:

```
s%3Aig3o5xyhAd8ENAVnJ9nyiNPSLfbZixT6.WjjJ0358gGRf2hbnO2VHInz62fvC4tQQIcnZESBy
s%3A<cookie_akun_2>
```

> 💡 **Cara mendapatkan cookie:**
>
> * Login ke [Spheron](https://tge.spheron.network/missions)
> * Tekan `F12` → buka tab **Network**
> * Lakukan spin manual
> * Cari cookie `spheron.sid` di header permintaan

---

### 4. Jalankan Skrip dengan `tmux`

```bash
pkg install tmux  # jika belum terpasang
source venv/bin/activate
tmux new -s dst
python spheron_spin.py
```

* Keluar dari `tmux`: `Ctrl + B`, lalu tekan `D`
* Masuk kembali ke sesi: `tmux attach -t dst`

---

## 📄 Log dan Troubleshooting

* Periksa log:

  ```bash
  nano spon
  cat spheron.log
  ```
* Contoh log:

  ```
  2025-05-24 01:26:00 - INFO - Spin berhasil untuk akun 1: {...}
  ```

### ❗ Mengatasi Error

* **401: Authentication Required**

  * Penyebab: Cookie tidak valid atau kedaluwarsa
  * Solusi: Perbarui cookie di `sid.txt`

* **File `sid.txt` tidak ditemukan**

  * Pastikan file berada di direktori yang sama dan tidak kosong

* **Skrip berhenti tiba-tiba**

  * Nonaktifkan optimasi baterai Termux di pengaturan Android
  * Cek sesi `tmux`: `tmux attach -t dst`

---

## 🕒 Catatan

* Perbarui `sid.txt` secara berkala jika cookie kedaluwarsa
* Gunakan waktu lokal Termux (misal: WIB)
* Untuk otomatisasi login lebih lanjut, gunakan Selenium (kontak kontributor)

---

## 🤝 Kontribusi

Pull request sangat diterima!
Fork repositori di:
🔗 [https://github.com/daimun29/spon](https://github.com/daimun29/spon)

---

## 📄 Lisensi

MIT License

---

```
