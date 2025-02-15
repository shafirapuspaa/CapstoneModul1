
from tabulate import tabulate

# Data awal

daftar_buku = [['Index', 'Judul_buku', 'Penerbit', 'Tahun_terbit', 'Status','Rak'],
               ["Dilan", 'Pidibaiq', 2019, 'Tersedia',1],['Hujan','Tereliye',2018,'Tersedia',2],['Mimpi','April Cahaya',2020,'Tersedia',2],['Monolog','Rika',2017,'Tersedia',3]]
isi_chart = [['Judul_buku', 'Penerbit', 'Tahun_terbit']]
isi_identitas = [['Index','Nama', 'Nomor hp', 'NIK','Judul_buku', 'Penerbit', 'Tahun_terbit']]

# Fungsi untuk menampilkan menu karyawan
def menu_karyawan():
    print('')
    print('Selamat datang karyawan')
    print('''List jobdesc karyawan
          1. Menampilkan daftar buku
          2. Menambahkan list buku
          3. Menghapus buku baru
          4. Menampilkan list peminjam
          5. Kembali ke menu utama
          ''')

# Fungsi untuk menampilkan menu peminjam
def menu_peminjam():
    print('')
    print('''Selamat datang di peminjaman online. Apa yang anda ingin lakukan? :
          1. Melihat daftar buku
          2. Meminjam buku
          3. Mengembalikan buku
          4. Menampilkan rak buku
          5. Menu karyawan
          ''')

# Fungsi untuk menampilkan daftar buku
def tampilkan_daftar_buku():
    print('Berikut adalah daftar buku yang tersedia di perpustakaan kami: ')
    print(tabulate(daftar_buku, headers='firstrow', showindex="always"))

# Fungsi untuk mencari buku di rak
def cari_buku():
    print('''Berikut adalah list rak koleksi buku kami sesuai jenis buku: 
           - Rak 1 Novel
           - Rak 2 Kamus
           - Rak 3 Komik'''
           )
    while True: 
        try:
            rak = int(input('Masukkan nomor rak yang anda ingin lihat koleksinya: '))
        except ValueError: #untuk mencegah kesalahan memasukan jenis data
            print('Inputan tidak valid!,silahkan input kembali')
            continue
        buku_di_rak = [buku for buku in daftar_buku[1:] if buku[4] == rak] #daftar buku 1: karena 0 headers buku[4] itu letak ranya == rak
        if buku_di_rak:
            print(f"Daftar buku di rak {rak}:")
            print(tabulate(buku_di_rak, headers=daftar_buku[0], showindex="always")) #menampilkan koleksi buku setiap raknya

            #input user dapat melihat kembali koleksi buku di rak berbeda
            lagi = (input('Mau liat rak yang lain[ya,tidak]? ').lower()) 
            if lagi == 'tidak':
                print('Terimakaasih telah melihan koleksi buku di rak kami ')
                break #keluar loopingan ke menu utam
            elif lagi == 'ya':
                print('''Berikut adalah list rak koleksi buku kami sesuai jenis buku: 
                    - Rak 1 Novel
                    - Rak 2 Kamus
                    - Rak 3 Komik''')
                continue #masuk kembali ke loopingan
            else:
                print('Input tidak sesuai silahkan pilih kembali menu menampilkan rak buku')
                break
        else:
            print(f"Tidak ada buku di rak {rak},silahkan input kembali nomor rak ")
            continue #masuk kembali ke loopingan masukan nomor rak

