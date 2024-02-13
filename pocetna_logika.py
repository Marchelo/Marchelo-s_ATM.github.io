import time
class Osoba:
    # konstruktor, baza
    def __init__(self, ime, prezime, sifra, stanje=True, balance=0):
        self.ime = ime
        self.prezime = prezime
        self.sifra = sifra
        self.stanje = stanje
        # self.balans = balance
    
    def __str__(self):
        return f"Pozdrav {self.ime} {self.prezime}"

    # Funkcija koja vraca stanje racuna
    # Stanje racuna moze biti Aktivno(True) ili Zatvoren(False)
    def state(self):
        if self.stanje == True:
            return f"Stanje racuna: Aktivan"
        else:
            return f"Stanje racuna: Zatvoren"

    # Funkcija koja vraca sifru
    def password(self):
        return self.sifra

    #Funkcija koja vraca sve podatke korisnika
    def podaci(self):
        return [self.ime, self.prezime, self.stanje, self.sifra]


if __name__ == "__main__":

    # Baza
    # regex = {Osoba1:{ime:Luka,prezime:Drobnjak}}
    # for 
    O = Osoba("Luka","Drobnjak", 4425, True)
    
    # Napravi funkcije
    # Validacija korisnika
    # Provera stanja
    # Podizanje gotovine 

    # print(O1.stanje)
    # Bankmant
    print('Ubacite svoju karticu!')
    time.sleep(3)
    # Prva funkcija nam je najbitnija, jer ona vraca podatak da li je korisnik validan.
    # Ako korisnik nije validan, treba da mu izbaci gresku.
    # Ako je korisnik validan, treba da mu izbaci glavni prozor gde moze da vrsi ostale funkcije.
    # Validaciju korisnika cemo proveriti preko sledecih podataka: IME, PREZIME, SIFRA.
    # Posto ce podaci o korisniku biti u formi liste: [ime, prezime, stanje, sifra], pristupamo samo sifri.
    def user_validation(password, user):
        if password == user[3]:
            print("\nDobrodosli u ATM x3000!\nIzaberite dalju opciju.")
            print("""1 == Provera stanja\n2 == Podizanje gotovine\n3 == Izlaz""") # f"{Provera stanja}{Validacija korisnika}{Izlaz}"
            todo = int(input("Opcija: "))
            if todo == 1:
                print("\nIzabrali ste proveru stanja.\nVase trenutno stanje racuna je ..funkcija koja vraca stanje novca na racunu.. \n")
            elif todo == 2:
                opt2()
            elif todo == 3:
                print("\nIzlazak iz programa.\nUzmite vasu karticu.")
        else:
            print("Pogresno uneta sifra, pokusajte ponovo.")

    def opt2():
        print("""\nOdaberite iznos koji zelite podici sa racuna.
1 == 500        2 == 1000       3 == 2000
4 == 5000       5 == 10000      6 == Drugi iznos""")
        opt =  int(input("Opcija koju zelite: "))
        if opt == 1 or opt == 2 or opt == 3 or opt == 4 or opt == 5:
            print("\nVasa transakcija se izvrsava..")
            time.sleep(2)
            print("Transakcija je izvrsena, uzmite Vasu karticu.")
        elif opt == 6:
            int(input("\nDrugi iznos koji zelite podici je: "))
            time.sleep(2)
            print("Vasa transakcija se izvrsava..")
            time.sleep(2)
            print("Transakcija je izvrsena, uzmite Vasu karticu.")
        else:
            print("\nPogresan unos!")

i = input("Korisničko ime: ")
s = int(input("Šifra: "))
user_validation(s, O.podaci())
