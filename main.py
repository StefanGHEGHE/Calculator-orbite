import math

# Constante
R_PAMANT_M = 6371_000
G = 6.67430e-11
M_PAMANT = 5.972e24

def calculeaza_orbita(alt_km):
    if alt_km < 160:
        print("Altitudine prea mica.")
        return None, None

    r = R_PAMANT_M + (alt_km * 1000)
    
    viteza_kms = math.sqrt((G * M_PAMANT) / r) / 1000
    perioada_min = (2 * math.pi * math.sqrt((r**3) / (G * M_PAMANT))) / 60
    
    return viteza_kms, perioada_min

def main():
    print("Calculator Traiectorii")
    
    while True:
        cmd = input("Altitudine (km) [sau 'q' pentru exit]: ").strip()
        
        if cmd.lower() == 'q':
            print("Sistem oprit. Zbor lin!")
            break
            
        try:
            alt = float(cmd)
            viteza, timp = calculeaza_orbita(alt)
            
            if viteza and timp:
                print(f" > Viteza: {viteza:.2f} km/s | Perioada: {timp:.2f} min")
        except ValueError:
            print("Eroare: Introdu un număr valid.")

if __name__ == "__main__":
    main()