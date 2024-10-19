#Belajar fungsi
        #mengisi nilai parameter
def sapa(nama, tanggal_lahir):
  print("Halo,", nama, tanggal_lahir, "!")
# Format string tanpa jarak spasi
  # print(f"Halo, {nama}!")
# Menampilkan hasil fungsi

# mengisi nilai fungsi dengan tipe data string yaitu andi
sapa("Andi Firmansyah Taufik", 18)  
# Output: Halo, Andi!

def tambah(a, b, c):
  hasil = (a + b) / c
  return hasil

jumlah = tambah(3, 5, 2)
print("Hasilnya adalah:", jumlah)  
# Output: 8:4=2