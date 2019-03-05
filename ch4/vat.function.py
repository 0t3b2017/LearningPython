def calculate_proce_with_vat(price, vat):
    return price * (100 + vat) / 100

print(calculate_proce_with_vat(100, 5.0))
