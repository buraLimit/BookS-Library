from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from konekcijaSaBazom import konekcija

LARGEFONT = ("Verdana", 14)

class PageClan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        rightFrame = tk.Frame(self)
        rightFrame.grid(row=1, column=2, rowspan=6, columnspan=3)
        scroll = Scrollbar(rightFrame, orient=VERTICAL)

        # DRVO ZA Clanove
        self.treeClan = ttk.Treeview(rightFrame, height=12, columns=("ID", "Ime", "Prezime", "Adresa", "Broj", "Email"),yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)


        frame = Frame (self)
        # Ime
        labelIme = ttk.Label(self, text="Ime: ", font= LARGEFONT)
        labelIme.grid(row=0, column=0, padx=10, pady=10)
        entryIme = ttk.Entry(self, width=20)
        entryIme.grid(row=0, column=1, padx=10, pady=10, ipady = 4)

        # Prezime
        labelPrezime= ttk.Label(self, text="Prezime: ", font= LARGEFONT)
        labelPrezime.grid(row=1, column=0, padx=10, pady=10)
        entryPrezime = ttk.Entry(self, width=20)
        entryPrezime.grid(row=1, column=1, padx=10, pady=10, ipady = 4)

        # Adresa
        labelAdresa = ttk.Label(self, text="Adresa: ", font= LARGEFONT)
        labelAdresa.grid(row=2, column=0, padx=10, pady=10)
        entryAdresa = ttk.Entry(self, width=20)
        entryAdresa.grid(row=2, column=1, padx=10, pady=10, ipady = 4)

        # Broj
        labelBroj = ttk.Label(self, text="Broj: ", font= LARGEFONT)
        labelBroj.grid(row=3, column=0, padx=10, pady=10)
        entryBroj = ttk.Entry(self, width=20)
        entryBroj.grid(row=3, column=1, padx=10, pady=10, ipady = 4)

        # Email
        labelEmail = ttk.Label(self, text="Email: ", font= LARGEFONT)
        labelEmail.grid(row=4, column=0, padx=10, pady=10)
        entryEmail = ttk.Entry(self, width=20)
        entryEmail.grid(row=4, column=1, padx=10, pady=10, ipady = 4)

        #unosi novog korisnika
        def FNunosClanova():
            if entryIme.get()=='' or entryPrezime.get()=='' or  entryAdresa.get()=='' or  entryBroj.get()=='':
                messagebox.showerror(title='Greska', message="Sva polja osim mejla su obavezna!")
            else:
                try:
                    konekcija.cursor.callproc('pro_unesiKorisnika', [entryIme.get(), entryPrezime.get(), entryAdresa.get(), entryBroj.get(), entryEmail.get()])
                    konekcija.db.commit()
                    messagebox.showinfo(title='Obavestenje', message="Uspesno ste upisali novog clana")
                    self.prikazClanova()
                    entryIme.delete(0,END)
                    entryPrezime.delete(0,END)
                    entryBroj.delete(0,END)
                    entryAdresa.delete(0,END)
                    entryEmail.delete(0,END)
                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()





        #ISPISUJE U POLJA PODATKE
        def popuniZaIzmenu(nesto):
            clan = self.treeClan.focus()
            podaci = self.treeClan.item(clan)
            red = podaci['values']
            global id1
            id1 = red[0]

            entryIme.delete(0, END)
            entryIme.insert(0, red[1])
            entryPrezime.delete(0, END)
            entryPrezime.insert(0, red[2])
            entryAdresa.delete(0, END)
            entryAdresa.insert(0, red[3])
            entryBroj.delete(0, END)
            entryBroj.insert(0, red[4])
            entryEmail.delete(0, END)
            entryEmail.insert(0, red[5])

        #MENJA CLANA
        def izmeniClana():
            clan = self.treeClan.focus()
            podaci = self.treeClan.item(clan)
            red = podaci['values']
            try:
                id1 = int(red[0])
                print(id1)
            except:
                print("Nije selektovan nijedan clan!")

            if entryIme.get()=='' or entryPrezime.get()=='' or  entryAdresa.get()=='' or  entryBroj.get()=='':
                messagebox.showerror(title='Greska', message="Niste obelezili nijednog clana!")
            else:
                try:
                    konekcija.cursor.callproc('pro_updateKorisnik', [id1, entryIme.get(), entryPrezime.get(), entryAdresa.get(), entryBroj.get(), entryEmail.get()])
                    konekcija.db.commit()
                    messagebox.showinfo(title='Obavestenje', message="Uspesno ste izmenili podatke")
                    self.prikazClanova()
                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()

        #BRISE CLANA
        def obrisiClana():
            clan = self.treeClan.focus()
            podaci = self.treeClan.item(clan)

            red = podaci['values']
            try:
                id1 = int(red[0])
                print(id1)
            except:
                print("Nije selektovan nijedan clan!")

            if entryIme.get()=='' or entryPrezime.get()=='' or  entryAdresa.get()=='' or  entryBroj.get()=='':
                messagebox.showerror(title='Greska', message="Niste obelezili nijednog clana!")
            else:
                try:
                    text1 = konekcija.cursor.callproc('pro_obrisiKorisnika', [id1, ''])
                    konekcija.db.commit()
                    messagebox.showinfo(title='Obavestenje', message=str(text1[1]))

                    entryIme.delete(0, END)
                    entryPrezime.delete(0, END)
                    entryAdresa.delete(0, END)
                    entryBroj.delete(0, END)
                    entryEmail.delete(0, END)

                    self.prikazClanova()
                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()

        #Pronalazi clana
        def nadjiClana():
            if entryImePretraga.get() == '' or entryPrezimePretraga.get() == '':
                messagebox.showerror(title='Greska', message="Morate popuniti oba polja!")
            else:
                try:
                    print(entryImePretraga.get())
                    konekcija.cursor.execute(f'SELECT * FROM korisnik WHERE ime = "{entryImePretraga.get()}" AND prezime = "{entryPrezimePretraga.get()}";')
                    print('PROSAO exec')
                    result = konekcija.cursor.fetchall()

                    if len(result) != 0:
                        print('NASAO NESTO')
                        top = tk.Toplevel()
                        top.title("Rezultat pretrage")
                        top.geometry("900x200+600+350")
                        pretragaFrame = tk.Frame(top)
                        pretragaFrame.pack(anchor='center', fill='both', expand=True, padx=15, pady=15)
                        scroll = Scrollbar(pretragaFrame, orient=VERTICAL)

                        treePretragaClana = ttk.Treeview(pretragaFrame, height=12, columns=("ID", "Ime", "Prezime", "Adresa", "Broj", "Email"), yscrollcommand=scroll.set,show='headings')
                        scroll.pack(side=RIGHT, fill=Y)

                        treePretragaClana.heading("ID", text="ID")
                        treePretragaClana.heading("Ime", text="Ime")
                        treePretragaClana.heading("Prezime", text="Prezime")
                        treePretragaClana.heading("Adresa", text="Adresa")
                        treePretragaClana.heading("Broj", text="Broj")
                        treePretragaClana.heading("Email", text="Email")


                        treePretragaClana.column("ID", width=15, anchor=CENTER)
                        treePretragaClana.column("Ime", width=70, anchor=CENTER)
                        treePretragaClana.column("Prezime", width=80, anchor=CENTER)
                        treePretragaClana.column("Adresa", width=130, anchor=CENTER)
                        treePretragaClana.column("Broj", width=100, anchor=CENTER)
                        treePretragaClana.column("Email", width=120, anchor=CENTER)

                        treePretragaClana.pack(fill=BOTH, expand=1)
                        for row in result:
                            treePretragaClana.insert('',END,values=row)

                    else:
                        messagebox.showinfo(title='Obavestenje', message='Clan ne postoji')

                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()

        #DUGMAD
        btnUnos = ttk.Button(self, text="Unos clana",command=lambda: FNunosClanova(), width=20)
        btnUnos.grid(row=5, column=0, padx=10, pady=10, ipady = 8)
        btnIzmena = ttk.Button(self, text="Izmena clana", command=lambda: izmeniClana(), width=20)
        btnIzmena.grid(row=5, column=1, padx=10, pady=10, ipady = 8)
        btnObrisi = ttk.Button(self, text="Obrisi clana", command=lambda: obrisiClana(), width=20)
        btnObrisi.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipady = 8)
        btnNazad = ttk.Button(self, text="Nazad", width=20, command=lambda: controller.show_frame('StartPage'))
        btnNazad.grid(row=9, column=3, padx=10, pady=10,rowspan=2, ipady = 8)

        btnNadji = ttk.Button(self, text="Pronadji clana", width=20, command=lambda: nadjiClana())
        btnNadji.grid(row=9, column=2, padx=10, pady=10,rowspan=2, ipady = 8)


        #IME PRETRAGA
        labelImePretraga = ttk.Label(self, text="Ime za pretragu: ", font= LARGEFONT)
        labelImePretraga.grid(row=9, column=0, padx=10, pady=10)
        entryImePretraga = ttk.Entry(self, width=20)
        entryImePretraga.grid(row=9, column=1, padx=10, pady=10, ipady = 4)

        # Prezime PRETRAGA
        labelPrezimePretraga = ttk.Label(self, text="Prezime za pretragu: ", font= LARGEFONT)
        labelPrezimePretraga.grid(row=10, column=0, padx=10, pady=10)
        entryPrezimePretraga = ttk.Entry(self, width=20)
        entryPrezimePretraga.grid(row=10, column=1, padx=10, pady=10, ipady = 4)

        #FRAME ZA DRVO
        rightFrame = tk.Frame(self)
        rightFrame.grid(row=1,column=2,rowspan=6,columnspan =3)
        scroll = Scrollbar(rightFrame, orient=VERTICAL)

         #DRVO ZA Clanove
        self.treeClan = ttk.Treeview(rightFrame,height=12,columns=("ID", "Ime", "Prezime", "Adresa", "Broj", "Email"),yscrollcommand = scroll.set)
        scroll.pack(side=RIGHT,fill=Y)

        self.treeClan.heading("ID",text="ID")
        self.treeClan.heading("Ime",text="Ime")
        self.treeClan.heading("Prezime",text="Prezime")
        self.treeClan.heading("Adresa",text="Adresa")
        self.treeClan.heading("Broj",text="Broj")
        self.treeClan.heading("Email",text="Email")
        self.treeClan['show']='headings'

        self.treeClan.column("ID", width=15,anchor=CENTER)
        self.treeClan.column("Ime", width=70,anchor=CENTER)
        self.treeClan.column("Prezime", width=80,anchor=CENTER)
        self.treeClan.column("Adresa", width=130,anchor=CENTER)
        self.treeClan.column("Broj", width=100,anchor=CENTER)
        self.treeClan.column("Email", width=120,anchor=CENTER)

        self.treeClan.pack(fill=BOTH,expand=1)
        self.treeClan.bind("<ButtonRelease-1>", popuniZaIzmenu)
        self.prikazClanova()

        # prikaz clanova
    def prikazClanova(self):
        konekcija.cursor.execute("select * from korisnik")
        result = konekcija.cursor.fetchall()
        if len(result) != 0:
            self.treeClan.delete(*self.treeClan.get_children())
            for row in result:
                self.treeClan.insert('', END, values=row)
        konekcija.db.commit()