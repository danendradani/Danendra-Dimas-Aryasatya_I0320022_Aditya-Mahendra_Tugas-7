# input kalimat awal
print("Masukkan kalimat")
kalimat = str(input("<< "))
print()

# menghitung jumlah huruf vokal dalam kalimat
print("Menghitung jumlah huruf vokal")
a = kalimat.count("a")
i = kalimat.count("i")
u = kalimat.count("u")
e = kalimat.count("e")
o = kalimat.count("o")
print("Jumlah seluruh huruf vokal dalam kalimat tersebut adalah ", a + i + u + e +o)
print()

# mengubah menjadi huruf kapital
print("Mengubah menjadi huruf kapital")
print(kalimat.upper())
print()

# mengganti 1 kata
print("Mengganti salah satu kata")
diganti = str(input("Kata yang ingin diganti : "))
pengganti = str(input("Kata pengganti : "))
print()
print("Kalimat awal : \n", kalimat)
print("Kalimat setelah diubah : \n", kalimat.replace(diganti, pengganti))
print()