# Simulador de dado 
# Simular o uso de um dado, gerando um valor de 1 até 6 
import random 
import PySimpleGUI as sg

class SimuladorDeDado: 
    def __init__(self): 
        self.valor_minimo = 1 
        self.valor_maximo = 6 
        # LAYOUT 
        self.layout = [ 
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
    
    def Iniciar(self): 
        # CRIAR UMA JANELA 
        self.janela = sg.Window('Simulador de Dado',self.layout)       
        # LER OS VALORES NA TELA 
        self.eventos, self.valores = self.janela.Read()
        # FAZER ALGUMA COISA COM ESSES VALORES
        while True:
            try:
                if self.eventos == 'sim' or self.eventos == 's': 
                    self.GerarValorDoDado() 
                elif self.eventos == 'não' or self.eventos == 'n': 
                    print('Agradecemos sua participação!')
                else:
                    print('Digite sim ou não')
            except: 
                print('Ocorreu um erro ao receber sua resposta')
            
    def GerarValorDoDado(self): 
        print(random.randint(self.valor_minimo,self.valor_maximo)) 

simulador = SimuladorDeDado() 
simulador.Iniciar()
