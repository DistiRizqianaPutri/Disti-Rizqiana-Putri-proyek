# Dokumentasi Test Case - Proyek Analisis Nilai Siswa

| ID | Fitur | Input | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | Rata-rata | `70, 80, 90` | `80.0` | `80.0` | **PASS**[cite: 7] |
| **TC02** | Kelulusan | `60` | `Lulus` | `Lulus` | **PASS**[cite: 7] |
| **TC03** | Input angka | `abc` | Pesan input tidak valid | Pesan input tidak valid | **PASS**[cite: 7, 20] |
| **TC04** | Data Kosong | `""` (kosong) | Rata-rata 0, tidak error | Rata-rata 0, tidak error | **PASS**[cite: 7] |