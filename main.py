from analiza_tranzactii import (
    total_tranzactii,
    medie_tranzactii,
    client_top,
    procent_tranzactii_mari,
    salveaza_raport
)

def main():
    nume_fisier = "tranzactii.csv"
    try:
        total = total_tranzactii(nume_fisier)
        medie = medie_tranzactii(nume_fisier)
        client_maxim, total_maxim = client_top(nume_fisier)
        procent = procent_tranzactii_mari(nume_fisier)
        print("\n=== ANALIZA TRANZACTIILOR BANCARE ===")
        print("Total tranzactii:", total, "lei")
        print("Medie tranzactii:", medie, "lei")
        print("Client cu cel mai mare volum:", client_maxim, "-", total_maxim, "lei")
        print("Procent tranzactii mari:", round(procent, 2), "%")
        salveaza_raport(nume_fisier, "raport_tranzactii.csv")
        print("\nRaportul a fost generat cu succes!")
    except FileNotFoundError:
        print("Eroare: fisierul nu a fost gasit.")
if __name__ == "__main__":
    main()
