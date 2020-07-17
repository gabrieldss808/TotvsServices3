from tkinter import Tk
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import X,Y


class PopUpAtuTime(Tk):

    InputBox = Entry
    lbTitle = Label
    TimeIntervalNumber = int()
    btOk = Button

    def configureComponents(self):

        self.title("Intervalo")
        self["bg"] = "#616161"

        self.resizable(0,0)

        self.Positioninthecenter()

        self.lbTitle = Label(self)
        self.lbTitle["bg"] = "#616161"
        self.lbTitle["text"] = "Os Serviços são atualizados a cada\n" + str(self.TimeIntervalNumber) + "s"
        self.lbTitle["font"] = "Roboto 10"
        self.lbTitle["fg"] = "white"
        self.lbTitle.pack(padx=10, pady=5)

        self.InputBox = Entry(self)
        self.InputBox["validate"] = "key"
        self.InputBox["validatecommand"] = (self.InputBox.register(self.ValidateCommand),'%S')
        self.InputBox.pack(fill=X,padx=40,pady=5)

        self.btOk = Button(self)
        self.btOk["text"] = "OK"
        self.btOk["font"] = "Roboto 12"
        self.btOk["fg"] = "white"
        self.btOk["bg"] = "#34A853"
        self.btOk["bd"] = 0
        self.btOk["relief"] = "flat"
        self.btOk["command"] = self.FinalizeCommand
        self.btOk.pack(fill=X,padx=40,pady=5)

    def ValidateCommand(self,CurrentCharacter):

        if (CurrentCharacter.isdigit()):

            return True
        else:

            return False

    def FinalizeCommand(self):

        self.master.master.timeInterval = int(self.InputBox.get())

        self.destroy()

    def Positioninthecenter(self):

        largura = 225
        altura = 110

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

