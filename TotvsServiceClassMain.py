from utils.topMenu import TopMenu
from utils.bottomPanels import BottomPanels
from tkinter.ttk import Button
from tkinter import PanedWindow
from tkinter import VERTICAL
from tkinter import Tk
from tkinter import BOTH
from threading import Thread

class TotvsService3(Tk):

    topMenu = TopMenu   
    BottomPanels = BottomPanels
    linhaDeSeparacao = PanedWindow

    def configTotvsServiceLayoyt(self):

        self.title('Totvs Services 3')
        
        self.Positioninthecenter()

        self["bg"] = "#616161"

        self.iconbitmap("icons/icon.ico")

        self.LoadPainels()

        self.bind("<Configure>",self.callback)
              
    def Positioninthecenter(self):

        largura = 600
        altura = 600

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.minsize(550,546)

    def LoadPainels(self):

        self.topMenu = TopMenu(self)
        self.topMenu.AdButtons()
        self.topMenu.pack()

        self.linhaDeSeparacao = PanedWindow()
        self.linhaDeSeparacao.pack()

        self.BottomPanels = BottomPanels(self)

        self.BottomPanels.addGroups()
        
        self.BottomPanels.pack()

        self.configPainels()
        
    def callback(self,event):

        self.configPainels()

    def configPainels(self):

        self.topMenu["height"] = self.winfo_height()*0.12
        self.topMenu["width"] = self.winfo_width()
        self.topMenu["bg"] = "#616161"

        self.linhaDeSeparacao["height"] = 4
        self.linhaDeSeparacao["width"] = self.winfo_width()
        self.linhaDeSeparacao["bg"] = "#9E9E9E"


        self.BottomPanels["height"] = self.winfo_height()*0.88
        self.BottomPanels["width"] = self.winfo_width()
        self.BottomPanels["bg"] = "#616161"