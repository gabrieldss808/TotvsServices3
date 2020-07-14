from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import X,Y,LEFT,RIGHT,BOTH,TRUE,StringVar

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
        self.ServiceNameAndStatus.set(self.ServiceNameDisplay + "\nRunning")

        self.ConfigComponents()
    
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
        self.btServiceStop.pack(side=RIGHT,fill=BOTH)

        self.btServiceStart = Button(self)
        self.btServiceStart["text"] = "Start"
        self.btServiceStart["font"] = "Roboto 15"
        self.btServiceStart["fg"] = "white"
        self.btServiceStart["width"] = 10
        self.btServiceStart["bg"] = "#616161"
        self.btServiceStart["bd"] = 0
        self.btServiceStart["relief"] = "flat"
        self.btServiceStart["command"] = self.Click
        self.btServiceStart.pack(side=RIGHT,fill=BOTH)

        self.barStatusColor = Frame(self)
        self.barStatusColor["width"] = 10
        self.barStatusColor["bg"] = "#34A853"
        self.barStatusColor.pack(side=RIGHT,fill=Y)

    def Click(self):

        self.barStatusColor["bg"] = "#EA4335"