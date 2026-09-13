pituus = float(input("Anna pituus senttimetreinä: "))
if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")