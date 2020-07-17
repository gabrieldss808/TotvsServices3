# TotvsServices3
Projeto de app para gerenciar os serviços do windows voltado para os serviços da Estrutura do Protheus.

# Visão Geral

O Aplicativo controla os serviços atrávez de grupos, onde é possivel iniciar e parar os serviços:

![image](https://user-images.githubusercontent.com/45453977/87826175-ca952e00-c84e-11ea-8284-dae3ad48125c.png)

# Download 

[Totvs Service 3](dist/TotvsService3.rar)

# How to use

***Controlando os Grupos:***

![startStopGroup](https://user-images.githubusercontent.com/45453977/87829049-93c21680-c854-11ea-8b39-998d0a8928d0.gif)

<H3>Configurando o App: </H3>

![Uso](https://user-images.githubusercontent.com/45453977/87829131-c4a24b80-c854-11ea-9ae2-580847ba31e2.gif)

***Tags do CSV de configuração:***

Tag Group: indica o inicio de um grupo

Para configura-lá é preciso colocar da seguine maneira: 

Group;Nome Descritivo do Grupo;Numero Indicando o Delay em cada passagem

***Sobre o Delay:*** é numerico e indica que for iniciado um grupo ou parado, na iniciação de cada serviço ocorre um intervalo de iniciação, não permitindo iniciar ou parar os serviços todos de uma vez.(se não for informado o intervalo será de um 1 segundo).
