def gallonat_litroiksi(gallonat):
    return gallonat * 3.785
gallonat = float(input("Anna gallonamäärä: "))
while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.2f} litraa")
    gallonat = float(input("Anna gallonamäärä: "))