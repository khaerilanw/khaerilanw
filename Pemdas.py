# INPUT USER
print("PROGRAM HITUNG GAJI KARYAWAN\n")

nama = input("Nama Karyawan: ")
jabatan = input("Golongan Jabatan: ")
if jabatan == "1":
    jab = 0.05
elif jabatan == "2":
    jab = 0.1
elif jabatan == "3":
    jab = 0.15
else:
    jab = 0
pendidikan = input("Pendidikan: ")
if pendidikan == "SMA":
    pend = 0.025
elif pendidikan == "D1":
    pend = 0.05
elif pendidikan == "D3":
    pend = 0.2
elif pendidikan == "S1":
    pend = 0.3
else:
    pend = 0

jamKerja = int(input("Jumlah jam kerja: "))
if jamKerja > 8:
    jamLembur = jamKerja - 8

# OPERASI HITUNG GAJI

tunjanganJabatan = jab * 300000
tunjanganPendidikan = pend * 300000
lembur = jamLembur * 3500
total = 300000 + tunjanganJabatan + tunjanganPendidikan + lembur

print("Karyawan yang bernama", nama)
print("Honor yang diterima")
print("Tunjangan jabatan Rp.", tunjanganJabatan)
print("Tunjangan pendidikan Rp.", tunjanganPendidikan)
print("Honor lembur Rp.", lembur)
print("")
print("Total Gaji Rp.", total)
print("Gaji pokok + tunjangan + lembur")