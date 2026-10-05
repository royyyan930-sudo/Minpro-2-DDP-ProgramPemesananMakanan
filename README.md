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








