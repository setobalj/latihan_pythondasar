pricelist = {
    "ayam": 15000,
    "sapi": 12000,
    "babi": 10000,
}

total_kotor = 0
total_diskon = 0
total_bersih = 0

print("=== SISTEM KASIR PINTAR TOKO DAGING ===")
print("Ketik 'cukup' untuk selesai")

while True:
    jenis = input("Masukkan jenis daging (Ayam/Sapi/Babi): ").strip().lower()

    if jenis == "cukup":
        break

    if jenis not in pricelist:
        print("Peringatan: jenis daging tidak terdaftar. Silakan pilih Ayam, Sapi, atau Babi.")
        continue

    try:
        kg = float(input("Masukkan jumlah kilogram: "))
    except ValueError:
        print("Peringatan: jumlah kilogram harus berupa angka.")
        continue

    if kg <= 0:
        print("Peringatan: jumlah kilogram harus lebih dari 0.")
        continue

    harga_per_kg = pricelist[jenis]
    total_kg = kg
    subtotal = harga_per_kg * kg
    diskon = 0

    if jenis == "ayam":
        if kg >= 5:
            diskon = subtotal * 0.10
        else:
            diskon = 0
    elif jenis == "sapi":
        if kg >= 2:
            diskon = subtotal * 0.15
        else:
            diskon = 0
    elif jenis == "babi":
        if kg >= 3:
            diskon = subtotal * 0.12
        else:
            diskon = 0

    total_kotor += subtotal
    total_diskon += diskon
    total_bersih += subtotal - diskon

    print(f"Subtotal {jenis.title()}: Rp {subtotal:,.2f}")
    print(f"Diskon: Rp {diskon:,.2f}")
    print("-" * 30)

print("\n=== NOTA PEMBAYARAN ===")
print(f"Total kotor:      Rp {total_kotor:,.2f}")
print(f"Total potongan:   Rp {total_diskon:,.2f}")
print(f"Total bersih:     Rp {total_bersih:,.2f}")
print("Terima kasih telah berbelanja!")
