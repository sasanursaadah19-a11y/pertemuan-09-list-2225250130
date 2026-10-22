
# Pertemuan 09 List dan Pengolahan Data Numerik

**Nama:** Sasa Nursaadah

**NIM:** 2225250130

**Kelas:** 3F

## Tujuan

Mempelajari penggunaan list, indeks, slicing, manipulasi list, agregasi data numerik, filtering, dan fungsi statistik untuk mengolah kumpulan data menggunakan Python.

## Cara Menjalankan

Jalankan program praktik dengan perintah berikut melalui terminal:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

## Struktur Program

Program `analisis_nilai_mahasiswa.py` memiliki beberapa proses berikut:

1. `rata_rata(data)` digunakan untuk menghitung rata-rata nilai dan mengembalikan 0 jika list kosong.
2. `nilai_lulus(data, batas=60)` digunakan untuk menyaring nilai yang memenuhi batas kelulusan.
3. `len(nilai)` digunakan untuk menghitung banyaknya data.
4. `sum(nilai)` digunakan untuk menghitung total nilai.
5. `min(nilai)` dan `max(nilai)` digunakan untuk mencari nilai minimum dan maksimum.
6. Program menghitung jumlah mahasiswa yang lulus dan belum lulus.

## Hasil Pengujian

| Operasi | Input | Hasil yang Diharapkan |
|---|---|---|
| Rata-rata | `[60, 70, 80]` | `70.00` |
| Minimum dan maksimum | `[60, 70, 80]` | `60` dan `80` |
| Jumlah nilai lulus | `[60, 70, 80]` | `3` |
| Filter kelulusan | `[59, 60, 61]`, batas `60` | `[60, 61]`, jumlah `2` |
| List kosong | `[]` | Rata-rata `0`, tanpa error |

## Refleksi

Dengan menggunakan list, beberapa data numerik dapat disimpan dalam satu variabel sehingga lebih mudah diolah. Fungsi membantu membuat proses perhitungan lebih terstruktur dan dapat digunakan kembali. Saya juga memahami penggunaan indeks, slicing, agregasi, dan filtering untuk mengolah data, serta pentingnya memeriksa list kosong sebelum menghitung rata-rata.

