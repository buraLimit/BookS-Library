from tkinter import *
import tkinter as tk
from tkinter import ttk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = Frame(self)
        frame.pack(anchor='center',pady=60)

        btnIznajmi = ttk.Button(frame, text="Izdaj knjigu", width=30, command=lambda: controller.show_frame('PageIznajmi'))
        btnIznajmi.grid(row=0, column=2, padx=10, pady=10,columnspan = 2, rowspan=2, ipady=15)

        btnVrati = ttk.Button(frame, text="Povracaj knjige", width=30,command=lambda: controller.show_frame('PageVrati'))
        btnVrati.grid(row=0, column=4, padx=10, pady=10,columnspan = 2, rowspan=2, ipady=15)

        btnNoviClan = ttk.Button(frame, text="Clanovi", width=30, command=lambda: controller.show_frame('PageClan'))
        btnNoviClan.grid(row=2, column=2, padx=10, pady=10,columnspan = 2, ipady=15)

        btnNovaKnjiga = ttk.Button(frame, text="Nova knjiga", width=30, command=lambda: [controller.show_frame('PageKnjiga')])
        btnNovaKnjiga.grid(row=2, column=4, padx=10, pady=10,columnspan = 2, ipady=15)

        btnNoviAutor = ttk.Button(frame, text="Novi autor", width=30, command=lambda: controller.show_frame('PageAutor'))
        btnNoviAutor.grid(row=4, column=2, padx=10, pady=10,columnspan = 2, ipady=15)

        btnNovaKategorija = ttk.Button(frame, text="Nova kategorija", width=30, command=lambda: controller.show_frame('PageKategorija'))
        btnNovaKategorija.grid(row=4, column=4, padx=10, pady=10,columnspan = 2, ipady=15)

        btnPretragaKorisnika = ttk.Button(frame, text="Novi Izdavac", width=30,command=lambda: controller.show_frame('PageIzdavac'))
        btnPretragaKorisnika.grid(row=6, column=2, padx=10, pady=10, columnspan=2, ipady=15)

        btnPretragaKjige = ttk.Button(frame, text="Prikaz svih knjiga", width=30, command=lambda: [controller.show_frame('PagePrikazKnjiga')])
        btnPretragaKjige.grid(row=6, column=4, padx=10, pady=10, columnspan=2, ipady=15)
