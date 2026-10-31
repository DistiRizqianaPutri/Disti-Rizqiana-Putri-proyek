# Konstanta batas kelulusan sesuai modul
BATAS_LULUS = 60

def hitung_rata_rata(nilai):
    """Mengembalikan rata-rata list numerik.
    Jika data kosong, fungsi mengembalikan 0 untuk mencegah ZeroDivisionError[cite: 7].
    """
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)

def status_lulus(nilai, batas=BATAS_LULUS):
    """Menyaring daftar nilai siswa yang mencapai atau di atas batas kelulusan[cite: 5, 6]."""
    return [x for x in nilai if x >= batas]

def ringkasan(nilai):
    """Menghasilkan dictionary ringkasan statistik nilai siswa[cite: 5]."""
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(status_lulus(nilai))
    }