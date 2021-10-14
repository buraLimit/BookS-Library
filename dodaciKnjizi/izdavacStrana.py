from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from konekcijaSaBazom import konekcija
from knjige.knjigeStrana import PageKnjiga
LARGEFONT = ("Verdana", 14)


class PageIzdavac(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = Frame(self)
        frame.pack(anchor='center', pady=70)

        # Ime IZDAVACA
        labelImeIzdavaca = ttk.Label(frame, text="Naziv Izdavaca: ",font = LARGEFONT)
        labelImeIzdavaca.grid(row=0, column=0, padx=10, pady=10)
        entryImeIzdavaca = ttk.Entry(frame, width=20)
        entryImeIzdavaca.grid(row=0, column=1, padx=10, pady=10, ipady = 4)

        # Grad
        labelGrad = ttk.Label(frame, text="Grad: ",font = LARGEFONT)
        labelGrad.grid(row=1, column=0, padx=10, pady=10)
        entryGrad = ttk.Entry(frame, width=20)
        entryGrad.grid(row=1, column=1, padx=10, pady=10, ipady = 4)

        # Adresa
        labelAdresa = ttk.Label(frame, text="Adresa: ",font = LARGEFONT)
        labelAdresa.grid(row=2, column=0, padx=10, pady=10)
        entryAdresa = ttk.Entry(frame, width=20)
        entryAdresa.grid(row=2, column=1, padx=10, pady=10, ipady = 4)

        def dodajIzdavaca():
            if entryImeIzdavaca.get() == '' or entryAdresa.get() == '' or entryGrad.get() == '':
                messagebox.showerror(title='Greska', message="Sva polja moraju biti popunjena!")
            else:
                try:
                    tekst = konekcija.cursor.callproc('pro_dodajIzdavaca', [entryImeIzdavaca.get(), entryGrad.get(), entryAdresa.get(), ""])
                    konekcija.db.commit()

                    messagebox.showinfo(title='Obavestenje', message=tekst[3])
                    entryImeIzdavaca.delete(0, END)
                    entryGrad.delete(0, END)
                    entryAdresa.delete(0, END)

                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()

        btnNazad = ttk.Button(frame, text="Nazad", width=20, command=lambda: controller.show_frame('StartPage'))
        btnNazad.grid(row=4, column=0, padx=10, pady=10, ipady = 8)
        btnDodajAutora = ttk.Button(frame, text="Dodaj Izdavaca", width=20, command=lambda: [dodajIzdavaca(),PageKnjiga.izdavaci(self)])
        btnDodajAutora.grid(row=4, column=1, padx=10, pady=10, ipady = 8)