# Fungsi untuk meminjam buku
def pinjam_buku():
    while True: #ketika benar akan melooping terus agar bisa pakai try and except
            print(' ')
            print('Berikut adalah buku koleksi kami: ')
            print(tabulate(daftar_buku,headers= 'firstrow',showindex="always"))
            try:
                pinjam = int(input('Masukan index buku yang ingin dipinjam: '))
            except ValueError: #untuk mencegah kesalahan memasukan jenis data
                print('inputan tidak valid! ')
                continue  #agar masuk ke input pinjam

            #untuk mencegah memasukan index yang tidak sesuai
            if 0 <= pinjam < len(daftar_buku) - 1: 

                #ketika status buku dengan index yang dipilih = tersedi
                if daftar_buku [pinjam+1][3] == 'Tersedia': 
                    daftar_buku0 = daftar_buku[pinjam+1][0] # kolom judul buku
                    daftar_buku1 = daftar_buku[pinjam+1][1] # kolom penerbit
                    daftar_buku2 = daftar_buku[pinjam+1][2] # kolom tahun terbit

                    chart = [daftar_buku0,daftar_buku1,daftar_buku2] #menggabungkan judul,penerbit dan tahun terbit
                    isi_chart.append(chart) #di append agar isichart dapat bertambah

                    # Memasukan identitas user
                    nama = input('Masukan identitas anda: ').capitalize()
                    nomor= input('Masukan nomor telfon: ')
                    nik = input('Masukan nomor nik anda sesuai KTP: ')

                    print(' ')
                    print('isi chart anda: ')
                    print(tabulate(isi_chart,headers= 'firstrow',showindex="always"))
                    print('')

                    #ubah statusnya yang sudah dipinjam menjadi tidak tersedia 
                    daftar_buku [pinjam+1][3] = ' Tidak tersedia'
                    print(' ')
                    print(f'Selamat {nama} anda berhasil meminjam buku dengan koleksi dibawah ini: ')
                    print(' ')
                    print(tabulate(isi_chart,headers= 'firstrow',showindex="always")) 
                    identitas = [nama,nomor,nik,daftar_buku0,daftar_buku1,daftar_buku2]

                    #membuat tabel identitas dan buku yang dipinjam
                    isi_identitas.append(identitas) 

                    #ingin meminjam lagi atau tidak?
                    print(' ')
                    lagi = input('mau sewa yang lain[ya,tidak]? ').lower ()
    
                    if lagi == 'tidak': 
                        print('Terimakasih telah meminjam buku saat ini chart anda sebagai berikut: ')
                        print(tabulate(isi_chart,headers= 'firstrow',showindex="always"))
                        break
                    elif lagi == 'ya':
                        continue #jika 'ya' dapat meminjam kembali dengan melooping/ masuk lagi ke program pinjam buku
                    else:
                        print('Input tidak sesuai silahkankan memilih kembali ke menu utama, saat ini list chart anda sebagai berikut:') 
                        print(tabulate(isi_chart,headers= 'firstrow',showindex="always"))
                        break    

                #jika status tidak tersedia
                elif daftar_buku [pinjam+1][3] == ' Tidak tersedia': #+1 karena headers tidak ingin dihitung
                        print('maaf buku sedang dipinjam,silahkan memilih koleksi buku lainnya')
                        print(' ')
                        continue #masuk kembali ke loop pinjam buku
                
            # jika index pinjam lebih dari pilihan index maka akan melooping kembal
            else:
                 print('input tidak valid ') 
                 continue #masuk kembali ke loop pinjam buku
            break


def kembalikan_buku2():
    print('')
    print('Buku yang anda pinjam')
    print(tabulate(isi_chart, headers='firstrow', showindex="always"))
    while True: #menjaga inputan agar sesuai menggunakan try and except
        try:
            balikin = int(input('Masukkan index buku yang ingin dikembalikan: '))
        except ValueError:
            print('Input tidak sesuai')
            continue   

        # Pengecekan apakah indeks valid
        if 0 <= balikin < len(isi_chart) - 1:  # -1 karena headers tidak dihitung

            #Ambil judul buku yang dikembalikan
            judul_buku = isi_chart[balikin + 1][0]  # +1 karena ada headers
            del isi_chart[balikin + 1]  # Hapus buku dari isi_chart
            for buku in daftar_buku:   # Ubah status buku di daftar_buku menjadi "Tersedia"
                if buku[0] == judul_buku:  # Cari buku berdasarkan judul
                    buku[3] = 'Tersedia'  # Ubah status
                    break    
                print('')
                print('Buku berhasil dikembalikan.')
                print('')
                print('Isi chart anda sekarang:')
                print(tabulate(isi_chart, headers='firstrow', showindex="always"))

            #ingin mengembalikan lagi
            lagi = input('mau mengembalikan yang lain[ya,tidak]? ').lower()
            if lagi == 'tidak': 
                print('Terimakasih telah mengembalikan buku')
                break 
            if lagi == 'ya':
                continue #jika meminjam lagi maka akan melooping program
            else:
                print('''Terimakasih telah mengembalikan buku,
                    maaf input tidak valid jika ingin mengembalikan kembali ketik 3''')
                break   #menjaga salah input ya dan tidak
        else:
            print('''Indeks tidak valid! anda salah menginput index atau anda sudah mengembalikan semua buku''') #jika diluar index yang valid atau chart kosong
            return


