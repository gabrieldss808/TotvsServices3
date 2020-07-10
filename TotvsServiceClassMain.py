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
from win32.lib.win32serviceutil import QueryServiceStatus

class TotvsService3(Tk):

    topMenu = TopMenu   
    BottomPanels = BottomPanels
    linhaDeSeparacao = PanedWindow
    log = logController
    GroupsOfServices = list()

    def configTotvsServiceLayoyt(self):

        self.title('Totvs Services 3')
        self.log = logController()
        
        self.Positioninthecenter()

        self["bg"] = "#616161"

        self.iconbitmap("icons/icon.ico")

        self.LoadPainels()

        self.bind("<Configure>",self.callback)

        self.readCsv()
              
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

    #Lê o CSV e cria os criar os Grupos de Serviços especificado no CSV
    def readCsv(self):

        linha = ''
        groupName = ''
        groupIndex = 0
        StringErro = ''
        
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

                        if(self.validService(linha[0])):

                            if(groupName == ''):
                                groupName = 'Grupo Nulo'
                                self.GroupsOfServices.append(['Grupo Nulo',1,[] ])
                                groupIndex += 1

                            self.GroupsOfServices[groupIndex-1][2].append([linha[0],linha[1]])
        
            self.BottomPanels.AddGroupsAndServices(self.GroupsOfServices)
        except Exception as e:

            StringErro+= '###########################################################\n'
            StringErro+= "Erro no CSV: \t" + str(e) + "\n"
            StringErro+= '###########################################################\n'

            self.log.consoleLogAdd(StringErro)

        

    # #Valida se o Serviço está disponível no Windows
    def validService(self,nameService=''):

        StringErro = ""

        try:

            QueryServiceStatus(nameService)
            return True
        except Exception as e:

            StringErro+= '###########################################################\n'
            StringErro+= "Erro no Serviço: " + nameService + "\t" + "Erro: " + str(e) + "\n"
            StringErro+= '###########################################################\n'

            self.log.consoleLogAdd(StringErro)

            return False
