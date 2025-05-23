Script Python untuk mengotomatiskan spin API Spheron (https://tge.spheron.network/api/user/spin) setiap 24 jam untuk banyak akun menggunakan cookie spheron.sid dari sid.txt. Script dijalankan di Termux dengan tmux untuk operasi di latar belakang.
Fitur
Spin otomatis setiap 24 jam untuk semua akun di sid.txt.
Logging ke spheron.log.
Jeda 2 detik antar akun untuk mencegah rate limiting.
Berjalan di latar belakang dengan tmux.
Prasyarat
Termux: Unduh dari F-Droid.
Python: Versi 3.7+.
Koneksi Internet: Stabil.
Cookie spheron.sid: Untuk setiap akun.
Git dan tmux: Untuk kloning dan latar belakang.
Pengaturan
1. Kloning Repository
bash
git clone https://codeberg.org/daimun/spon.git
cd spon
2. Siapkan Lingkungan Virtual
Buat dan aktifkan venv:
bash
python -m venv venv
source venv/bin/activate
Instal dependensi:
bash
pip install requests schedule
3. Siapkan sid.txt
Buat sid.txt:
bash
nano sid.txt
Tambahkan cookie spheron.sid, satu per baris:
s%3Aig3o5xyhAd8ENAVnJ9nyiNPSLfbZixT6.WjjJ0358gGRf2hbnO2VHInz62fvC4tQQIcnZESBy
s%3A<cookie_akun_2>
Simpan (Ctrl+O, Enter, Ctrl+X).
Mendapatkan Cookie:
Login ke Spheron di browser.
Buka Developer Tools (F12 → Network).
Lakukan spin di https://tge.spheron.network/missions.
Salin spheron.sid dari Request Headers (Cookie).
4. Jalankan Script dengan tmux
Instal tmux:
bash
pkg install tmux
Aktifkan venv:
bash
source venv/bin/activate
Jalankan di sesi tmux bernama dst:
bash
tmux new -s dst python spheron_spin.py
Keluar dari tmux: Ctrl+B, lalu D.
Kembali ke sesi: tmux attach -t dst.
Hentikan: Masuk sesi, Ctrl+C, lalu exit.
5. Periksa Log
Log di spheron.log:
bash
cat spheron.log
Contoh:
2025-05-24 01:26:00 - INFO - Spin berhasil untuk akun 1: {...}
Mengatasi Error
Error 401: Authentication Required
Pesan:
Spin gagal untuk akun 1, status 401: {"message":"Authentication required","type":"authentication_error"}
Solusi:
Perbarui cookie di sid.txt:
Login ke Spheron, salin spheron.sid baru dari Developer Tools.
Uji cookie:
bash
curl -X POST https://tge.spheron.network/api/user/spin -H "Content-Type: application/json" -H "Cookie: spheron.sid=s%3A<cookie_anda>" -d '{}'
Periksa payload/header di Developer Tools, tambahkan ke spheron_spin.py jika perlu:
python
payload = {"user_id": "123"}  # Contoh
headers["Authorization"] = "Bearer <token>"  # Jika diperlukan
File sid.txt Tidak Ditemukan
Pastikan sid.txt ada di direktori spon dan tidak kosong.
Script Berhenti
Nonaktifkan optimasi baterai untuk Termux di pengaturan Android.
Periksa sesi: tmux attach -t dst.
Catatan
Cookie: Perbarui sid.txt jika cookie kedaluwarsa.
Zona Waktu: Gunakan waktu lokal Termux (WIB, 24 Mei 2025, 01:26).
Otomatisasi: Gunakan Selenium untuk login otomatis jika diperlukan (kontak kontributor).
Kontribusi
Fork di https://codeberg.org/daimun/spon.git dan buat pull request untuk perbaikan.
Lisensi
MIT License
Penjelasan
Repository: Diubah ke https://codeberg.org/daimun/spon.git sesuai permintaan.
Singkat: Kode script tidak disertakan, hanya disebutkan sebagai spheron_spin.py.
tmux new -s dst: Digunakan untuk sesi latar belakang, menggantikan screen.
Error 401: Langkah penanganan tetap disertakan.
Jadwal 24 Jam: Script tetap berjalan setiap 24 jam via schedule.every(24).hours.
venv dan Termux: Langkah pengaturan venv dan tmux disertakan secara ringkas.
Untuk Mengunggah ke Codeberg
Simpan README.md dan spheron_spin.py di direktori lokal.
Commit dan push:
bash
git add README.md spheron_spin.py sid.txt
git commit -m "Tambah README dan script auto spin"
git push origin main
