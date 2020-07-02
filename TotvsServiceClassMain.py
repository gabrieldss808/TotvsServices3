from tkinter import Tk
from utils.topMenu import TopMenu
from utils.bottomMenu import BottomMenu
from tkinter import BOTH
from tkinter.ttk import Button, Style
from threading import Thread


class TotvsService3(Tk):

    topMenu = TopMenu   
    bottomMenu = BottomMenu

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

        self.bottomMenu = BottomMenu(self)
        self.bottomMenu.pack()

        self.configMenu()
        

    def callback(self,event):

        self.configMenu()
        

    def configMenu(self):

        self.topMenu["height"] = self.winfo_height()*0.12
        self.topMenu["width"] = self.winfo_width()
        self.topMenu["bg"] = "#616161"

        self.bottomMenu["height"] = self.winfo_height()*0.88
        self.bottomMenu["width"] = self.winfo_width()
        self.bottomMenu["bg"] = "#4285F4"