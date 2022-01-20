import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de E-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Button('Enviar')]
        ]

        # Janela
        janela = sg.Window('Dados do Usuário', layout)

        # Extrair os dados da tela
        self.button, self.values = janela.Read()


    def Iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        aceita_gmail = self.values['gmail']
        aceita_outlook = self.values['outlook']
        aceita_yahoo = self.values['yahoo']
        aceita_cartao = self.values['aceitaCartao']
        nao_aceita_cartao = self.values['naoAceitaCartao']

        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'aceita Gmail: {aceita_gmail}')
        print(f'aceita Outlook: {aceita_outlook}')
        print(f'aceita Yahoo: {aceita_yahoo}')
        print(f'aceita cartão: {aceita_cartao}')
        print(f'não aceita cartão: {nao_aceita_cartao}')



tela = TelaPython()
tela.Iniciar()