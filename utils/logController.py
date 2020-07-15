
class logController():

    def clearLog(self):

        self.consoleLog = open('service.log','w',1,'utf-8')

        self.consoleLog.write("")

    #Metodo responsável por atualizar os console log da ultima execução do App
    def consoleLogAdd(self, menssageText):

        self.consoleLog = open('service.log','a',1,'utf-8')

        self.consoleLog.write(menssageText + '\n')

        self.consoleLog.close()