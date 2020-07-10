import sys 

from os.path import abspath, join
from tkinter import Button
from tkinter import PanedWindow
from tkinter import Label
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import DoubleVar
from tkinter import X,LEFT,RIGHT,BOTTOM,BOTH
from tkinter.ttk import Frame
from tkinter.ttk import Progressbar
from tkinter.ttk import Style
from utils.stylesInterface import StylesInterface

class ServiceGroup(Frame):

    NameGroup = StringVar
    DelayTime = 1
    lbServiceGroupName = Label
    progressBarProcessing = Progressbar
    progressBarStyle = Style
    progressNumber = DoubleVar
    btStarGroup = Button
    imagebtStarGroup = PhotoImage
    btStopGroup = Button
    imagebtStopGroup = PhotoImage
    linhaDeSeparacao = PanedWindow
    OrganizerButtons = PanedWindow

    def __init__(self, *args, **kw):

        Frame.__init__(self, *args, **kw)

        self.NameGroup = StringVar()

        self.ConfigComponents()
    
    def SetInformationGroup(self,name="",delay=0):

        self.NameGroup.set(name)
        self.DelayTime = delay

    def StartGroup(self):
        pass

    def StropGroup(self):
        pass

    def resource_path(self,relative_path):
        
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = abspath("./icons")

        return join(base_path, relative_path)

    def ConfigComponents(self):

        self.lbServiceGroupName = Label(self)
        self.lbServiceGroupName["bg"] = "#616161"
        self.lbServiceGroupName["textvariable"] = self.NameGroup
        self.lbServiceGroupName["font"] = "Roboto 20"
        self.lbServiceGroupName["fg"] = "white"
        self.lbServiceGroupName.pack(pady=5)

        self.progressNumber = DoubleVar()
        self.progressNumber.set(7)
        self.progressBarStyle = Style()
        self.progressBarStyle.theme_use('clam')
        self.progressBarStyle.configure("Horizontal.TProgressbar", troughcolor ='#616161', background="#34A853",lightcolor='#34A853',darkcolor="#34A853")
        self.progressBarProcessing = Progressbar(self, style="Horizontal.TProgressbar",variable=self.progressNumber,maximum=10)
        self.progressBarProcessing.pack(fill=X, padx=10,pady=10)

        self.OrganizerButtons = PanedWindow(self)
        self.OrganizerButtons["height"] = 80
        self.OrganizerButtons["bg"] = "#616161"
        self.OrganizerButtons.pack(fill=X,padx=10)

        self.btStarGroup = Button(self.OrganizerButtons,command=self.StartGroup)
        self.btStarGroup["bg"] = "#616161"
        self.btStarGroup["bd"] = 0
        self.imagebtStarGroup = PhotoImage(file=self.resource_path("btStartGroupIcon.png"))
        self.btStarGroup.config(image=self.imagebtStarGroup)
        self.btStarGroup.pack(fill=X,side=LEFT,padx=10)
        
        self.btStopGroup = Button(self.OrganizerButtons,command=self.StropGroup)
        self.btStopGroup["bg"] = "#616161"
        self.btStopGroup["bd"] = 0
        self.imagebtStopGroup = PhotoImage(file=self.resource_path("btStopGroupIcon.png"))
        self.btStopGroup.config(image=self.imagebtStopGroup)
        self.btStopGroup.pack(fill=X,side=LEFT,padx=5)

        self.linhaDeSeparacao = PanedWindow(self)
        self.linhaDeSeparacao["height"] = 2
        self.linhaDeSeparacao["bg"] = "#9E9E9E"
        self.linhaDeSeparacao.pack(fill=X,padx=20,pady=5)