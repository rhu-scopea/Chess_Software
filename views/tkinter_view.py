from tkinter import *
from tkinter import ttk

BG_COLOR = '#401D09'
FONT_COLOR = '#F2F2F2'
TITLE_FONT = 'Lato'
TITLE_SIZE = 30
TEXT_FONT = 'Courrier'
TEXT_SIZE = 15

TEXT_CONF = {
    'font': f"{TEXT_FONT}, {TEXT_SIZE}",
    'bg': BG_COLOR,
    'fg': FONT_COLOR
}

class TkinterView:

    def __init__(self):
        self.root = Tk()

        # Titre de la fenêtre
        self.root.title("Chess Master")
        # Taille de la fenêtre
        self.root.geometry("400x400")
        # Taille minimmale
        self.root.minsize(200, 300)
        # Changer l'icone par defaut
        self.root.iconbitmap("src/chess.ico")
        # Changer la couleur d'arrière-plan
        self.root.config(background=BG_COLOR)

        self.main_frame = Frame(self.root)

        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.lb = ttk.Label(self.frm, text="Hello World!")
        self.lb.grid(column=0, row=0)
        self.btn = ttk.Button(self.frm, text="Quit", command=self.root.destroy)
        self.btn.grid(column=1, row=0)

        self.root.mainloop()

    def create_menu(self):
        # Création de la barre de menu
        self.menu_bar = Menu(self.root)
        
        # Création du menu Tournoi
        self.menu_tournament = Menu(self.menu_bar, tearoff=0)
        self.menu_tournament.add_command()
        