def tampilkan_hasil(hasil_ringkasan):
    """Menampilkan ringkasan hasil analisis nilai ke terminal[cite: 5]."""
    print("\n" + "="*35)
    print("      RINGKASAN ANALISIS NILAI     ")
    print("="*35)
    print(f"Total Siswa       : {hasil_ringkasan['jumlah']}")
    print(f"Rata-rata Kelas   : {hasil_ringkasan['rata_rata']:.2f}")
    print(f"Nilai Minimum     : {hasil_ringkasan['minimum']}")
    print(f"Nilai Maksimum    : {hasil_ringkasan['maksimum']}")
    print(f"Siswa Lulus (>=60): {hasil_ringkasan['lulus']}")
    print("="*35)