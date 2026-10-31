# Dokumentasi Penggunaan & Pengujian Visual

Dokumen ini berisi panduan alur eksekusi aplikasi **Analisis Nilai Siswa** serta penjelasannya untuk melengkapi struktur folder `docs/` pada proyek akhir.

---

## 1. Alur Eksekusi Program

1. **Menjalankan Program:**
   Pengguna menjalankan program utama dari terminal direktori proyek:
   ```bash
   python main.py
   ```

2. **Input Data Siswa:**
   Program akan meminta pengguna memasukkan deretan nilai yang dipisahkan oleh spasi atau koma.
   * *Contoh Input Valid:* `75 80 65 90 55 85 70`
   * *Contoh Input Invalid (Teks):* `70 80 abc` (akan ditangani oleh modul `src/input_data.py` tanpa *crash*).

3. **Pemrosesan Data:**
   Modul `src/proses.py` menghitung:
   * Total siswa
   * Rata-rata kelas
   * Nilai tertinggi (maksimum) dan terendah (minimum)
   * Jumlah siswa yang lulus (berdasarkan KKM `BATAS_LULUS = 60`)

4. **Output Hasil Analisis:**
   Modul `src/output.py` menampilkan format ringkasan statistik secara rapi di terminal.

---

## 2. Bukti Pengujian Visual (Screenshot)

Simpan hasil *screenshot* terminal Anda di dalam folder `docs/screenshot/` dengan nama berkas `hasil_run.png`. 

![Tampilan Program Saat Dijalankan](screenshot/hasil_run.png)

> **Catatan:** Jika berkas gambar `hasil_run.png` sudah diletakkan di dalam folder `docs/screenshot/`, gambar tersebut akan otomatis ditampilkan pada pratinjau Markdown di VS Code maupun GitHub.