def ambil_input_nilai():
    """Menerima input nilai dari pengguna dengan penanganan error[cite: 7, 20]."""
    try:
        masukan = input("Masukkan daftar nilai siswa (pisahkan dengan spasi atau koma): ")
        if not masukan.strip():
            print("Peringatan: Input kosong.")
            return []
        
        # Mengubah format string menjadi list integer
        nilai_list = [int(x) for x in masukan.replace(',', ' ').split()]
        return nilai_list
    except ValueError:
        print("Kesalahan: Input tidak valid. Harap masukkan angka[cite: 7, 20].")
        return []