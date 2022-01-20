import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue')
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de E-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider((0,255), 0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar')],
            [sg.Output((30,20))]
        ]

        # Janela
        self.janela = sg.Window('Dados do Usuário', layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            slider_velocidade = self.values['sliderVelocidade']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita Gmail: {aceita_gmail}')
            print(f'aceita Outlook: {aceita_outlook}')
            print(f'aceita Yahoo: {aceita_yahoo}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'não aceita cartão: {nao_aceita_cartao}')
            print(f'slider velocidade: {slider_velocidade}')



tela = TelaPython()
tela.Iniciar()