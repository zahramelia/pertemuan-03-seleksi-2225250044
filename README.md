# Pertemuan 03 Seleksi Python

Nama: Zahra Amelia  
NIM: 2225250044  
Kelas: 3 B  

## Tujuan

Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan

Program dapat dijalankan melalui terminal dengan perintah:

python tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas

1. Membaca koefisien a, b, dan c sebagai bilangan float.
2. Memeriksa apakah nilai a sama dengan 0.
3. Jika a = 0, maka input bukan merupakan persamaan kuadrat.
4. Jika a tidak sama dengan 0, menghitung diskriminan dengan rumus:
   D = b² - 4ac.
5. Jika D > 0, maka persamaan memiliki dua akar real yang berbeda.
6. Jika D = 0, maka persamaan memiliki satu akar real kembar.
7. Jika D < 0, maka persamaan tidak memiliki akar real.
8. Menampilkan hasil perhitungan dengan dua angka di belakang koma.

## Hasil Pengujian

| Input (a, b, c) | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| (1, -5, 6) | Dua akar real: 3 dan 2 | Diskriminan = 1.00, Akar pertama = 3.00, Akar kedua = 2.00 | Sesuai |
| (1, 2, 1) | Akar real kembar: -1 | Diskriminan = 0.00, Akar kembar = -1.00 | Sesuai |
| (1, 0, 1) | Tidak ada akar real | Diskriminan = -4.00, Tidak memiliki akar real. | Sesuai |
| (0, 2, 3) | Bukan persamaan kuadrat | Bukan persamaan kuadrat. | Sesuai |

## Refleksi

Kesalahan logika yang perlu diperhatikan adalah menentukan jenis akar berdasarkan nilai diskriminan. Jika kondisi D > 0, D = 0, dan D < 0 tidak dibedakan dengan benar, hasil program dapat menjadi tidak sesuai. Setelah dilakukan pengujian dengan beberapa kondisi diskriminan, program dapat menentukan jenis akar sesuai dengan input yang diberikan.

## Bantuan/Sumber

Materi Pertemuan 03 Seleksi Python.