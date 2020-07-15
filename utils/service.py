from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import X,Y,LEFT,RIGHT,BOTH,TRUE,StringVar
from utils.logController import logController
import win32

class Service(Frame):

    ServiceName = ""
    ServiceNameDisplay = ""
    ServiceNameAndStatus = StringVar
    lbServiceNameAndStatus = Label
    barStatusColor = Frame
    btServiceStart = Button
    btServiceStop = Button
    
    def __init__(self, parent,serviceName="",serviceNameDisplay="", *args, **kw):
        Frame.__init__(self, parent, *args, **kw)   

        self.ServiceName = serviceName
        self.ServiceNameDisplay = serviceNameDisplay

        self.ServiceNameAndStatus = StringVar()
        self.ServiceNameAndStatus.set(self.ServiceNameDisplay)

        self.ConfigComponents()
    
    def atuStatus(self,StringStatus="",Status=None):

        self.ServiceNameAndStatus.set(StringStatus)

        if ('RUNNING' in StringStatus):

            self.barStatusColor["bg"] = "#34A853"
        elif('STOPPED' in StringStatus):

           self.barStatusColor["bg"] = "#EA4335"
        else:

            self.barStatusColor["bg"] = "#757575"

    def ConfigComponents(self):

        self["bd"] = 1
        self["bg"] = "#757575"

        self.lbServiceNameAndStatus = Label(self)
        self.lbServiceNameAndStatus["bg"] = "#616161"
        self.lbServiceNameAndStatus["textvariable"] = self.ServiceNameAndStatus
        self.lbServiceNameAndStatus["font"] = "Roboto 15"
        self.lbServiceNameAndStatus["fg"] = "white"
        self.lbServiceNameAndStatus.pack(side=LEFT, fill=BOTH, expand=True)

        self.btServiceStop = Button(self)
        self.btServiceStop["text"] = "Stop"
        self.btServiceStop["font"] = "Roboto 15"
        self.btServiceStop["fg"] = "white"
        self.btServiceStop["width"] = 10
        self.btServiceStop["bg"] = "#616161"
        self.btServiceStop["bd"] = 0
        self.btServiceStop["relief"] = "flat"
        self.btServiceStop["command"] = self.StopService
        self.btServiceStop.pack(side=RIGHT,fill=BOTH)

        self.btServiceStart = Button(self)
        self.btServiceStart["text"] = "Start"
        self.btServiceStart["font"] = "Roboto 15"
        self.btServiceStart["fg"] = "white"
        self.btServiceStart["width"] = 10
        self.btServiceStart["bg"] = "#616161"
        self.btServiceStart["bd"] = 0
        self.btServiceStart["relief"] = "flat"
        self.btServiceStart["command"] = self.StartService
        self.btServiceStart.pack(side=RIGHT,fill=BOTH)

        self.barStatusColor = Frame(self)
        self.barStatusColor["width"] = 10
        self.barStatusColor["bg"] = "#34A853"
        self.barStatusColor.pack(side=RIGHT,fill=Y)

    def StartService(self):

        service = win32.lib.win32serviceutil
        StringErro = ""

        try:

            if(service.QueryServiceStatus(self.ServiceName)[1] == 1):

                service.StartService(self.ServiceName)

                StringMen = 'Iniciando: ' + self.ServiceName

                logController.consoleLogAdd(logController,StringMen)
        except Exception as e:    
            
            StringErro+= "###########################################################\n"
            StringErro+= "Erro no Serviço: " + self.ServiceName + "\t" + "Erro: " + str(e) + "\n"
            if("Acesso negado" in StringErro):
                StringErro+="Inicie a aplicação como Administrador\n"
            StringErro+= "###########################################################\n"

            logController.consoleLogAdd(logController,StringErro)

    def StopService(self):

        service = win32.lib.win32serviceutil
        StringErro = ""

        try:
            if(service.QueryServiceStatus(self.ServiceName)[1] == 4):
                        
                service.StopService(self.ServiceName)

                StringMen = 'Parando: ' + self.ServiceName

                logController.consoleLogAdd(logController,StringMen)
        except Exception as e:    
            
            StringErro+= "###########################################################\n"
            StringErro+= "Erro no Serviço: " + self.ServiceName + "\t" + "Erro: " + str(e) + "\n"
            if("Acesso negado" in StringErro):
                StringErro+="Inicie a aplicação como Administrador\n"
            StringErro+= "###########################################################\n"

            logController.consoleLogAdd(logController,StringErro)