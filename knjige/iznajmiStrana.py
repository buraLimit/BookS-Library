from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from konekcijaSaBazom import konekcija

LARGEFONT = ("Verdana", 14)

class PageIznajmi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = Frame(self)
        frame.pack(anchor='center', pady=60)

        #Iznajmi
        labelKorisnik = ttk.Label(frame, text="ID korisnika: ", font = LARGEFONT)
        labelKorisnik.grid(row=0, column=0, padx=10, pady=10)
        entryKorisnik = ttk.Entry(frame, width=20)
        entryKorisnik.grid(row=0, column=1, padx=10, pady=10, ipady = 4)

        labelKnjiga = ttk.Label(frame, text="ID knjige: ", font = LARGEFONT)
        labelKnjiga.grid(row=1, column=0, padx=10, pady=10)
        entryKnjiga = ttk.Entry(frame, width=20)
        entryKnjiga.grid(row=1, column=1, padx=10, pady=10, ipady = 4)

        btnNazad = ttk.Button(frame, text="Nazad", width=15, command=lambda: controller.show_frame('StartPage'))
        btnNazad.grid(row=2, column=1, padx=10, pady=10,ipady=8)

        def iznajmiKnjigu():
            korisnik = entryKorisnik.get()
            knjiga = entryKnjiga.get()
            if korisnik=='' or knjiga=='':
                messagebox.showerror(title='Greska', message="Polja ne mogu biti prazna!")
            else:
                try:
                    tekst = konekcija.cursor.callproc('pro_izdajKnjigu', [korisnik, knjiga, ""])
                    konekcija.db.commit()

                    messagebox.showinfo(title='Obavesntenje', message=tekst[2])
                    entryKorisnik.delete(0, END)
                    entryKnjiga.delete(0, END)
                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()
                    messagebox.showerror(title='Greska', message="Uneli ste pogresne podatke!")



        btnIznajmi = ttk.Button(frame, text="Iznajmi knjigu", width=15, command=iznajmiKnjigu)
        btnIznajmi.grid(row=2, column=0, padx=10, pady=10,ipady=8)