# Minpro-2-DDP-ProgramPemesananMakanan

### Nama = Muhammad Royyan Mubarrok

### NIM = 2609116005

### Kelas = A

# PROGRAM PEMESANAN MAKANAN

Di Program Saya Sebelum nya Saya membuat Program Pemesanan online, Dan Sekarang saya membuat Menjadi program pesanan nya bisa diakses oleh admin dan pembeli,di menu admin bisa menambahkan  pesanan dan menghapus pesanan, kalau pembeli buat untuk pesan makanan dan bisa juga menghapus pesanan yang sudah dipesan

## 1. Penjelasan Kode Program

#### A. Membuat function Dan dictionary

<img width="528" height="278" alt="image" src="https://github.com/user-attachments/assets/bf43bb60-7ed2-40c4-8687-6760239ff71b" />

Penjelelasan: Disini Saya Menggunakan 3 Library Yaitu PrettyTable,Pwinput, dan OS. Prettytable untuk bikin table di pesanan biar keliatan rapi outputnya, OS Untuk Membersihkan Layar Terminal, dan Pwinput Untuk Memasukkan Password tidak Keliatan. Lalu ada 2 dictionary ysng pertama users dan yang kedua Daftar_makanan

<img width="606" height="315" alt="Screenshot 2026-10-05 204109" src="https://github.com/user-attachments/assets/893fe397-1826-4931-84d5-c7ddfa2aa4fa" />

Function yang pertama Yaitu bersihkan_layar yang dimana untuk membersihkan Tamoilan teks di terminal agar Terlihat Tetap rapi, Lalu Function Yang kedua Tampilkan_Daftar_makanan Yang dimana isinya ada Prettytable agar menjadi tabel terlihat Rapi dan juga ada alignment yang dimana mengatur teks jadisebelah kiri/kanan, lalu ada for key stv variable perulangan yang digunakan untuk mengakses dictionary

<img width="449" height="252" alt="Screenshot 2026-10-05 205945" src="https://github.com/user-attachments/assets/d17fb9ca-8e12-4782-871e-185f5a4508e5" />

Di system utama ini yaitu Login dimana bertugas Melakukan verifikasi pengguna sebelum masuk ke aplikasi, ada bersihkan_layar agar terilaht rapi di terminal tidak behamburan, lalu username input untuk menginput nama pengguna,lalu ada password pwinput yang dimana ketika memasukkan password tidak keliatan dan disamarkan manggunakan * untuk keamanan, dan kalau if username in users buat memeriksa apakah username ada di dalam dictionary users begitu juga dengan password, lalu ada bagian else jika username dan password salah sistem akan menampilkan "Username Dan Password Salah!", lalu tekan enter untuk mengulanginya lagi

#### B. Menu Admin dan Users 

<img width="385" height="413" alt="Screenshot 2026-10-05 212153" src="https://github.com/user-attachments/assets/2e83bc12-af31-4dc6-90ac-104939ca16ec" />
<img width="298" height="164" alt="Screenshot 2026-10-05 212206" src="https://github.com/user-attachments/assets/53b10191-b03e-43cb-bc19-8cf4273ba564" />

Disini saya Menmpilkan menu admin yang dimana masi menggunakan while true. 1. Menampilkan Daftar pesanan saja lalu tekan enter untuk kembali ke menu yang ke 2. yang kedua ini menambahkan menu baru yang dimana kita memakai nama, kategori dan harga, new_id itu untuk biarpesanan menjadi nomor lalu diakhirnya ada + 1 biar tidak mengulang jadi 1 lagi dan except error yang dimana kita harus memaukkan berupa angka kalau huruf tidak bisa diakses pengguna dipakaasa untuk memasaukkan angka, lalu yang 3 yaitu mengubah menu, tampilkan daftar pesanan lalu key = intput peesanan yang ingin diubah lalu memasukkan menu baru nama,kategori, dan harga. pesanan berhasil dirubah, 4. menghapus menu pesanan, menampilkan pesanan lalu pilih pesanan yang ingin dihapus menggunakan daftar_makanan.pop untuk menghapus makanan. 5. Logout  keluar dari menu admin

