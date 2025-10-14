class fileManager:
    def __init__(self):
        self.file_name = "FileDiTesto.txt"

    def leggi_file(self):
        try:
            file = open(self.file_name, 'r') 
            content = file.read()
            file.close()
            return content
        except FileNotFoundError:
            return "File non trovato"

    def scrivi_file(self, content):
        try:
            file = open(self.file_name, 'w')
            file.write(content)
            file.close()
        except Exception as e:
            return "Error"

    def append_su_file(self, content):
        try:
            content = "\n" + content
            file = open(self.file_name, 'a')
            file.write(content)
            file.close()
        except Exception as e:
            return "Errore"
    
    def cancella_file(self):
        file = open(self.file_name, 'w')
        file.write("")
        file.close()
        return "Contenuto del File Cancellato"
        


print("Inizio programma")
file_manager = fileManager()

while True:
    print("""
    Scegli un'opzione: 
    0. Cancella il contenuto del file 
    1. Scrivi 
    2. Leggi 
    3. Aggiungi 
    4. Esci\n""")

    opzione = input("Inserisci il numero dell'opzione scelta: ")

    if opzione == "1": # Scrivi
        contenuto = input("Scrivi qualcosa da scrivere nel file: ")
        file_manager.scrivi_file(contenuto)
    elif opzione == "2": # Leggi
        isNull = file_manager.leggi_file()
        if isNull == "": #Se è vuoto lo faccio presente all'utente
            print("File vuoto")
        else: #Altrimenti stampo il contenuto
            print("Contenuto del file:")
            print(file_manager.leggi_file())
    elif opzione == "3": # Aggiungi in append
        s = input("Scrivi qualcosa da aggiungere al file: ")
        file_manager.append_su_file(s)
        print("Contenuto del file:")
        print(file_manager.leggi_file())
    elif opzione == "4": # Esci
        print("Uscita dal programma")
        break
    elif opzione == "0": # Cancella il contenuto del file
        print(file_manager.cancella_file())
    else:
        print("Opzione non valida, riprova")


