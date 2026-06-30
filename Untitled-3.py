import json
from pathlib import Path

MENU_FILE = Path("Daftar menu.json")
DISCOUNT_RULES = {
    "ayam": (5, 0.10),
    "sapi": (2, 0.15),
    "babi": (3, 0.12),
}


def load_pricelist():   #Method to load the price list from a JSON file and normalize the keys to lowercase.
    """Load the price list from JSON and normalize meat type keys."""
    with MENU_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return {key.lower(): value for key, value in data.items()}


def format_idr(amount):    #Method to format a number into Indonesian Rupiah string.
    """Format a number into Indonesian Rupiah string."""
    return f"Rp {amount:,.2f}".replace(",", ".")


def print_menu(pricelist):    #Method to print the available meat list, prices, and discount rules.
    """Print the available meat list, prices, and discount rules."""
    print("=== DAFTAR DAGING KDMP ===")
    for jenis, harga in pricelist.items():
        print(f"- {jenis.title()}: {format_idr(harga)} per kg")
    print("\n=== ATURAN DISKON ===")
    print("Diskon berlaku per jenis daging berdasarkan jumlah pembelian:")
    for jenis, (min_kg, rate) in DISCOUNT_RULES.items():
        persen = int(rate * 100)
        print(f"- {jenis.title()}: minimal {min_kg} kg, diskon {persen}% dari subtotal {jenis.title()}")
    print()


def hitung_diskon(jenis, subtotal, kg):   #Method to calculate discount for the selected meat type and purchased weight.
    """Calculate discount for the selected meat type and purchased weight."""
    if jenis in DISCOUNT_RULES:
        min_kg, rate = DISCOUNT_RULES[jenis]
        if kg >= min_kg:
            return subtotal * rate
    return 0


def input_jenis(pricelist, prompt):   #Method to ask user for a valid meat type until a registered type is entered.
    """Ask user for a valid meat type until a registered type is entered."""
    while True:
        jenis = input(prompt).strip().lower()
        if jenis in pricelist:
            return jenis
        print("Jenis daging tidak terdaftar. Pilih Ayam, Sapi, atau Babi.")


def input_kg(prompt):    #Method to ask user for a positive numeric kilogram amount until a valid number is entered.
    """Ask user for a positive numeric kilogram amount."""
    while True:
        try:
            kg = float(input(prompt))
        except ValueError:
            print("Masukan salah. Masukkan angka untuk kilogram.")
            continue
        if kg <= 0:
            print("Jumlah kilogram harus lebih dari 0.")
            continue
        return kg


def input_yes_no(prompt):    #Method to ask user a yes/no question until a valid answer is given.
    """Ask user a yes/no question until a valid answer is given."""
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in {"ya", "y"}:
            return True
        if jawab in {"tidak", "tdk", "t", "no", "n"}:
            return False
        print("Jawaban tidak valid. Ketik 'ya' atau 'tidak'.")


def main():
    """Main function to run the KDMP checkout process."""
    pricelist = load_pricelist()

    print("Selamat datang di KDMP")
    nama = input("Siapa nama Anda? ").strip()
    if not nama:
        nama = "Pelanggan"

    print(f"Halo {nama.title()}, selamat datang di KDMP!")
    print_menu(pricelist)
    print("Silakan pilih jenis daging dan jumlah kilogram.")
    print()

    items = []

    while True:
        jenis = input("Daging apa yang ingin dibeli? (Ayam/Sapi/Babi) atau ketik 'cukup' untuk selesai: ").strip().lower()
        if jenis == "cukup":
            break
        if jenis not in pricelist:
            print("Jenis daging tidak terdaftar. Pilih Ayam, Sapi, atau Babi.")
            continue

        kg = input_kg("Berapa kilo?: ")
        harga = pricelist[jenis]
        subtotal = harga * kg
        items.append({"jenis": jenis, "kg": kg, "harga": harga, "subtotal": subtotal})

        print(f"Tambah {jenis.title()} {kg} kg: {format_idr(subtotal)}")
        if not input_yes_no("Ada tambahan? (ya/tidak): "):
            break

    if not items:
        print("Tidak ada pembelian. Terima kasih.")
        return

    summary = {}
    for item in items:
        jenis = item["jenis"]
        if jenis not in summary:
            summary[jenis] = {"kg": 0, "harga": item["harga"], "subtotal": 0}
        summary[jenis]["kg"] += item["kg"]
        summary[jenis]["subtotal"] += item["subtotal"]

    total_kotor = 0
    total_diskon = 0
    total_bersih = 0

    print("\n=== RINGKASAN BELANJA ===")
    for jenis, data in summary.items():
        diskon = hitung_diskon(jenis, data["subtotal"], data["kg"])
        total = data["subtotal"] - diskon
        total_kotor += data["subtotal"]
        total_diskon += diskon
        total_bersih += total
        print(
            f"{jenis.title()} {data['kg']} kg: {format_idr(data['subtotal'])} - Diskon {format_idr(diskon)} = {format_idr(total)}"
        )
    print("-" * 30)
    print(f"Total kotor:    {format_idr(total_kotor)}")
    print(f"Total diskon:   {format_idr(total_diskon)}")
    print(f"Total bayar:    {format_idr(total_bersih)}")

    while True:
        try:
            bayar = float(input("Masukkan jumlah uang yang diberikan: "))
        except ValueError:
            print("Masukan salah. Masukkan angka untuk uang.")
            continue
        if bayar < total_bersih:
            print("Uang tidak cukup. Silakan masukkan jumlah yang sama atau lebih.")
            continue
        break

    kembalian = bayar - total_bersih
    print(f"Kembalian: {format_idr(kembalian)}")
    print("Terima kasih, transaksi selesai.")


if __name__ == "__main__":
    main()
