nama_program = "KDMP"
print(f"---Selamat Datang di {nama_program} Ayam Potong---")

harga_ayam = 20000

while True:
    jawaban = input("Berapa ayam yang anda beli (kg):").strip().lower()
    if jawaban == "cukup":
        print("Terima kasih!")
        break
    try:
        berapa_kilo = float(jawaban)
    except ValueError:
        print("Input harus angka.")
        continue

    total_harga = harga_ayam * berapa_kilo

    if berapa_kilo > 5:
        diskon = 7000
        print(f"Selamat! Anda mendapatkan diskon sebesar: Rp{diskon:,.0f}")
    elif berapa_kilo >= 2:
        diskon = 5000
        print(f"Selamat! Anda mendapatkan diskon sebesar: Rp{diskon:,.0f}")
    else:
        diskon = 0
        print("Maaf, Anda tidak mendapatkan diskon.")

    total_bayar = total_harga - diskon
    print(f"Silahkan Bayar sebesar: Rp{total_bayar:,.0f}")