# Fungsi untuk menambahkan buku baru
def tambah_buku():
    while True: #pengecekan input yang sesuai
        try:
            judul_baru = input('Masukkan judul baru: ').lower()
            penerbit_baru = input('Masukkan nama penerbit: ').lower()
            terbitan_baru = int(input('Masukkan tahun terbit: '))
            rak_baru = int(input('Masukkan rak: '))
            status_baru = 'Tersedia'

            #penjagaan agar nomor rak hanya bisa diisi sampai 3
            if rak_baru >3 and rak_baru==0:
                print('Rak hanya ada 3!, harap ulangi iput buku')
                continue
        except ValueError:
            print('input tidak sesuai')
            continue
        #menambahkan daftar buku baru
        add_buku = [judul_baru, penerbit_baru, terbitan_baru, status_baru,rak_baru]
        daftar_buku.append(add_buku)
        tampilkan_daftar_buku()

        #ingin menambahkan lagi
        lagi = input('mau tambah buku yang lain[ya,tidak]? ').lower()
        if lagi == 'tidak': 
            return 
        if lagi == 'ya':
            continue #jika tidak meminjam lagi
        else:
            print('Input tidak Sesuai silahkan pilih kembali lagi menu ')
            break

# Fungsi untuk menghapus buku
def hapus_buku():
    while True:  # Loop untuk pengecekan input yang sesuai
        try:
            print(tabulate(daftar_buku, headers='firstrow', showindex="always"))
            hapus_pesanan = int(input('Masukkan index buku yang ingin dihapus: '))
            
            # Cek apakah index yang dimasukkan valid
            if hapus_pesanan < 0 or hapus_pesanan >= len(daftar_buku) - 1:  # -1 karena header di index 0
                print('Index tidak valid. Silakan masukkan index yang sesuai.')
                continue  # Lanjutkan loop untuk meminta input kembali
            
            # Ambil buku berdasarkan index
            buku = daftar_buku[hapus_pesanan + 1]  # +1 karena header di index 0
            
            # Cek status buku
            if buku[3] == 'Tersedia':
                del daftar_buku[hapus_pesanan + 1]  # Hapus buku yang tersedia
                print('Buku berhasil dihapus.')
                print(tabulate(daftar_buku, headers='firstrow', showindex="always"))
                
                # Tanya apakah ingin menghapus buku lagi
                lagi = input('Mau hapus buku lagi [ya/tidak]? ').lower()
                if lagi == 'tidak':
                    return  # Kembali ke menu utama
                elif lagi != 'ya':
                    print('Input tidak valid, kembali ke menu utama.')
                    return  # Kembali ke menu utama jika input tidak valid
            else:
                print('Buku tidak dapat dihapus karena statusnya "tidak tersedia".')
                break  # Keluar dari loop dan kembali ke menu utama
        
        except ValueError:
            print('Input tidak valid. Harap masukkan angka.')
            continue  # Lanjutkan loop untuk meminta input kembali



                
        
# Fungsi untuk menampilkan list peminjam
def tampilkan_peminjam():
    print('Data peminjam sebagai berikur: ')
    print(tabulate(isi_identitas,headers= 'firstrow',showindex="always"))

# Fungsi utama
def main():
    while True:
        menu_peminjam()
        try:
            aksi = int(input('Masukan list yang ingin dijalankan: '))
        except ValueError:
            print('inputan tidak valid silahkan memilih index yang tepat!')
            continue
        if aksi == 1:
            tampilkan_daftar_buku()
        if aksi == 2:
            pinjam_buku()   
        elif aksi == 3:
            kembalikan_buku2()
        elif aksi ==4:
            cari_buku()
        elif aksi == 5:
            while True:
                try:
                    pasword = int(input('Masukkan 3 angka password karyawan: '))
                except ValueError:
                    print('Input tidak valid')
                    continue
                if pasword == 123:
                    while True:
                        menu_karyawan()
                        try:
                            jobdesc = int(input('Masukkan list karyawan yang ingin dijalankan: '))
                        except ValueError:
                            print('Input tidak valid')
                            continue
                        if jobdesc == 1:
                            tampilkan_daftar_buku()
                        elif jobdesc == 2:
                            tambah_buku()
                        elif jobdesc == 3:
                            hapus_buku()
                        elif jobdesc == 4:
                            tampilkan_peminjam()
                        elif jobdesc == 5:
                            break
                        else:
                             print('index tidak sesuai')
                             continue
                    break
                else:
                    print('Password salah!')
        

# Jalankan program
main()