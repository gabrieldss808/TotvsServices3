import os
import sys
from tkinter import PanedWindow
from tkinter import Button
from tkinter import PhotoImage

class TopMenu(PanedWindow):
    
    btAtualizaService = Button    
    btAtuServiceTimeInterval = Button
    btReloadCSV = Button
    imagebtAtualizaService = PhotoImage
    imagebtAtuServiceTimeInterval = PhotoImage
    imagebtReloadCSV = PhotoImage

    def AdButtons(self):

        self.btAtualizaService = Button()
        self.btAtuServiceTimeInterval = Button()
        self.btReloadCSV = Button()
        
        self.btAtualizaService["command"] = self.Click
        self.btAtualizaService["bd"] = 0
        self.btAtualizaService["bg"] = "#616161"
        self.imagebtAtualizaService = PhotoImage(file=self.resource_path("refresh.png"))
        self.btAtualizaService.config(image=self.imagebtAtualizaService)
      
        self.btAtuServiceTimeInterval["command"] = self.Click
        self.btAtuServiceTimeInterval["bd"] = 0
        self.btAtuServiceTimeInterval["bg"] = "#616161"
        self.imagebtAtuServiceTimeInterval = PhotoImage(file=self.resource_path("time.png"))
        self.btAtuServiceTimeInterval.config(image=self.imagebtAtuServiceTimeInterval)

        self.btReloadCSV["command"] = self.Click
        self.btReloadCSV["bd"] = 0
        self.btReloadCSV["bg"] = "#616161"
        self.imagebtReloadCSV = PhotoImage(file=self.resource_path("reloading.png"))
        self.btReloadCSV.config(image=self.imagebtReloadCSV)

        self.paneconfig(self.btAtualizaService,sticky="W")
        self.paneconfig(self.btAtuServiceTimeInterval,sticky="W")
        self.paneconfig(self.btReloadCSV,sticky="W")

        self.add(self.btAtualizaService,padx=1, pady=1)
        self.add(self.btAtuServiceTimeInterval,padx=1, pady=1)
        self.add(self.btReloadCSV,padx=1, pady=1)
        
    
    def Click(self):

        pass

    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("./icons")

        return os.path.join(base_path, relative_path)
