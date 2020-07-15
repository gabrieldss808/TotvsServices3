import os
import sys

from time import sleep
from csv import reader
from tkinter import PanedWindow
from tkinter import VERTICAL
from tkinter import Tk
from tkinter import BOTH
from threading import Thread
from tkinter.ttk import Button
from utils.topMenu import TopMenu
from utils.bottomPanels import BottomPanels
from utils.logController import logController
from threading import Thread

class TotvsService3(Tk):

    log = logController
    topMenu = TopMenu   
    timeInterval = int()
    timeIntervalIsRun = False
    bottomPanels = BottomPanels
    linhaDeSeparacao = PanedWindow
    GroupsOfServices = list()

    def configTotvsServiceLayout(self):

        self.title('Totvs Services 3')
        self.log = logController()
        self.log.clearLog()
        
        self.Positioninthecenter()

        self["bg"] = "#616161"

        self.iconbitmap(self.resource_path("icon.ico"))

        self.LoadPainels()

        self.bind("<Configure>",self.callback)

        self.readCsv()

    def iniScheduleAtuService(self):
        
        self.timeIntervalIsRun = True
        self.timeInterval = 5

        schedule = Thread(target=self.scheduleAtuService,args=[])
        schedule.start()

    def scheduleAtuService(self):

        while (self.timeIntervalIsRun):
            
            self.AtuService()
            sleep(self.timeInterval)

    def AtuService(self):

        for Group in self.bottomPanels.interior.winfo_children():

            Group.AtuServices()

    def closingApp(self):

        self.timeIntervalIsRun = False
              
    def Positioninthecenter(self):

        largura = 650
        altura = 600

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.minsize(650,600)

    def LoadPainels(self):

        self.topMenu = TopMenu(self)
        self.topMenu.AdButtons()
        self.topMenu["bg"] = "#616161"
        self.topMenu.pack()

        self.linhaDeSeparacao = PanedWindow()
        self.linhaDeSeparacao["bg"] = "#9E9E9E"
        self.linhaDeSeparacao.pack()

        self.bottomPanels = BottomPanels(self)
        self.bottomPanels["bg"] = "#616161"
        self.bottomPanels.pack()

        self.configPainels()
        
    def callback(self,event):

        task =  Thread(target=self.configPainels,args=[])
        task.start()

    def ReloadBottonPanel(self):

        self.bottomPanels.ClearServicesGroups()

        self.update()

        self.readCsv()

    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("./icons")

        return os.path.join(base_path, relative_path)

        

    def configPainels(self):

        self.topMenu["height"] = self.winfo_height()*0.12
        self.topMenu["width"] = self.winfo_width()

        self.linhaDeSeparacao["height"] = 4
        self.linhaDeSeparacao["width"] = self.winfo_width()

        self.bottomPanels["height"] = self.winfo_height()*0.88
        self.bottomPanels["width"] = self.winfo_width()

    #Lê o CSV e cria os criar os Grupos de Serviços especificado no CSV
    def readCsv(self):

        linha = ''
        groupName = ''
        groupIndex = 0
        StringErro = ''
        self.GroupsOfServices.clear()
        
        try:
            with open('services.csv','r') as arquivo_csv :

                leitor = reader(arquivo_csv, delimiter=';')

                for linha in leitor:

                    if(linha[0] == 'Group'):
                        
                        if(len(linha) > 2):

                            self.GroupsOfServices.append( [linha[1] ,int(linha[2]),[]] )
                            groupName = linha[1]
                        else:

                            self.GroupsOfServices.append( [linha[1],1,[]] )
                            groupName = linha[1]
                        
                        groupIndex += 1
                    else:

                        if(groupName == ''):
                            groupName = 'Grupo Nulo'
                            self.GroupsOfServices.append(['Grupo Nulo',1,[] ])
                            groupIndex += 1

                        self.GroupsOfServices[groupIndex-1][2].append([linha[0],linha[1]])
        
            self.bottomPanels.AddGroupsAndServices(self.GroupsOfServices)
        except Exception as e:

            StringErro+= '###########################################################\n'
            StringErro+= "Erro no CSV: \t" + str(e) + "\n"
            StringErro+= '###########################################################\n'

            self.log.consoleLogAdd(StringErro)
