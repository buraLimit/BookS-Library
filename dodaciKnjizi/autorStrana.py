from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from konekcijaSaBazom import konekcija

LARGEFONT = ("Verdana", 14)
from knjige.knjigeStrana import PageKnjiga

class PageAutor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = Frame(self)
        frame.pack(anchor='center', pady=70)

        # Autor
        labelAutor = ttk.Label(frame, text="Autor: ", font = LARGEFONT)
        labelAutor.grid(row=0, column=0, padx=10, pady=10)
        entryAutor = ttk.Entry(frame, width=20)
        entryAutor.grid(row=0, column=1, padx=10, pady=10, ipady = 4)

        def dodajAutora():
            if entryAutor.get() == '':
                messagebox.showerror(title='Greska', message="Morate popuniti polje!")
            else:
                try:
                    tekst = konekcija.cursor.callproc('pro_dodajAutora', [entryAutor.get(), ""])
                    konekcija.db.commit()

                    messagebox.showinfo(title='Obavestenje', message=tekst[1])
                    entryAutor.delete(0, END)

                except:
                    print('NIJE upisano')
                    konekcija.db.rollback()

        btnNazad = ttk.Button(frame, text="Nazad", width=30, command=lambda: controller.show_frame('StartPage'))
        btnNazad.grid(row=1, column=1, padx=10, pady=10, ipady = 8)
        btnDodajAutora = ttk.Button(frame, text="Dodaj autora", width=20, command=lambda: [dodajAutora(),PageKnjiga.autori(self)])
        btnDodajAutora.grid(row=0, column=2, padx=10, pady=10, columnspan=2, ipady = 8)

