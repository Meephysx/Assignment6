NAMA = Danis Setiawati

NIM  = 20240040053

---

# Penilaian Skor dengan Python

Program ini digunakan untuk menentukan nilai huruf dan predikat berdasarkan skor yang diperoleh oleh pengguna. Program ini juga telah dilengkapi dengan validasi input agar dapat menangani kesalahan masukan yang tidak sesuai.

## Tabel Penilaian

| Skor   | Nilai Huruf | Predikat             |
|--------|------------|----------------------|
| 90-100 | A          | Dengan Pujian        |
| 80-89  | B          | Sangat Memuaskan     |
| 70-79  | C          | Memuaskan            |
| 60-69  | D          | Tidak Memuaskan      |
| 0-59   | E          | TIDAK LULUS          |

## Fitur Program

- Meminta pengguna untuk memasukkan skor (0-100).
- Menentukan nilai huruf dan predikat berdasarkan skor.
- Menampilkan hasil berupa skor, nilai huruf, dan predikat.
- Memiliki validasi input untuk memastikan hanya angka dalam rentang 0-100 yang dapat diterima.

## Cara Menjalankan Program

1. Pastikan Anda memiliki Python terinstal di komputer Anda (versi 3.x direkomendasikan).
2. Simpan file program sebagai `skor.py`.
3. Jalankan program menggunakan terminal atau command prompt:
   ```bash
   python skor.py
   ```
4. Masukkan skor yang diinginkan dan program akan menampilkan hasilnya.

## Kode Program

```python
def skor():
    """
    Program untuk menentukan nilai huruf dan predikat kelulusan
    berdasarkan skor yang diinput oleh pengguna.
    """
    try:
        # Meminta input dari pengguna
        skor = int(input("Masukkan skor (0-100): "))
        
        # Validasi range skor
        if skor < 0 or skor > 100:
            print("Error: Skor harus di antara 0 sampai 100.")
            return
        
        # Menentukan nilai huruf dan predikat
        if skor >= 90:
            nilai_huruf = "A"
            predikat = "Dengan Pujian"
        elif skor >= 80:
            nilai_huruf = "B"
            predikat = "Sangat Memuaskan"
        elif skor >= 70:
            nilai_huruf = "C"
            predikat = "Memuaskan"
        elif skor >= 60:
            nilai_huruf = "D"
            predikat = "Tidak Memuaskan"
        else:
            nilai_huruf = "E"
            predikat = "TIDAK LULUS"
        
        # Menampilkan hasil
        print(f"Skor Anda: {skor}")
        print(f"Nilai Huruf: {nilai_huruf}")
        print(f"Predikat   : {predikat}")
    
    except ValueError:
        print("Error: Masukkan nilai numerik (bilangan bulat).")

# Memanggil fungsi
penilaian()
```

## Flowchart

Berikut adalah flowchart sederhana dari program ini:

```
Mulai
 |
 v
Input skor -> ubah ke integer
 | (jika gagal, tampilkan "Error: Masukkan nilai numerik" -> Selesai)
 v
Cek apakah skor < 0 atau skor > 100
 | (jika ya, tampilkan "Error: Skor harus di antara 0 sampai 100" -> Selesai)
 v
IF skor >= 90
   Nilai Huruf = A, Predikat = "Dengan Pujian"
ELIF skor >= 80
   Nilai Huruf = B, Predikat = "Sangat Memuaskan"
ELIF skor >= 70
   Nilai Huruf = C, Predikat = "Memuaskan"
ELIF skor >= 60
   Nilai Huruf = D, Predikat = "Tidak Memuaskan"
ELSE
   Nilai Huruf = E, Predikat = "TIDAK LULUS"
 v
Tampilkan hasil
 v
Selesai
```

## Validasi Kesalahan

- Jika pengguna memasukkan nilai di luar rentang 0-100, program akan menampilkan pesan error dan meminta input ulang.
- Jika pengguna memasukkan nilai non-numerik, program akan menampilkan pesan error dan meminta input ulang.


