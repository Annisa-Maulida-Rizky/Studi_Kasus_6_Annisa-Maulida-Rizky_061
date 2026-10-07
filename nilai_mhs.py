import json

with open("data_nilai.json", "r", encoding = "utf-8") as f :
    data = json.load(f)

def tambah_data (NAMA, NIM, PRODI, NILAI, MATKUL):
    data.append ({
        "Nama" : NAMA,
        "NIM" : NIM,
        "Prodi" : PRODI,
        "Nilai" : NILAI,
        "Matkul" : MATKUL 
    })
    return "Data berhasil ditambah"

def simpan_file():
    with open ("data_nilai.json", "w", encoding= "utf-8") as f :
        json.dump (data, f, indent= 4)
        return "Data tersimpan ke data_nilai"

def tampilkan_data():
    for mahasiswa in data:
         print("Nama    : ", mahasiswa["Nama"])
         print("NIM     : ", mahasiswa["NIM"])
         print("Prodi   : ", mahasiswa["Prodi"])
         print("Nilai   : ", mahasiswa["Nilai"])
         print("Matkul  : ", mahasiswa["Matkul"])
         print("_________________________________")

while True:
    print("========== Menu ==========")
    print("1. Tampilkan data nilai")
    print("2. Tambahkan nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("========= Data Nilai =========")
        tampilkan_data()

    elif pilihan == "2":
        print("======== Tambah Data Nilai ========")

        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        prodi = input("Masukkan prodi: ")
        nilai = input("Masukkan nilai: ")
        matkul = input("Masukkan matkul: ")

        print(tambah_data(nama, nim, prodi, nilai, matkul))
        print(simpan_file())

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid")
