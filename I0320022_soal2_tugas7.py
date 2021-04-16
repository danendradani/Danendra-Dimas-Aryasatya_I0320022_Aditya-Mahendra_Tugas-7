# input jumlah nilai yang akan dimasukkan
n = int(input("Banyak nilai yang ingin dimasukkan : "))
data = []
print()

# pengulangan memasukkan nilai
i = 1
while i <= n:
    nilai = float(input("Masukkan nilai ke-%d : " %i))
    data.append(nilai)
    i = i + 1
print()
print("Data nilai : ", data)
print()

# menghitung nilai minimal
import math
print("Nilai terendah : ", min(data))
print()

# menghitung nilai maksimal
import math
print("Nilai tertinggi : ", max(data))
print()

# menghitung rata-rata
import math
rata_rata = sum(data) / n
print("Nilai rata-rata : ", rata_rata)
print()

# pembulatan rata-rata ke atas
import math
print("Nilai rata-rata setelah dibulatkan ke atas : ", math.ceil(rata_rata))
print()

# pembulatan rata-rata ke bawah
import math
print("Nilai rata-rata setelah dibulatkan ke bawah : ", math.floor(rata_rata))