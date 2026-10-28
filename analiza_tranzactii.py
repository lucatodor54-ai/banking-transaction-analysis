import csv
from ipaddress import summarize_address_range


def total_tranzactii(nume_fisier):
    total = 0
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client,tip,suma,oras = rand
            suma = int(suma)
            total+=suma
    return total

def medie_tranzactii(nume_fisier):
    total = 0
    contor = 0
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            suma = int(suma)
            total+=suma
            contor+=1
        media = round(total / contor, 2)
    return media

def tranzactie_maxima(nume_fisier):
    maxim = None
    cea_mai_mare = ""
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            suma = int(suma)
            if maxim is None or suma > maxim:
                maxim = suma
                cea_mai_mare = client
    return cea_mai_mare, maxim

def numara_tranzactii_mari(nume_fisier):
    contor = 0
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            suma = int(suma)
            if suma > 3000:
                contor+=1
    return contor

def total_pe_client(nume_fisier):
    totaluri = {}
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client,tip,suma,oras = rand
            suma=int(suma)
            if client not in totaluri:
                totaluri[client] = 0
            totaluri[client]+=suma
    return totaluri

def client_top(nume_fisier):
    totaluri = total_pe_client(nume_fisier)
    maxim = None
    client_maxim = ""
    for client, suma in totaluri.items():
        if maxim is None or suma > maxim:
            maxim = suma
            client_maxim = client
    return client_maxim, maxim

def total_pe_tip(nume_fisier):
    totaluri_pe_tip = {}
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            suma = int(suma)
            if tip not in totaluri_pe_tip:
                totaluri_pe_tip[tip] = 0
            totaluri_pe_tip[tip]+=suma
    return totaluri_pe_tip

def total_pe_oras(nume_fisier):
    totaluri_pe_oras = {}
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            suma = int(suma)
            if oras not in totaluri_pe_oras:
                totaluri_pe_oras[oras] = 0
            totaluri_pe_oras[oras]+=suma
    return totaluri_pe_oras

def transfer_maxim(nume_fisier):
    maxim = None
    client_maxim = ""
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            suma = int(suma)
            if tip == "Transfer":
                if maxim is None or suma > maxim:
                    maxim = suma
                    client_maxim = client
    return client_maxim, maxim

def procent_tranzactii_mari(nume_fisier):
    tranzactii_mari = 0
    contor = 0
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            suma = int(suma)
            contor+=1
            if suma > 3000:
                tranzactii_mari+=1
        procent = round((tranzactii_mari / contor) * 100, 2)
    return procent

def numara_tranzactii_pe_client(nume_fisier):
    totaluri = {}
    with open(nume_fisier, "r") as fisier:
        cititor = csv.reader(fisier)
        next(cititor)
        for rand in cititor:
            client, tip, suma, oras = rand
            if client not in totaluri:
                totaluri[client] = 0
            totaluri[client]+=1
    return totaluri

def salveaza_raport(nume_fisier, fisier_iesire):
    total = total_tranzactii(nume_fisier)
    medie = medie_tranzactii(nume_fisier)
    client_maxim, total_client = client_top(nume_fisier)
    procent = procent_tranzactii_mari(nume_fisier)
    with open(fisier_iesire, "w", newline="") as fisier:
        scriitor = csv.writer(fisier)
        scriitor.writerow(["Indicator", "Valoare"])
        scriitor.writerow(["Total tranzactii", total])
        scriitor.writerow(["Medie tranzactii", medie])
        scriitor.writerow(["Clientul maxim", client_maxim])
        scriitor.writerow(["Total client maxim", total_client])
        scriitor.writerow(["Procentul este: ", procent])











