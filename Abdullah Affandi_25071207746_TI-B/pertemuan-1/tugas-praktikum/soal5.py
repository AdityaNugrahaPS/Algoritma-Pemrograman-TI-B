def hitung(a: float, b: float) -> tuple[float, float]:
    """
    Mengembalikan penjumlahan dan pengurangan dua bilangan
    """
    return a + b, a - b

tambah, kurang = hitung(9999, 20000)
print(f"Penjumlahan = {tambah}")
print(f"Pengurangan = {kurang}")