<img width="352" height="396" alt="Screenshot 2026-10-05 215839" src="https://github.com/user-attachments/assets/baf40c28-ef75-4c3c-a48c-7ace76c79e11" />
<img width="347" height="223" alt="Screenshot 2026-10-05 220118" src="https://github.com/user-attachments/assets/acdd815f-bead-410c-8f9a-ecd5506e5254" />

Disini ada juga menampilkan menu users yang dimana juga menggunakan while true. 1.Menambah Pesanan, yang dimana kita memesan suaatu makanan yang telah kita pesan lalu menampilkan pesanan berhasil ditambahkan 2.mengubah pesanan yang dimana saya memakai jika pesanan itu tidak ada maka menampilkan "pesanan Masih kosong" lalu jika ada saya memakai prettytable agar keliatan rapi lalu silahkan pilih pesanan yang ingin diubah menggunakan wha =, lalu memilih pesanan pilih pesanan pengganti if makanan_baru in Daftar_Makanan dan Pesanan berhasil berubah. 3.menghapus Pesanan disini kita disuru memilih pesanan yang ingin dihapus yang sudah kita pesan lalu saya menggunakan pop. 4. selesai dan pembayaran, disini kita melanjutkan proses selanjutnya yaitu pembayaran maka selesai.

#### C. Proses Pembayaran dan main

<img width="352" height="304" alt="Screenshot 2026-10-05 221259" src="https://github.com/user-attachments/assets/65c2b136-cc81-4faa-83bb-e795997db917" />

Dari Proses ini saya menampilkan pesanan yang sudah dipesan, lalu users ditanya untuk member ya atau tidak jika ya maka mendapatkan diskon 10 persen jika tidak maka tidak dapat persen, lalu menampilkan total semua harga dan berapa harga diskon dikurangin dengan harga total lalu dijumlahkan semua maka selesai

<img width="248" height="161" alt="image" src="https://github.com/user-attachments/assets/d41fd16d-e538-4f6d-8f88-42a2b8c78328" />

Disini adalah fungsi main yang mengontrol alur jalannya  seluruh aplikasi dari awal hingga selesai,while True:: Looping utama agar aplikasi terus berjalan atau berulang sampai pengguna memilih untuk keluar (exit). if __name__ == "__main__": main(): Menjadikan fungsi main() sebagai titik awal eksekusi ketika file Python ini dijalankan langsung.

## 2. OUTPUT

#### A. ADMIN

<img width="197" height="65" alt="image" src="https://github.com/user-attachments/assets/c40fb85f-409d-4f00-bc4c-ecca9bc854bc" />

Login Sebagai admin

<img width="233" height="219" alt="image" src="https://github.com/user-attachments/assets/ca02e4e4-d64f-4a8b-915d-2d65112e6fe2" />

Menu 1 Menampilkan Daftar Menu + Penceet enter Untuk Kembali

<img width="259" height="254" alt="image" src="https://github.com/user-attachments/assets/74f82571-c5c1-4951-ae50-54efb916ae53" />

menu 2 Untuk Menambahkan Daftar menunya

<img width="224" height="223" alt="image" src="https://github.com/user-attachments/assets/63d63ee0-47cd-4db7-aa13-fd567004da54" />

ini Tampilan Bahwa Menu baru berhasil ditambahkan 

<img width="308" height="274" alt="image" src="https://github.com/user-attachments/assets/d6810c51-255e-4fb2-b5c3-063080687c64" />

Menu 3 Untuk Mengubah daftar manu + Memasukkankan menu baru

<img width="226" height="223" alt="image" src="https://github.com/user-attachments/assets/d6d7dde8-30f8-4b11-8e7f-3190abce70b1" />

Tampilan Menu Berhasil Berubah

<img width="257" height="230" alt="image" src="https://github.com/user-attachments/assets/59f1a597-37d5-4a06-aa5d-389f609270c7" />

