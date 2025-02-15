# Proyek Manajemen Buku Sederhana
Proyek ini adalah program Python sederhana untuk mengelola daftar buku. Program ini memungkinkan pengguna untuk melihat daftar buku, menghapus buku yang tersedia, dan memvalidasi input pengguna.

## Fitur
  1. Menampilkan daftar buku dalam format tabel menggunakan library tabulate.
  2. Menghapus buku dari daftar berdasarkan indexx.
  3. Validasi Input Pengguna :
     a. Memastikan Index yang dimasukkan valid.
     b. Memastikan buku yang dihapus memiliki status "Tersedia".
  4. Loop untuk menghapus buku lagi atau kembali ke menu utama.
## Sistem peminjaman buku yang telah dibuat memiliki fitur utama sebagai berikut:

1. Peminjaman Buku: Pengguna dapat memilih buku dari daftar dan meminjamnya.
2. Pengembalian Buku: Pengguna dapat mengembalikan buku yang sudah dipinjam.
3. Manajemen Buku: Karyawan dapat menambahkan dan menghapus buku dari sistem.
4. Pencarian Buku Berdasarkan Rak: Pengguna dapat mencari buku sesuai dengan rak tempat penyimpanannya.
5. List Peminjam: Menampilkan daftar pengguna yang telah meminjam buku.
   
## CRUD Fuction 
### 1. Menambahkan data baru ke sistem:
- Menambahkan Buku Baru `(tambah_buku())`:
- Admin dapat menambahkan buku ke daftar buku dengan input judul, penerbit, tahun terbit, dan rak penyimpanan.
- Membuat Data Peminjaman `(pinjam_buku())`:
- Ketika pengguna meminjam buku, data peminjaman mereka dicatat dalam isi_chart dan isi_identitas.
  
### 2. Read (Membaca Data)
Fungsi untuk menampilkan data yang ada:
- Menampilkan Daftar Buku `(tampilkan_daftar_buku())`:
- Menampilkan semua buku yang tersedia di sistem.
- Menampilkan Buku Berdasarkan Rak `(cari_buku())`:
- Pengguna dapat mencari buku berdasarkan rak tertentu.
- Melihat Daftar Peminjam `(tampilkan_peminjam())`:
- Admin dapat melihat siapa saja yang telah meminjam buku.
- Menampilkan Buku yang Dipinjam (pinjam_buku() & kembalikan_buku2()):
- Menampilkan daftar buku yang sedang dipinjam oleh pengguna.
  
### 3. Update (Memperbarui Data)
Fungsi yang mengubah status atau informasi dalam sistem:
- Memperbarui Status Buku saat Dipinjam (pinjam_buku()):
- Saat buku dipinjam, statusnya berubah dari "Tersedia" menjadi "Tidak Tersedia".
- Memperbarui Status Buku saat Dikembalikan (kembalikan_buku2()):
- Setelah buku dikembalikan, statusnya berubah kembali menjadi "Tersedia".
- Mengubah Informasi Buku (bisa ditambahkan sebagai fitur baru)
Jika admin ingin memperbarui informasi buku (misalnya mengganti rak atau penerbit).

### 4. Delete (Menghapus Data)
Fungsi yang menghapus data dari sistem:
- Menghapus Buku dari Daftar (hapus_buku()):
- Admin dapat menghapus buku dari daftar jika tidak diperlukan lagi.
- Menghapus Data Peminjaman saat Buku Dikembalikan (kembalikan_buku2()):
- Buku yang telah dikembalikan dihapus dari isi_chart.
- Menghapus Data Peminjam (bisa ditambahkan sebagai fitur baru)
- Jika ada peminjam yang tidak aktif atau datanya perlu dihapus dari sistem.

## Struktur Data
-  `daftar_buku` (List), Daftar buku dengan header dan data.
- `isi_chart`, (List), Daftar buku dalam format sederhana.
- `isi_identitas`, (List) Daftar identitas peminjam dan buku yang dipinjam.
- `hapus_pesanan`, (Integer) Index buku yang ingin dihapus.
- `lagi`, (String) Pilihan pengguna untuk menghapus buku lagi.
- `buku`, (List) Data buku yang dipilih oleh pengguna.
- `identitas`, (List) Data identitas peminjam dan buku yang dipinjam  
    




