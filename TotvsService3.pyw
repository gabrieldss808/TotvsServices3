######################################################
## TotvsService3                                    ##
## Description: Projeto de app para gerenciar       ##
## os serviços do windows voltado para os serviços  ##
## da Estrutura do Protheus.                        ##
##                                                  ##
## Versão: 3.0 15/07/2020                           ##
######################################################

from TotvsServiceClassMain import TotvsService3

AppExec = TotvsService3()

AppExec.configTotvsServiceLayout()
AppExec.iniScheduleAtuService()

AppExec.mainloop()

AppExec.closingApp()