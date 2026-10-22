
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

lulus = nilai_lulus(nilai)
tidak_lulus = len(nilai) - len(lulus)

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Daftar nilai = {nilai}")
print(f"Jumlah data = {len(nilai)}")
print(f"Total nilai = {sum(nilai)}")
print(f"Rata-rata = {rata_rata(nilai):.2f}")
print(f"Nilai minimum = {min(nilai)}")
print(f"Nilai maksimum = {max(nilai)}")
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")
print(f"Jumlah tidak lulus = {tidak_lulus}")


print("\n=== TEST CASE WAJIB ===")

# Test 1: Rata-rata
data = [60, 70, 80]
print("\nTest 1 - Rata-rata")
print(f"Hasil: {rata_rata(data):.2f}")
print("Harapan: 70.00")

# Test 2: Minimum dan maksimum
print("\nTest 2 - Minimum dan maksimum")
print(f"Minimum: {min(data)}")
print(f"Maksimum: {max(data)}")
print("Harapan: 60 dan 80")

# Test 3: Jumlah nilai lulus
print("\nTest 3 - Jumlah lulus")
print(f"Hasil: {len(nilai_lulus(data))}")
print("Harapan: 3")

# Test 4: Batas kelulusan 60
data = [59, 60, 61]
print("\nTest 4 - Batas kelulusan")
print(f"Nilai lulus: {nilai_lulus(data)}")
print(f"Jumlah lulus: {len(nilai_lulus(data))}")
print("Harapan: 2")

# Test 5: List kosong
data = []
print("\nTest 5 - List kosong")
print(f"Hasil: {rata_rata(data)}")
print("Harapan: 0")
