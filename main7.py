# Harga makanan
harga_makanan = {
    "nasi goreng": 20000,
    "mie goreng": 15000,
    "sate": 30000
}
uang_saku = 3010000
diskon_persen = 20

def hitung_total(pesanan):
    total = 0
    for makanan, jumlah in pesanan.items():
        total += harga_makanan[makanan] * jumlah
    return total

def tampilkan_rincian(pesanan):
    print("\nRincian Belanja:")
    for makanan, jumlah in pesanan.items():
        harga = harga_makanan[makanan]
        total_harga = harga * jumlah
        print(f"- {jumlah} porsi {makanan}: Rp {total_harga}")

pesanan = {}
lanjutkan = True

while lanjutkan:
    print("Menu Makanan:")
    for makanan, harga in harga_makanan.items():
        print(f"- {makanan}: Rp {harga}")
    
    jenis_makanan = input("Masukkan jenis makanan (atau 'selesai' untuk mengakhiri): ")
    if jenis_makanan.lower() == "selesai":
        lanjutkan = False
    else:
        jumlah_porsi = int(input("Masukkan jumlah porsi: "))
        pesanan[jenis_makanan] = pesanan.get(jenis_makanan, 0) + jumlah_porsi

# Hitung total harga
total_belanja = hitung_total(pesanan)

# Cek diskon
if total_belanja > 100000:
    diskon = total_belanja * diskon_persen / 100
    total_belanja -= diskon
    print(f"Anda mendapatkan diskon {diskon_persen}% sebesar Rp{diskon}")

# Cek apakah uang saku cukup
if total_belanja > uang_saku:
    print("Uang saku Anda tidak cukup.")
else:
    kembalian = uang_saku - total_belanja
    tampilkan_rincian(pesanan)
    print(f"\nTotal Belanja: Rp {total_belanja}")
    print(f"Uang Kembalian: Rp {kembalian}")

# SOAL NO 4
fruits = ("banana", "apple", "cherry")

# Ubah tuple menjadi list
fruit_list = list(fruits)
fruit_list.sort()
print(fruit_list)

# Buat list karakter dari "banana"
banana_chars = list(fruit_list[1])  # Akses elemen "banana" dan ubah menjadi list

print(banana_chars)  # Output: ['b', 'a', 'n', 'a', 'n', 'a']


# SOAL NO 5
def find_intersection(set1, set2):
    """Mencari irisan dari dua set."""
    return set1.intersection(set2)

set1 = {1, 2, 3, 4, 7}
set2 = {3, 4, 5, 6, 7}
result = find_intersection(set1, set2)
print(result)