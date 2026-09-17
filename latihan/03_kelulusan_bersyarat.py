# Program menentukan kelulusan berdasarkan nilai dan kehadiran

nilai = float(input("Masukkan nilai: "))
kehadiran = float(input("Masukkan kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")