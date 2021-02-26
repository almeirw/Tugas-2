nama = []
phone_number= []
print('Selamat datang!')
def daftar_kontak():
    print('Daftar kontak')
    for x in range(len(nama)):
        print('Nama:', nama[x])
        print('No Telepon:', phone_number[x])

def tambah_kontak():
    isian_nama = (input('Nama:'))
    isian_nomor = (input('No Telepon:'))
    nama.append(isian_nama)
    phone_number.append(isian_nomor)
    if isian_nama == str() and isian_nomor == int():
        print('Kontak berhasil ditambahkan')
    else:
        pass

while True:
    print('---Menu---')
    print ('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    print('============')
    isian_pilihan = int(input('Pilih Menu:'))
    if isian_pilihan == 1:
        daftar_kontak()
    elif isian_pilihan == 2:
        tambah_kontak()
    elif isian_pilihan == 3:
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia')
        pass