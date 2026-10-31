# Berkas Utama Program: main.py
from src.input_data import ambil_input_nilai
from src.proses import ringkasan
from src.output import tampilkan_hasil

def main():
    print("=========================================")
    print("   PROGRAM ANALISIS NILAI SISWA (UNTIRTA) ")
    print("=========================================\n")
    
    # 1. Mengambil masukan data dari pengguna (dengan penanganan error)
    data_nilai = ambil_input_nilai()
    
    if data_nilai:
        # 2. Memproses data statistik melalui modul proses
        hasil = ringkasan(data_nilai)
        
        # 3. Menampilkan ringkasan hasil analisis ke terminal
        tampilkan_hasil(hasil)
    else:
        print("\nProgram dihentikan: Tidak ada data valid yang diproses.")

if __name__ == "__main__":
    main()