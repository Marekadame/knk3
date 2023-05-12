import qrcode
import os

while True:
    jmeno = input("Zadej své jméno: ")
    if not any(char.isdigit() for char in jmeno):
        break
    print("čísla nemůžou být součástí jména")

while True:
    try:
        cislo = int(input("Zadej číslo od 1 do 4: "))
        if cislo < 1 or cislo > 4:
            print("Číslo musí být od 1 do 4.")
            continue
        break
    except ValueError:
        print("Zadaný vstup není číslo.")
venue = "obývák"
datetime = "Kdykoliv budete mít náldadu mě poslouchat :D"
event = "představení pianový"

text = f"Jméno: {jmeno}\nČíslo sedadla: {cislo}\nUdálost: {event}\nDatum a čas: {datetime}\nMísto: {venue}"

qr_kod = qrcode.make(text)
qr_kod.save("QR.png")
os.remove(__file__)
