# 1. Inisialisasi Dictionary produk awal
produk = {
    "nama" : "Susu",
    "harga" : "10000",
    "stok" : "25"
}

# 2. Perulangan menu
while True:
    print("\n=== MENU PENGELOLAAN DATA PRODUK ===")
    print("1. Tampilkan data produk")
    print("2. Tambahkan data produk")
    print("3. Ubah harga produk")
    print("4. Hapus kategori produk")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # 3. Menampilkan data produk
        print("\n--- Data Produk ---")
        for key, value in produk.items():
            print(f"{key.capitalize()}: {value}")

    elif pilihan == "2":
        # 4. Menambahkan data kategori
        kategori_baru = input("Masukkkan nama kategori: ")
        produk["kategori"] = kategori_baru
        print("Kategori berhasil ditambahkan!")

        print("\n--- Data Produk terbaru ---")
        for key, value in produk.items():
            print(f"{key.capitalize()}: {value}")

    elif pilihan == "3":
        # 5. Mengubah data
        harga_baru = int(input("Masukkan harga baru: "))
        produk["harga"] = harga_baru
        print("Harga berhasil diubah!")

        print("\n--- Data Produk terbaru ---")
        for key, value in produk.items():
            print(f"{key.capitalize()}: {value}")

    elif pilihan == "4":
        # 6. Hapus data kategori
        if "kategori" in produk:
            del produk["kategori"]
            print("Kategori berhasil dihapus!")
        else:
            print("Kategori belum ada di dalam data produk.")

    elif pilihan == "5":
        # 7. Keluar dari pengulangan
        print("Terima kasih!")
        break

else:
    print("Pilihan tidak valid, silahkan coba lagi.")