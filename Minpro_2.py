import os
import pwinput
from prettytable import PrettyTable

# -------------------------------------------------------------
# STRUKTUR DATA
# -------------------------------------------------------------
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "royyan": {"password": "user123", "role": "user"}
}

daftar_makanan = {
    1: {"nama": "Mie Gacoan Level 1", "kategori": "makanan", "harga": 12000},
    2: {"nama": "Mie Gacoan Level 2", "kategori": "makanan", "harga": 13000},
    3: {"nama": "Mie Gacoan Level 3", "kategori": "makanan", "harga": 14000},
    4: {"nama": "Udang Keju", "kategori": "makanan", "harga": 10000},
    5: {"nama": "Es Teh", "kategori": "minuman", "harga": 8000}
}

pesanan = []

# -------------------------------------------------------------
# FUNGSI PENDUKUNG
# -------------------------------------------------------------
def bersihkan_layar():
    """Menggunakan library os untuk membersihkan terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_daftar_makanan():
    """Fungsi untuk menampilkan menu yang tersedia menggunakan PrettyTable"""
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Menu", "Kategori", "Harga"]
    
    tabel.align["Nama Menu"] = "l"
    tabel.align["Kategori"] = "l"
    tabel.align["Harga"] = "r"

    for key, val in daftar_makanan.items():
        tabel.add_row([key, val['nama'], val['kategori'].capitalize(), f"Rp{val['harga']:,}"])

    print("\n" + "="*45)
    print("            DAFTAR MENU MAKANAN")
    print("="*45)
    print(tabel)

# -------------------------------------------------------------
# FUNGSI UTAMA: SYSTEM LOGIN
# -------------------------------------------------------------
def login():
    bersihkan_layar()
    print("="*40)
    print("           SYSTEM LOGIN")
    print("="*40)
    username = input("Masukkan Username : ")
    password = pwinput.pwinput("Masukkan Password : ", mask="*")

    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    else:
        print(" Username atau Password salah!")
        input("Tekan Enter untuk mencoba lagi...")
        return None

# -------------------------------------------------------------
# FUNGSI ROLE ADMIN
# -------------------------------------------------------------
def menu_admin():
    while True:
        bersihkan_layar()
        print("="*40)
        print("      MENU ADMIN")
        print("="*40)
        print("1. Lihat Daftar Menu ")
        print("2. Tambah Menu Baru ")
        print("3. Ubah Menu ")
        print("4. Hapus Menu ")
        print("5. Logout")
        
        pilihan = input("Pilih Menu Admin (1-5): ")

        if pilihan == "1":
            tampilkan_daftar_makanan()
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            tampilkan_daftar_makanan()
            nama = input("Masukkan nama menu baru     : ")
            kategori = input("Masukkan kategori (makanan/minuman): ")
            try:
                harga = int(input("Masukkan harga              : "))
                new_id = max(daftar_makanan.keys(), default=0) + 1
                daftar_makanan[new_id] = {"nama": nama, "kategori": kategori, "harga": harga}
                print(f" Menu '{nama}' berhasil ditambahkan!")
            except ValueError:
                print(" Input harga harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "3":
            tampilkan_daftar_makanan()
            try:
                key = int(input("Masukkan ID menu yang ingin diubah: "))
                if key in daftar_makanan:
                    nama = input("Nama Baru    : ")
                    kategori = input("Kategori Baru: ")
                    harga = int(input("Harga Baru   : "))
                    daftar_makanan[key] = {"nama": nama, "kategori": kategori, "harga": harga}
                    print(" Menu berhasil diperbarui!")
                else:
                    print(" ID Menu tidak ditemukan!")
            except ValueError:
                print("Input harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "4":
            tampilkan_daftar_makanan()
            try:
                key = int(input("Masukkan ID menu yang ingin dihapus: "))
                if key in daftar_makanan:
                    removed = daftar_makanan.pop(key)
                    print(f" Menu '{removed['nama']}' berhasil dihapus!")
                else:
                    print(" ID Menu tidak ditemukan!")
            except ValueError:
                print(" Input harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "5":
            break
        else:
            print(" Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

# -------------------------------------------------------------
# FUNGSI ROLE USER
# -------------------------------------------------------------
def menu_user():
    while True:
        bersihkan_layar()
        tampilkan_daftar_makanan()
        print("\nMENU PELANGGAN")
        print("1. Menambah Pesanan")
        print("2. Mengubah Pesanan")
        print("3. Menghapus Pesanan")
        print("4. Selesai & Bayar")

        pilih = input("Pilih menu (1-4): ")

        if pilih == "1":
            try:
                nomor = int(input("Pilih Nomor Menu: "))
                if nomor in daftar_makanan:
                    pesanan.append(daftar_makanan[nomor])
                    print(f" '{daftar_makanan[nomor]['nama']}' berhasil ditambahkan!")
                else:
                    print(" Nomor menu tidak tersedia.")
            except ValueError:
                print(" Masukkan angka yang valid!")
            input("Tekan Enter untuk melanjutkan...")

        elif pilih == "2":
            if not pesanan:
                print(" Pesanan masih kosong.")
            else:
                tabel_pesanan = PrettyTable()
                tabel_pesanan.field_names = ["No", "Nama Pesanan", "Harga"]
                tabel_pesanan.align["Nama Pesanan"] = "l"
                tabel_pesanan.align["Harga"] = "r"
                
                for i, item in enumerate(pesanan, 1):
                    tabel_pesanan.add_row([i, item['nama'], f"Rp{item['harga']:,}"])

                print("\n--- Pesanan Anda Saat Ini ---")
                print(tabel_pesanan)

                try:
                    idx = int(input("Pilih nomor pesanan yang mau diubah: ")) - 1
                    if 0 <= idx < len(pesanan):
                        tampilkan_daftar_makanan()
                        makanan_baru = int(input("Pilih nomor menu pengganti: "))
                        if makanan_baru in daftar_makanan:
                            pesanan[idx] = daftar_makanan[makanan_baru]
                            print(" Pesanan berhasil diubah!")
                        else:
                            print(" Menu baru tidak valid.")
                    else:
                        print(" Nomor pesanan tidak ditemukan.")
                except ValueError:
                    print(" Masukkan angka yang valid!")
            input("Tekan Enter untuk melanjutkan...")

        elif pilih == "3":
            if not pesanan:
                print(" Pesanan masih kosong.")
            else:
                tabel_hapus = PrettyTable()
                tabel_hapus.field_names = ["No", "Nama Pesanan"]
                tabel_hapus.align["Nama Pesanan"] = "l"

                for i, item in enumerate(pesanan, 1):
                    tabel_hapus.add_row([i, item['nama']])

                print("--- Hapus Pesanan ---")
                print(tabel_hapus)

                try:
                    idx = int(input("Masukkan Nomor yang ingin dihapus: ")) - 1
                    if 0 <= idx < len(pesanan):
                        item_dihapus = pesanan.pop(idx)
                        print(f" '{item_dihapus['nama']}' berhasil dihapus.")
                    else:
                        print(" Nomor pesanan tidak ditemukan.")
                except ValueError:
                    print(" Masukkan angka yang valid!")
            input("Tekan Enter untuk melanjutkan...")

        elif pilih == "4":
            proses_pembayaran()
            break
        else:
            print(" Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

# -------------------------------------------------------------
# FUNGSI PEMBAYARAN
# -------------------------------------------------------------
def proses_pembayaran():
    bersihkan_layar()
    print("="*45)
    print("              RINGKASAN PESANAN")
    print("="*45)

    if not pesanan:
        print("Tidak ada pesanan yang diproses.")
        return

    tabel_ringkasan = PrettyTable()
    tabel_ringkasan.field_names = ["No", "Nama Menu", "Harga"]
    tabel_ringkasan.align["Nama Menu"] = "l"
    tabel_ringkasan.align["Harga"] = "r"

    total = 0
    for i, item in enumerate(pesanan, 1):
        tabel_ringkasan.add_row([i, item['nama'], f"Rp{item['harga']:,}"])
        total += item['harga']

    print(tabel_ringkasan)
    print("-" * 45)
    print(f"Total Awal : Rp{total:,}")

    while True:
        member = input("Apakah Anda member? (ya/tidak): ").strip().lower()
        if member in ["ya", "tidak"]:
            break
        print("[!] Jawab dengan 'ya' atau 'tidak'.")

    if member == "ya":
        diskon = total * 0.10
        total_bayar = total - diskon
        print(f"Diskon Member (10%): Rp{int(diskon):,}")
        print(f"Total Bayar        : Rp{int(total_bayar):,}")
    else:
        print(f"Total Bayar        : Rp{total:,}")

    print("Terima kasih sudah memesan!")
    input("Tekan Enter untuk keluar...")

# -------------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------------
def main():
    while True:
        role = None
        while role is None:
            role = login()

        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_user()
        print("Kembali ke halaman login?")
        pilihan = input("Ketik y untuk login kembali, "
                                "atau n untuk keluar: ").lower()
        if pilihan != "y":
                    print("\nTerima kasih telah menggunakan program!")
                    break

if __name__ == "__main__":
    main()