import tkinter as tk
import konekcijaSaBazom
import mysql.connector
from ttkthemes import ThemedTk

from pocetnaStrana import StartPage
from knjige.iznajmiStrana import PageIznajmi
from knjige.vratiStrana import PageVrati
from clanovi.clanoviStrana import PageClan
from knjige.knjigeStrana import PageKnjiga
from dodaciKnjizi.autorStrana import PageAutor
from dodaciKnjizi.kategorijaStrana import PageKategorija
from dodaciKnjizi.izdavacStrana import PageIzdavac
from knjige.prikazKnjigaStrana import PagePrikazKnjiga
from konekcijaSaBazom import konekcija
LARGEFONT = ("Verdana", 14)

class tkinterApp(ThemedTk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        ThemedTk.__init__(self, *args, **kwargs)
        ThemedTk.set_theme(self,'plastik')
        ThemedTk.iconbitmap(self,"slikaAppICO.ico")
        ThemedTk.title(self,"Biblioteka BookS")
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #inicijalizacija promenljiva za rad sa bazom
        konekcija.db = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="", db="biblioteka")
        konekcija.cursor = konekcija.db.cursor()

        # initializing frames to an empty array
        self.frames = {}
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, PageIznajmi, PageClan, PageVrati, PageKnjiga, PageAutor, PageKategorija, PageIzdavac, PagePrikazKnjiga):
            global frame
            ime_strane = F.__name__
            frame = F(parent=container, controller=self)
            #frame.config(bg='black')
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loo
            self.frames[ime_strane] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('StartPage')

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = tkinterApp()
app.geometry("+550+250")
app.mainloop()
