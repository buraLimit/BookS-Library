from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from konekcijaSaBazom import konekcija

LARGEFONT = ("Verdana", 14)


class PagePrikazKnjiga(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        rightFrame = Frame(self)
        rightFrame.pack(anchor='center', fill='both', expand=True,padx=15, pady=15)
        scroll = Scrollbar(rightFrame, orient=VERTICAL)
        self.treeKnjiga = ttk.Treeview(rightFrame, height=12, columns=("ID", "Naslov", "Autor", "Izdanje", "Godina", "ISBN", "Kategorija", "Izdavac", "Kolicina", "Slobodne"),
                                yscrollcommand=scroll.set)
        # FRAME ZA DRVO

        # DRVO ZA KNJIGE

        scroll.pack(side=RIGHT, fill=Y)

        self.treeKnjiga.heading("ID", text="ID")
        self.treeKnjiga.heading("Naslov", text="Naslov")
        self.treeKnjiga.heading("Autor", text="Autor")
        self.treeKnjiga.heading("Izdanje", text="Izdanje")
        self.treeKnjiga.heading("Godina", text="Godina")
        self.treeKnjiga.heading("ISBN", text="ISBN")
        self.treeKnjiga.heading("Kategorija", text="Kategorija")
        self.treeKnjiga.heading("Izdavac", text="Izdavac")
        self.treeKnjiga.heading("Kolicina", text="Kolicina")
        self.treeKnjiga.heading("Slobodne", text="Slobodne")
        self.treeKnjiga['show'] = 'headings'

        self.treeKnjiga.column("ID", width=15,anchor=CENTER)
        self.treeKnjiga.column("Naslov", width=100,anchor=CENTER)
        self.treeKnjiga.column("Autor", width=100,anchor=CENTER)
        self.treeKnjiga.column("Izdanje", width=15,anchor=CENTER)
        self.treeKnjiga.column("Godina", width=40,anchor=CENTER)
        self.treeKnjiga.column("ISBN", width=80,anchor=CENTER)
        self.treeKnjiga.column("Kategorija", width=50,anchor=CENTER)
        self.treeKnjiga.column("Izdavac", width=60,anchor=CENTER)
        self.treeKnjiga.column("Kolicina", width=30,anchor=CENTER)
        self.treeKnjiga.column("Slobodne", width=30, anchor=CENTER)

        self.treeKnjiga.pack(fill=BOTH, expand=1)
        #PagePrikazKnjiga.prikaziKnjige(self)

        frame = Frame(self)
        frame.pack(anchor="s")

        labelPretragaKnjiga = ttk.Label(frame, text="Unos sa pretragu: ", font = LARGEFONT)
        labelPretragaKnjiga.grid(row=0, column=0, padx=10, pady=10)
        entryPretragaKnjiga = ttk.Entry(frame, width=20)
        entryPretragaKnjiga.grid(row=0, column=1, padx=10, pady=10, ipady =4)

        def pretragaKnjige():
            if entryPretragaKnjiga.get() == '' :
                messagebox.showerror(title='Greska', message="Morate popuniti polje!")
            else:
                try:
                    print(entryPretragaKnjiga.get())
                    konekcija.cursor.execute(f'SELECT * FROM view_prikazknjiga WHERE naslov LIKE "%{entryPretragaKnjiga.get()}%" OR naziv_aut LIKE "%{entryPretragaKnjiga.get()}%" OR naziv_kat LIKE "%{entryPretragaKnjiga.get()}%";')
                    print('PROSAO exec')
                    result = konekcija.cursor.fetchall()

                    if len(result) != 0:
                        print('NASAO NESTO')

                        #NOVI PROZOR ZA PRETRAGU
                        top = tk.Toplevel()
                        top.title("Rezultat pretrage")
                        top.geometry("900x200+600+350")
                        pretragaFrame = tk.Frame(top)
                        pretragaFrame.pack(anchor='center', fill='both', expand=True, padx=15, pady=15)
                        scroll = Scrollbar(pretragaFrame, orient=VERTICAL)

                        treePretragaKnjiga = ttk.Treeview(pretragaFrame, height=12, columns=("ID", "Naslov", "Autor", "Izdanje", "Godina", "ISBN", "Kategorija", "Izdavac", "Kolicina", "Slobodne"),yscrollcommand=scroll.set)
                        scroll.pack(side=RIGHT, fill=Y)

                        treePretragaKnjiga.heading("ID", text="ID")
                        treePretragaKnjiga.heading("Naslov", text="Naslov")
                        treePretragaKnjiga.heading("Autor", text="Autor")
                        treePretragaKnjiga.heading("Izdanje", text="Izdanje")
                        treePretragaKnjiga.heading("Godina", text="Godina")
                        treePretragaKnjiga.heading("ISBN", text="ISBN")
                        treePretragaKnjiga.heading("Kategorija", text="Kategorija")
                        treePretragaKnjiga.heading("Izdavac", text="Izdavac")
                        treePretragaKnjiga.heading("Kolicina", text="Kolicina")
                        treePretragaKnjiga.heading("Slobodne", text="Slobodne")
                        treePretragaKnjiga['show'] = 'headings'

                        treePretragaKnjiga.column("ID", width=15, anchor=CENTER)
                        treePretragaKnjiga.column("Naslov", width=100, anchor=CENTER)
                        treePretragaKnjiga.column("Autor", width=100, anchor=CENTER)
                        treePretragaKnjiga.column("Izdanje", width=15, anchor=CENTER)
                        treePretragaKnjiga.column("Godina", width=40, anchor=CENTER)
                        treePretragaKnjiga.column("ISBN", width=80, anchor=CENTER)
                        treePretragaKnjiga.column("Kategorija", width=50, anchor=CENTER)
                        treePretragaKnjiga.column("Izdavac", width=60, anchor=CENTER)
                        treePretragaKnjiga.column("Kolicina", width=30, anchor=CENTER)
                        treePretragaKnjiga.column("Slobodne", width=30, anchor=CENTER)

                        treePretragaKnjiga.pack(fill=BOTH, expand=1)

                        for row in result:
                            treePretragaKnjiga.insert('',END,values=row)
                    else:
                        messagebox.showinfo(title='Obavestenje', message='Trazena knjiga ne postoji')

                except Exception as arg:
                    print('NIJE upisano', arg)
                    konekcija.db.rollback()

        btnPretrazi = ttk.Button(frame, text="Pretrazi", width=20, command=lambda: [pretragaKnjige(),entryPretragaKnjiga.delete(0,END)])
        btnPretrazi.grid(row=1, column=0, padx=10, pady=10, ipady=8)

        btnNazad = ttk.Button(frame, text="Nazad", width=20, command=lambda: controller.show_frame('StartPage'))
        btnNazad.grid(row=1, column=1, padx=10, pady=10, ipady=8)

        self.prikaziKnjige()

    def prikaziKnjige(self):
        konekcija.cursor.execute("select * from view_prikazknjiga")
        result = konekcija.cursor.fetchall()
        if len(result) != 0:
            self.treeKnjiga.delete(*self.treeKnjiga.get_children())
            for row in result:
                self.treeKnjiga.insert('', END, values=row)
        konekcija.db.commit()


