from math import pow
from time import sleep

class Calcolatrice:
    def imposta_numeri(self, n1, n2):
        self.numero1 = n1
        self.numero2 = n2

    def somma(self):
        return self.numero1 + self.numero2
    
    def sottrazione(self):
        return self.numero1 - self.numero2
    
    def moltiplicazione(self):
        return self.numero1 * self.numero2
    
    def divisione(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Errore: Divisione per zero"

    def potenza(self):
        return pow(self.numero1, self.numero2)

    def radice(self):
        if self.numero1 >= 0:
            return pow(self.numero1, 1 / self.numero2)
        else:
            return "Errore: Radice di numero negativo"
    
    def reset(self):
        self.numero1 = None
        self.numero2 = None
    
calc = Calcolatrice()

operazioni_disponibili = {
    '1': calc.somma,
    '2': calc.sottrazione,
    '3': calc.moltiplicazione,
    '4': calc.divisione,
    '5': calc.potenza,
    '6': calc.radice
}

while True:
    print("""Operazioni disponibili:
      1. Somma
      2. Sottrazione
      3. Moltiplicazione
      4. Divisione
      5. Potenza
      6. Radice
      7. Esci""")

    operazione = input("Scegli l'operazione (1-7): ")

    if operazione == '7':
        print("Uscita dalla calcolatrice.")
        break

    if operazione not in operazioni_disponibili:
        print("Operazione non valida.")
        continue

    n1 = float(input("Inserisci il primo numero: "))
    n2 = float(input("Inserisci il secondo numero: "))
    calc.imposta_numeri(n1, n2)

    risultato = operazioni_disponibili[operazione]()
    print("Risultato:", risultato)
    calc.reset()
    sleep(1)

