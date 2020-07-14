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

class TotvsService3(Tk):

    topMenu = TopMenu   
    bottomPanels = BottomPanels
    linhaDeSeparacao = PanedWindow
    log = logController
    GroupsOfServices = list()

    def configTotvsServiceLayout(self):

        self.title('Totvs Services 3')
        self.log = logController()
        
        self.Positioninthecenter()

        self["bg"] = "#616161"

        self.iconbitmap("icons/icon.ico")

        self.LoadPainels()

        self.bind("<Configure>",self.callback)

        self.readCsv()
              
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
        self.topMenu.pack()

        self.linhaDeSeparacao = PanedWindow()
        self.linhaDeSeparacao.pack()

        self.bottomPanels = BottomPanels(self)
        self.bottomPanels.pack()

        self.configPainels()
        
    def callback(self,event):

        task =  Thread(target=self.configPainels,args=[])
        task.start()

    def ReloadBottonPanel(self):

        self.bottomPanels.ClearServicesGroups()

        self.update()

        self.readCsv()

        

    def configPainels(self):

        self.topMenu["height"] = self.winfo_height()*0.12
        self.topMenu["width"] = self.winfo_width()
        self.topMenu["bg"] = "#616161"

        self.linhaDeSeparacao["height"] = 4
        self.linhaDeSeparacao["width"] = self.winfo_width()
        self.linhaDeSeparacao["bg"] = "#9E9E9E"

        self.bottomPanels["height"] = self.winfo_height()*0.88
        self.bottomPanels["width"] = self.winfo_width()
        self.bottomPanels["bg"] = "#616161"

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
