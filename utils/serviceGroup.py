from tkinter import PanedWindow
from tkinter import Button
from tkinter import Label
from tkinter.ttk import Progressbar
from tkinter import DoubleVar
from tkinter import X

class ServiceGroup(PanedWindow):

    lbServiceGroupName = Label
    progressBarProcessing = Progressbar
    NumberProgress = DoubleVar
    btStarGroup = Button
    btStopGroup = Button

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)

        self["bg"] = "#9E9E9E"

        self.lbServiceGroupName = Label(self)
        self.lbServiceGroupName["bg"] = "#9E9E9E"
        self.lbServiceGroupName["text"] = "Bancos de Dados"
        self.lbServiceGroupName["font"] = "Roboto 20"
        self.lbServiceGroupName["fg"] = "white"

        self.lbServiceGroupName.pack()

        self.NumberProgress = DoubleVar()
        self.progressBarProcessing = Progressbar(self, variable=self.NumberProgress,maximum=10)

        self.NumberProgress.set(5)

        self.progressBarProcessing.pack(fill=X, padx=10)

        self.btStarGroup = Button()
        self.btStopGroup = Button()

        self.add(self.btStarGroup)
        self.add(self.btStopGroup)




        