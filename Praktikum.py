# =================================
# MUHAMMAD KHAERIL ANWAR
# KELAS 12.1A.35
# TUGAS PERTEMUAN 7
# TUGAS PRAKTIKUM
# MATA KULIAH DASAR PEMROGRAMAN
# =================================

# -----MEMBUAT MATRIX-----

# MATRIX DENGAN ORDO 2X2
matrix_1 = [
    [2, 0],
    [7, 8]
]
print(matrix_1)

# MATRIX DENGAN ORDO 3X3
matrix_2 = [
    [2, 1, 4],
    [7, 8, 2],
    [3, 5, 1]
]
print(matrix_2)

# MATRIX DENGAN ORDO 4X4
matrix_3 = [
    [2, 1, 4, 6],
    [7, 8, 2, 1],
    [3, 5, 1, 8],
    [1, 7, 5, 2]
]
print(matrix_3)




# MELAKUKAN PENJUMLAHAN MATRIKS
mat1 = [
    [2, 8],
    [4, 9]
]

mat2 = [
    [2, 8],
    [4, 9]
]

for i in range(0, len(mat1)):
    for  j in range(0, len(mat1[0])):
        print(mat1[i][j] + mat2[i][j], end=" ")
    print("")

# MELAKUKAN PENGURANGAN MATRIKS
mat1 = [
    [6, 8],
    [4, 2]
]

mat2 = [
    [6, 4],
    [5, 7]
]

for i in range(0, len(mat1)):
    for j in range(0, len(mat1[0])):
        print(mat1[i][j] - mat2[i][j], end=" ")
    print("")

# MELAKUKAN PENGURANGAN MATRIKS
mat1 = [
    [9, 0],
    [3, 6]
]

mat2 = [
    [6, 0],
    [7, 2]
]

mat3 = []
for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)
    
    for x in range(0, len(mat3)):
        for y in range(0, len(mat3[0])):
            print(mat3[x][y], end=" ")
        print()

import pandas as pd

# VARIABEL YANG BERULANG MENGGUNAKAN LIST/MATRIKS
list_nim = []
list_nama = []
list_uts = []
list_uas = []
list_total = []

ulang = 3
for i in range(ulang):
    print("Data Ke-", i+1)
    list_nim.append(input("NIM : "))
    list_nama.append(input("Nama : "))
    list_uts.append(int(input("Nilai UTS : ")))
    list_uas.append(int(input("Nilai UAS : ")))

# PROSES
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

tamu = {
    "NIM":list_nim,
    "Nama Lengkap":list_nama,
    "Nilai UTS":list_uts,
    "Nilai UAS":list_uas,
    "Rata-rata":list_total
}
data_tamu = pd.DataFrame(tamu)

# PRINTOUT
print("========================DAFTAR NILAI========================")
print(data_tamu)
print("=============================================================")
