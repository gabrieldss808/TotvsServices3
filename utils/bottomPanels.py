import win32.lib.win32serviceutil

from tkinter import Frame
from tkinter import Scrollbar
from tkinter import Canvas
from tkinter import Button
from tkinter import VERTICAL, RIGHT, LEFT, BOTH, TRUE, FALSE, NW, Y, X
from utils.service import Service
from utils.serviceGroup import ServiceGroup
from utils.logController import logController
from utils.stylesInterface import StylesInterface

class BottomPanels(Frame):

    StyleServiceGroup = StylesInterface
    NumberStyle = int()
    log = logController

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        self.StyleServiceGroup = StylesInterface(self)

        self.log = logController()

        self.NumberStyle = 0

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, bg="#616161", highlightthickness=0, yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it

        self.interior = interior = Frame(canvas, bg="#616161")
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

    def ClearServicesGroups(self):

        ServiceGroups = self.interior.winfo_children()

        for ServiceGroup in ServiceGroups:

            ServiceGroup.destroy()

    def AddGroupsAndServices(self,GroupsOfServices=list()):

        for Group in GroupsOfServices:

            self.StyleServiceGroup.CreateStyleDynamic(str(self.NumberStyle))

            ServiceGroupObject = ServiceGroup(self.interior,style="RoundedFrame"+str(self.NumberStyle))

            ServiceGroupObject.ConfigComponents(len(Group[2]))

            ServiceGroupObject.SetInformationGroup(Group[0],Group[1])

            ServiceGroupObject.pack(fill=X ,pady=12, padx=20)

            for service in Group[2]:

                if(self.validService(service[0])):

                    serviceObject = Service(ServiceGroupObject,service[0],service[1])
                    serviceObject.pack( fill=X,padx=10,pady=7)

            self.NumberStyle += 1

    # #Valida se o Serviço está disponível no Windows
    def validService(self,nameService=''):

        StringErro = ""

        try:

            win32.lib.win32serviceutil.QueryServiceStatus(nameService)
            return True
        except Exception as e:

            StringErro+= '###########################################################\n'
            StringErro+= "Erro no Serviço: " + nameService + "\t" + "Erro: " + str(e) + "\n"
            StringErro+= '###########################################################\n'

            self.log.consoleLogAdd(StringErro)

            return False
