nama = input("Masukkan Nama Karyawan: ")
lama_kerja = float(input("Masukkan Lama Kerja (Tahun): "))
gaji_pokok = float(input("Masukkan Gaji Pokok (Rp): "))

if lama_kerja > 5:
    bonus = 0.10 * gaji_pokok
elif lama_kerja > 2:
    bonus = 0.05 * gaji_pokok
else:
    bonus = 0

total_gaji = gaji_pokok + bonus

print("\n--- Rincian Gaji Karyawan ---")
print(f"Nama       : {nama}")
print(f"Gaji Pokok : Rp {gaji_pokok:,.2f}")
print(f"Bonus      : Rp {bonus:,.2f}")
print(f"Total Gaji : Rp {total_gaji:,.2f}")