Menu 4 Untuk Menghapus Pesanan

<img width="251" height="210" alt="image" src="https://github.com/user-attachments/assets/971c6266-21e0-4405-bfe8-32cde5709f52" />

Tampilan berhasil Dihapus

<img width="249" height="114" alt="image" src="https://github.com/user-attachments/assets/d9b8c318-ebd4-4162-994e-ddd8dd7225d8" />

Menu 5 Logout, ketik y untuk Login Kembali, Atau n untuk keluar

#### B. USERS

<img width="206" height="65" alt="image" src="https://github.com/user-attachments/assets/b2fbaf03-3a7e-457a-8e53-c17192ef5d8e" />

Login Sebagai User

<img width="274" height="216" alt="image" src="https://github.com/user-attachments/assets/fcecfe99-9f8a-45a9-8746-fefda97e44f3" />

Menu 1 Menambahkan Pesanan + data yang dimasukkan oleh admin masih tersimpan jika sebelumnya logout dari role admin.

<img width="301" height="406" alt="image" src="https://github.com/user-attachments/assets/d30f4969-ff27-4af1-81e9-94dd01d47786" />

Menu 2 Mengubah pesanan yang sudah di pesan 

<img width="278" height="281" alt="image" src="https://github.com/user-attachments/assets/01d7d34c-732d-4dab-b437-06da4fa51ad2" />

Menu 3 Menghapus Pesanan yang sudah Pesanan

<img width="258" height="162" alt="image" src="https://github.com/user-attachments/assets/2a381130-0da3-4db1-89d6-71243e5a8601" />

Menu 4 Selesai Dan Bayar +menampilkan semua pesanan yang sudah dipesan + pengguna apakah member atau tidak jika member maka di beri 10% diskon + maka seelesai logout lalu pengguna "jika menginput "y" maka akan masuk ke proses login lagi"

#### C. try except Value Error

<img width="221" height="113" alt="image" src="https://github.com/user-attachments/assets/93606a84-d9a7-4ced-9b28-30d46b3b40de" />

Penjelasan: jika saya menginput huruf di situ, maka akan ada pringatan "harus berupa angka" dan terjadi pengulangan bukan crash/error.


## 3.PENJELASAN FLOWCHART

#### A.LOGIN

<img width="338" height="243" alt="image" src="https://github.com/user-attachments/assets/2065358a-7bf5-49f4-bf4b-1f4393ca6e67" />

Penjelasan: input username dan password, menggunakan decision pertama untuk mengecek apakah usn dan pw benar, lalu lanjut pengecekan role bisa nasuk ke admnin atau users, lalu jika pw dan username salah maka silahkan tekan enter untuk mengulangi

#### 1. MENU ADMIN

<img width="266" height="277" alt="image" src="https://github.com/user-attachments/assets/c3449b98-708b-447e-9a75-37e7482ad17e" />\

Penjelas sesuai dengan program, input 1 = Melihat daftar menu, input 2 = Menambah menu, input 3 = ubah Menu, input 4 = hapus Menu, untuk pilihan 1-4 mereka akan kembali lagi ke menu admin ketik enter untuk melanjutkan input pilihan lagi. Namun jika input 5 maka langsung lanjut ke input "kembali ke halaman login lagi?" y/n.

#### 2.MENU USERS

<img width="438" height="238" alt="image" src="https://github.com/user-attachments/assets/5e1ac89d-9fbf-4b3e-8d68-bbd785834020" />

Penjelasan Sesuai dengan Program, input 1 + Menambah Pesanan, input 2 = Mengubah Pesanan, input 3 = Menghapus Pesanan, input 4 =  Selesai dan Bayar, untuk pilihan 1-3 mereka akan kembali ke menu users ketik enter untuk melanjutkan input pilihan lagi, namun jika 4 maka dikasih decision yang dimana "apakah member ya/tidak" jika maka mendapatkan diskon 10% jika tidak langsung lanjut input "kembali ke halaman login lagi?" y/n.



















