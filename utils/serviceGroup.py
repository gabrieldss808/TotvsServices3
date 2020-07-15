import sys 
import os
import win32.lib.win32serviceutil 

from time import sleep
from tkinter import Button
from tkinter import PanedWindow
from tkinter import Label
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import DoubleVar
from tkinter import X,LEFT,RIGHT,BOTTOM,BOTH
from threading import Thread
from tkinter.ttk import Frame
from tkinter.ttk import Progressbar
from tkinter.ttk import Style
from utils.service import Service
from utils.logController import logController
from utils.stylesInterface import StylesInterface

class ServiceGroup(Frame):

    log = logController
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
    StyleServiceGroup = StylesInterface

    def __init__(self, *args, **kw):

        Frame.__init__(self, *args, **kw)

        self.NameGroup = StringVar()

        self.log = logController()
    
    def SetInformationGroup(self,name="",delay=0):

        self.NameGroup.set(name)
        self.DelayTime = delay

    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("./icons")

        return os.path.join(base_path, relative_path)

    def AtuServices(self):

        serviceTool = win32.lib.win32serviceutil

        for service in self.winfo_children():

            if ('service' in service._name):

                StringMen = 'Atualizando Status do Serviço... ' + service.ServiceName

                self.log.consoleLogAdd(StringMen)

                Status = self.StringStatus(serviceTool.QueryServiceStatus(service.ServiceName)[1])

                service.atuStatus(service.ServiceNameDisplay + "\n" + Status,Status)

    #Retorna a string de cada status do serviço
    def StringStatus(self,nService=0):

        if(nService == 1):
            return "STOPPED"
        elif(nService == 2):
            return "START PENDING"
        elif(nService == 3):
            return "STOP PENDING"
        elif(nService == 4):
            return "RUNNING"
        elif(nService == 5):
            return "CONTINUE PENDING"
        elif(nService == 6):
            return "PAUSE PENDING"
        elif(nService == 7):
            return "PAUSED"


    def ConfigComponents(self,NumberOfServices=0):

        self.lbServiceGroupName = Label(self)
        self.lbServiceGroupName["bg"] = "#616161"
        self.lbServiceGroupName["textvariable"] = self.NameGroup
        self.lbServiceGroupName["font"] = "Roboto 20"
        self.lbServiceGroupName["fg"] = "white"
        self.lbServiceGroupName.pack(pady=5)

        self.progressNumber = DoubleVar()
        self.progressBarStyle = Style()
        self.progressBarStyle.theme_use('clam')
        self.progressBarStyle.configure("Horizontal.TProgressbar", troughcolor ='#616161', background="#34A853",lightcolor='#34A853',darkcolor="#34A853")
        self.progressBarProcessing = Progressbar(self, style="Horizontal.TProgressbar",variable=self.progressNumber,maximum=NumberOfServices)
        self.progressBarProcessing.pack(fill=X, padx=10,pady=10)

        self.OrganizerButtons = PanedWindow(self)
        self.OrganizerButtons["height"] = 80
        self.OrganizerButtons["bg"] = "#616161"
        self.OrganizerButtons.pack(fill=X,padx=10)

        self.btStarGroup = Button(self.OrganizerButtons,command=self.StartGroup)
        self.btStarGroup["bg"] = "#616161"
        self.btStarGroup["bd"] = 0
        self.btStarGroup["command"] = self.StartGroup
        self.imagebtStarGroup = PhotoImage(file=self.resource_path("btStartGroupIcon.png"))
        self.btStarGroup.config(image=self.imagebtStarGroup)
        self.btStarGroup.pack(fill=X,side=LEFT,padx=10)
        
        self.btStopGroup = Button(self.OrganizerButtons,command=self.StopGroup)
        self.btStopGroup["bg"] = "#616161"
        self.btStopGroup["bd"] = 0
        self.btStopGroup["command"] = self.StopGroup
        self.imagebtStopGroup = PhotoImage(file=self.resource_path("btStopGroupIcon.png"))
        self.btStopGroup.config(image=self.imagebtStopGroup)
        self.btStopGroup.pack(fill=X,side=LEFT,padx=5)

        self.linhaDeSeparacao = PanedWindow(self)
        self.linhaDeSeparacao["height"] = 2
        self.linhaDeSeparacao["bg"] = "#9E9E9E"
        self.linhaDeSeparacao.pack(fill=X,padx=20,pady=5)
    
    def StartGroup(self):
        
        taskStartServices = Thread(target=self.OptionRunGroup,args=[1])
        taskStartServices.start()

    def StopGroup(self):
        
        taskStopServices = Thread(target=self.OptionRunGroup,args=[2])
        taskStopServices.start()

    def OptionRunGroup(self,Tipo=0):

        self.progressNumber.set(0)
        
        for service in self.winfo_children():

            if ('service' in service._name):

                if(Tipo == 1):

                    service.StartService()

                    updProgress = Thread(target=self.updateProgress, args=[])
                    updProgress.start()

                    sleep(self.DelayTime)
                if(Tipo == 2):

                    service.StopService()
                    
                    updProgress = Thread(target=self.updateProgress, args=[])
                    updProgress.start()

                    sleep(self.DelayTime)
        
        self.progressNumber.set(0)
    
    def updateProgress(self):

        self.progressNumber.set(self.progressNumber.get() + 1)