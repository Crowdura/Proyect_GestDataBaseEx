import tkinter as tkind
from tkinter.messagebox import showinfo
from .udi.label import confLabel
from .udi.button import confButton
from .udi.colorScreen import colorScreen

class confScreen (tkind.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Gestor de Excel")
        self.attributes('-fullscreen', True)
        self.config( bg="blue4" )
        self.tk_bisque()

        self.label = tkind.Label(self, text="Prueba de screen")
        self.label.pack()

        self.button = tkind.Button(self, text="Prueba de click", command= self.button_clicked)

        self.button = tkind.Button(self, text="Prueba de click", command= self.button_clicked)
                
        self.button = tkind.Button(self, text="Prueba de click", command= self.button_clicked)

        return
    def button_clicked(self):
        showinfo(title="Information", message="Prueba de mensaje")

    def confScree(self):

        return
    def typeScreen(self):

        return
    