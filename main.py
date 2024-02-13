import tkinter as tk                
import time
import re

class Osoba:
    # konstruktor, baza
    def __init__(self, ime, prezime, sifra, balance, stanje=True):
        self.ime = ime
        self.prezime = prezime
        self.sifra = sifra
        self.stanje = stanje
        self.balance = balance
    
    def __str__(self):
        return f"Dobrodošli {self.ime} {self.prezime}!"

    # Funkcija koja vraca stanje racuna
    # Stanje racuna moze biti Aktivno(True) ili Zatvoren(False)
    def state(self):
        if self.stanje == True:
            return f"Stanje racuna: Aktivan"
        else:
            return f"Stanje racuna: Zatvoren"

    #Funkcija koja vraca sumu novca na racunu
    def returnBalance(self):
        return self.balance

    # Funkcija koja vraca sifru
    def password(self):
        return self.sifra

    #Funkcija koja vraca sve podatke korisnika
    def podaci(self):
        return [self.ime, self.prezime, self.stanje, self.sifra]

# Klasa u kojoj se odvija menjanje stranica
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            # stavlja sve stranice na istu lokaciju 
            # ona na vrhu ce biti ona koja je vidljiva
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Pokazi mi frejm prema njegovom imenu'''
        frame = self.frames[page_name]
        frame.tkraise()

# Klasa za pocetnu stranicu i sve opcije u njoj 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#00004d')
        self.controller = controller

        self.controller.title('Bankomat')
        self.controller.state('zoomed')
        self.controller.iconphoto(False, 
                        tk.PhotoImage(file='E:/bankomatApp/src/components/atm.png'))

        headinLabel1 = tk.Label(self,
                                text='Bankomat x3000',
                                font=('Tahoma', 44, 'bold'),
                                foreground='white',
                                background='#00004d')
        headinLabel1.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#00004d')
        space_label.pack()

        password_label = tk.Label(self, 
                                text='Unesite lozinku',
                                font=('Tahoma', 16),
                                bg='#00004d',
                                fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()   # kazemo masini kakvog je tipa sifra koja se uzima
        password_entryBox = tk.Entry(self,
                                    textvariable=my_password,
                                    font=('Tahoma', 16),
                                    show='*',
                                    width=22)
        password_entryBox.pack(ipady=7)
                                    
        def check_password():
            if my_password.get() == data[2]:
                controller.show_frame('MenuPage')
                my_password.set('') # nakon stiskanja Exit buttona brise sifru iz entry boxa
                incorrect_passwordLabel['text']=''
            else:
                incorrect_passwordLabel['text']='Pogresna šifra'
        enter_button = tk.Button(self,
                                text='Enter',
                                command=check_password,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3)
        enter_button.pack(pady=10)

        incorrect_passwordLabel = tk.Label(self,
                                        text='',
                                        font=('Tahoma', 16),
                                        foreground='white',
                                        bg='#000033',
                                        anchor='n')
        incorrect_passwordLabel.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/visa.png')
        visaLabel = tk.Label(bottom_frame, image=visa_photo)
        visaLabel.pack(side='left')
        visaLabel.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/master.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
        
        def tick():
            current_time = time.strftime('%I:%M:%p').lstrip('0').replace('0','')    # makne se nula sa sata
            time_label.configure(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame, font=('Tahoma', 12))
        time_label.pack(side='right')

        tick()

# Klasa za stranicu sa glavnim menijem i njegovim f-jama
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#00004d')
        self.controller = controller

        headinLabel1 = tk.Label(self,
                                text='Bankomat x3000',
                                font=('Tahoma', 44, 'bold'),
                                foreground='white',
                                background='#00004d')
        headinLabel1.pack(pady=25)

        main_menuLabel = tk.Label(self, 
                                text='Glavni Meni',
                                font=('Tahoma', 14),
                                fg='white',
                                bg='#00004d')
        main_menuLabel.pack()

        selection_label = tk.Label(self,
                                text='Izaberite dalju opciju',
                                font=('Tahoma',14),
                                fg='white',
                                bg='#00004d',
                                anchor='w') # da tekst bude lociran na levo w - west
        selection_label.pack(fill='x') 

        button_frame = tk.Frame(self, bg='#000033')
        button_frame.pack(fill='both', expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
        
        withdraw_button = tk.Button(button_frame,
                                    text='Podizanje gotovine',
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        withdraw_button.grid(row=0, column=0, pady=5)

        def deposit():
            controller.show_frame('DepositPage')
        
        deposit_button = tk.Button(button_frame,
                                    text='Uplata',
                                    command=deposit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        def balance():
            controller.show_frame('BalancePage')
        
        balance_button = tk.Button(button_frame,
                                    text='Provera stanja',
                                    command=balance,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        balance_button.grid(row=2, column=0, pady=5)

        def exit():
            controller.show_frame('StartPage')
        
        exit_button = tk.Button(button_frame,
                                    text='Izlaz',
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        exit_button.grid(row=3, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/visa.png')
        visaLabel = tk.Label(bottom_frame, image=visa_photo)
        visaLabel.pack(side='left')
        visaLabel.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/master.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        def tick():
            current_time = time.strftime('%I:%M:%p').lstrip('0').replace('0','')    # makne se nula sa sata
            time_label.configure(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame, font=('Tahoma', 12))
        time_label.pack(side='right')

        tick()

# Funkcija za podizanje gotovine
class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#00004d')
        self.controller = controller

        headinLabel1 = tk.Label(self,
                                text='Bankomat x3000',
                                font=('Tahoma', 44, 'bold'),
                                foreground='white',
                                background='#00004d')
        headinLabel1.pack(pady=25)

        chose_amount_Label = tk.Label(self, 
                                text='Odaberite iznos koji zelite podići',
                                font=('Tahoma', 14),
                                fg='white',
                                bg='#00004d')
        chose_amount_Label.pack()

        button_frame = tk.Frame(self, bg='#000033')
        button_frame.pack(fill='both', expand=True)

        def withdraw(amount):
            global current_balance
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            # Podaci iz baze
            with open("E:/bankomatApp/src/components/file.txt", "r") as f:
                file_content = f.read()
                data = re.findall("'(.*?)'", file_content)

                f.close()

            with open("E:/bankomatApp/src/components/file.txt", "w") as f:
                data[4] = int(data[4]) - amount
                f.write("{ime:'"+str(data[0])+"',prezime:'"+str(data[1])+"',sifra:'"+str(data[2])+"',status:'"+str(data[3])+"',balance:'"+str(data[4])+"'} ")
                f.close()
                    
        button500 = tk.Button(button_frame,
                            text='500',
                            command=lambda:withdraw(500),
                            relief='raised',
                            borderwidth=3,
                            width=50,
                            height=5)
        button500.grid(row=0, column=0, pady=5)

        button1000 = tk.Button(button_frame,
                            text='1000',
                            command=lambda:withdraw(1000),
                            relief='raised',
                            borderwidth=3,
                            width=50,
                            height=5)
        button1000.grid(row=1, column=0, pady=5)

        button2000 = tk.Button(button_frame,
                            text='2000',
                            command=lambda:withdraw(2000),
                            relief='raised',
                            borderwidth=3,
                            width=50,
                            height=5)
        button2000.grid(row=2, column=0, pady=5)

        button5000 = tk.Button(button_frame,
                            text='5000',
                            command=lambda:withdraw(5000),
                            relief='raised',
                            borderwidth=3,
                            width=50,
                            height=5)
        button5000.grid(row=0, column=1, pady=5, padx=555)

        button10000 = tk.Button(button_frame,
                            text='10000',
                            command=lambda:withdraw(10000),
                            relief='raised',
                            borderwidth=3,
                            width=50,
                            height=5)
        button10000.grid(row=1, column=1, pady=5, padx=555)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,
                                    textvariable=cash,
                                    width=59,
                                    justify='right')    # tekst da se kuca desno
        other_amount_entry.grid(row=2, column=1, pady=5, padx=555, ipady=30)
        
        other_amount_label = tk.Label(button_frame,
                                    text='Drugi iznos',
                                    font=('Tahoma', 14),
                                    fg='white',
                                    bg='#00004d')
        other_amount_label.grid(row=3, column=1, pady=5, padx=555)
        # da korisnik moze uneti iznos novca koji zeli podici
        def other_amount(am): 
            am = eval(other_amount_entry.get()) # hvatanje vrednosti sa inputa
            global current_balance
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')

            # Podaci iz baze
            with open("E:/bankomatApp/src/components/file.txt", "r") as f:
                file_content = f.read()
                data = re.findall("'(.*?)'", file_content)
                f.close()
                
            with open("E:/bankomatApp/src/components/file.txt", "w") as f:
                data[4] = int(data[4]) - am # ubacujemo u txt fajl uhvacenu vrednost sa inputa
                f.write("{ime:'"+str(data[0])+"',prezime:'"+str(data[1])+"',sifra:'"+str(data[2])+"',status:'"+str(data[3])+"',balance:'"+str(data[4])+"'} ")
                f.close()

        other_amount_entry.bind('<Return>', other_amount)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/visa.png')
        visaLabel = tk.Label(bottom_frame, image=visa_photo)
        visaLabel.pack(side='left')
        visaLabel.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/master.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
        
        def tick():
            current_time = time.strftime('%I:%M:%p').lstrip('0').replace('0','')    # makne se nula sa sata
            time_label.configure(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame, font=('Tahoma', 12))
        time_label.pack(side='right')

        tick()

# Funkcija za uplatu novca na račun
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#00004d')
        self.controller = controller

        headinLabel1 = tk.Label(self,
                                text='Bankomat x3000',
                                font=('Tahoma', 44, 'bold'),
                                foreground='white',
                                background='#00004d')
        headinLabel1.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#00004d')
        space_label.pack()

        enter_amount_label = tk.Label(self, 
                                text='Unesite svotu',
                                font=('Tahoma', 16),
                                bg='#00004d',
                                fg='white')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposite_entry = tk.Entry(self,
                                textvariable=cash,
                                font=('Tahoma',14),
                                width=28)
        deposite_entry.pack(ipady=7)

        def deposit_cash(): 
            am = eval(deposite_entry.get()) # hvatanje vrednosti sa inputa
            global current_balance
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')

            # Podaci iz baze
            with open("E:/bankomatApp/src/components/file.txt", "r") as f:
                file_content = f.read()
                data = re.findall("'(.*?)'", file_content)
                f.close()
                
            with open("E:/bankomatApp/src/components/file.txt", "w") as f:
                data[4] = int(data[4]) + am # ubacujemo u txt fajl uhvacenu vrednost sa inputa
                f.write("{ime:'"+str(data[0])+"',prezime:'"+str(data[1])+"',sifra:'"+str(data[2])+"',status:'"+str(data[3])+"',balance:'"+str(data[4])+"'} ")
                f.close()
           
        enter_button = tk.Button(self,
                                text='Enter',
                                command=deposit_cash,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self, bg='#000033')
        two_tone_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/visa.png')
        visaLabel = tk.Label(bottom_frame, image=visa_photo)
        visaLabel.pack(side='left')
        visaLabel.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/master.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
        
        def tick():
            current_time = time.strftime('%I:%M:%p').lstrip('0').replace('0','')    # makne se nula sa sata
            time_label.configure(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame, font=('Tahoma', 12))
        time_label.pack(side='right')

        tick()
# Funkcija za proveru stanja na računu
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#00004d')
        self.controller = controller

        headinLabel1 = tk.Label(self,
                                text='Bankomat x3000',
                                font=('Tahoma', 44, 'bold'),
                                foreground='white',
                                background='#00004d')
        headinLabel1.pack(pady=25)

        global current_balance
        controller.shared_data['Balance'].set(data[4])
        balance_label = tk.Label(self,
                                textvariable=controller.shared_data['Balance'],
                                font=('Tahoma', 14),
                                foreground='white',
                                background='#00004d',
                                anchor='w')
        balance_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#000033')
        button_frame.pack(fill='both', expand=True)

        def menu():
            controller.show_frame('MenuPage')

        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Glavni Meni',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=0, column=0, pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                text='Izlaz',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=1, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        
        visa_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/visa.png')
        visaLabel = tk.Label(bottom_frame, image=visa_photo)
        visaLabel.pack(side='left')
        visaLabel.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='E:/bankomatApp/src/components/master.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
        
        def tick():
            current_time = time.strftime('%I:%M:%p').lstrip('0').replace('0','')    # makne se nula sa sata
            time_label.configure(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame, font=('Tahoma', 12))
        time_label.pack(side='right')

        tick()

if __name__ == "__main__":

    # Podaci iz baze
    #Regex =   r"   \"\w{0,}\" "g ili Regex = \" (.*?) \"
    with open("E:/bankomatApp/src/components/file.txt", "r") as f:
        file_content = f.read()
        # print(file_content)
        # print(re.search("\"\w{0,}\"", file_content))
        data = re.findall("'(.*?)'", file_content)
        print (data)
        f.close()


    O = Osoba(data[0],data[1],data[2],data[3],data[4])
    print(O)
    current_balance = O.returnBalance()
    
    app = SampleApp()
    app.mainloop() #pokretanje glavne petlje