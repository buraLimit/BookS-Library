from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
from konekcijaSaBazom import konekcija

LARGEFONT = ("Verdana", 14)

class PageKnjiga(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = Frame(self)
        frame.pack(anchor='center', pady=70)

        # Naslov
        labelNaslov = ttk.Label(frame, text="Naslov: ", font = LARGEFONT)
        labelNaslov.grid(row=0, column=0, padx=10, pady=10)
        entryNaslov = ttk.Entry(frame, width=25)
        entryNaslov.grid(row=0, column=1, padx=10, pady=10, ipady = 4)

        # AUTOR
        labelAutor= ttk.Label(frame, text="Autor: ", font = LARGEFONT)
        labelAutor.grid(row=1, column=0, padx=10, pady=10)
        global comboboxAutora
        comboboxAutora = AutocompleteCombobox(frame, width=22)
        comboboxAutora.grid(row=1, column=1, padx=10, pady=10, ipady=4)
        PageKnjiga.autori(self)

        # Izdanje
        labelIzdanje = ttk.Label(frame, text="Izdanje: ", font = LARGEFONT)
        labelIzdanje.grid(row=2, column=0, padx=10, pady=10)
        entryIzdanje = ttk.Entry(frame, width=25)
        entryIzdanje.grid(row=2, column=1, padx=10, pady=10, ipady = 4)

        # GODINA
        labelGodina = ttk.Label(frame, text="Godina: ", font = LARGEFONT)
        labelGodina.grid(row=3, column=0, padx=10, pady=10)
        entryGodina = ttk.Entry(frame, width=25)
        entryGodina.grid(row=3, column=1, padx=10, pady=10, ipady = 4)

        # ISBN
        labelISBN = ttk.Label(frame, text="ISBN: ", font = LARGEFONT)
        labelISBN.grid(row=0, column=2, padx=10, pady=10)
        entryISBN = ttk.Entry(frame, width=25)
        entryISBN.grid(row=0, column=3, padx=10, pady=10, ipady = 4)

        #Kategorija
        labelKategorija = ttk.Label(frame, text="Kategorija: ", font = LARGEFONT)
        labelKategorija.grid(row=1, column=2, padx=10, pady=10)
        global comboboxKategorija
        comboboxKategorija = AutocompleteCombobox(frame, width=22)
        comboboxKategorija.grid(row=1, column=3, padx=10, pady=10, ipady=4)
        PageKnjiga.kategorije(self)

        #Izdavac
        labelIzdavac = ttk.Label(frame, text="Izdavac: ", font = LARGEFONT)
        labelIzdavac.grid(row=2, column=2, padx=10, pady=10)
        global comboboxIzdavac
        comboboxIzdavac = AutocompleteCombobox(frame,width=22)
        comboboxIzdavac.grid(row=2, column=3, padx=10, pady=10, ipady=4)
        PageKnjiga.izdavaci(self)

        #Kolicina
        labelKolicina = ttk.Label(frame, text="Kolicina: ", font=LARGEFONT)
        labelKolicina.grid(row=3, column=2, padx=10, pady=10)
        entryKolicina = ttk.Entry(frame, width=25)
        entryKolicina.grid(row=3, column=3, padx=10, pady=10, ipady=4)

        def dodajKnjigu():

            if entryNaslov.get()=='' or entryIzdanje.get()=='' or  entryGodina.get()=='' or  entryISBN.get()=='' or entryKolicina.get()=='' or comboboxAutora.get()=='' or comboboxIzdavac.get() == '' or comboboxKategorija.get()=='':
                messagebox.showerror(title='Greska', message="Sva polja morate da popunite!")
            else:
                try:
                    konekcija.cursor.callproc('pro_dodajKnjigu', [entryNaslov.get(), comboboxAutora.get(), entryIzdanje.get(), entryGodina.get(), entryISBN.get(), comboboxKategorija.get(), comboboxIzdavac.get(), entryKolicina.get(), ''])
                    konekcija.db.commit()
                    messagebox.showinfo(title='Obavestenje', message="Uspesno ste dodali knjigu!")
                    entryNaslov.delete(0,END)
                    entryIzdanje.delete(0,END)
                    entryGodina.delete(0,END)
                    entryKolicina.delete(0,END)
                    entryISBN.delete(0,END)
                    comboboxKategorija.delete(0,END)
                    comboboxIzdavac.delete(0,END)
                    comboboxAutora.delete(0,END)
                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()
                    messagebox.showerror(title='Greska', message="Neki od podataka je pogresno unet!")



        btnNazad = ttk.Button(frame, text="Nazad", width=22, command=lambda: controller.show_frame('StartPage'))
        btnNazad.grid(row=2, column=4, padx=10, pady=10, columnspan=2, ipady = 8)
        btnDodajKnjigu = ttk.Button(frame, text="Dodaj knjigu", width=22, command=lambda: dodajKnjigu())
        btnDodajKnjigu.grid(row=1, column=4, padx=10, pady=10, columnspan=2, ipady = 8)

    def kategorije(self):
        listaKategorija = []
        konekcija.cursor.execute("select * from kategorija")
        resultK = konekcija.cursor.fetchall()
        for row in resultK:
            listaKategorija.append(str(row[1]))
        konekcija.db.commit()
        comboboxKategorija['completevalues'] = listaKategorija
        print(listaKategorija)

    def autori(self):
        listaAutora = []
        konekcija.cursor.execute("select * from autor")
        resultA = konekcija.cursor.fetchall()
        for row in resultA:
            listaAutora.append(str(row[1]))
        konekcija.db.commit()
        comboboxAutora['completevalues'] = listaAutora

    def izdavaci(self):
        listaIzdavac = []
        konekcija.cursor.execute("select * from izdavac")
        resultIz = konekcija.cursor.fetchall()
        for row in resultIz:
            listaIzdavac.append(str(row[1]))
        konekcija.db.commit()
        comboboxIzdavac['completevalues'] = listaIzdavac
