from tkinter import Tk

class TotvsService3(Tk):

    def configTotvsServiceLayoyt(self):

        self.title('Totvs Services 3')
        
        self.Positioninthecenter()

        self["bg"] = "#616161"

        self.iconbitmap("icons/icon.ico")
    
    def Positioninthecenter(self):

        largura = 450
        altura = 600

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))