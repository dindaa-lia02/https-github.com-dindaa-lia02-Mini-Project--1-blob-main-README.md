
print("Verifikasi Data Anda")
while True:
    nama = input("Nama: ")
    nim = int(input("NIM: "))

    if nama == "Dinda Aulia Rizky" and nim == 2409116076:
        print("Nama dan NIM Terverifikasi")
        break
    else:
        print("Nama dan NIM anda tidak ditemukan, silakan coba lagi")
        nama = input("Nama: ")
        nim = int(input("NIM: "))

print()

print("=====================================")
print("Menghitung Total Harga Barang Diskon")
print("=====================================")

print()

def kalkulator_total_hargadiskon():
    harga_barang= int(input("Masukkan harga barang: "))
    jumlah_pembelian= int(input("Masukkan jumlah pembelian: "))

    diskon=0.25
    total_harga= harga_barang * jumlah_pembelian

    if total_harga > 250000:
        diskon_harga= total_harga * diskon
        total_hargadiskon = total_harga - diskon_harga
        print("Selamat anda mendapatkan diskon sebesar 25%")
        print(f"Total harga setelah diskon: Rp {int(total_hargadiskon)}")
        print(f"Terima Kasih sudah berbelanja di Toko kami")
    else:
        print(f"Maaf anda tidak mendapat diskon dengan harga: Rp {int(total_harga)}")
        print(f"Terima Kasih sudah berbelanja di Toko kami")

while True:
    kalkulator_total_hargadiskon()
    pilih= input("Apakah ingin menghitung total harga lagi? y/n: ")
    if pilih.lower() == 'n':
        break