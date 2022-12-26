import PySimpleGUI as sg
from addrow import *

def tela_login():
    janela1 = [[sg.Text('Usuario:')],
               [sg.Input(key='Usuario')],
               [sg.Text('Senha:')],
               [sg.Input(key='Senha')],
               [sg.Button('Login'), sg.Button('Esqueci a Senha')]]
    return sg.Window('Tela de Login', janela1, finalize=True)
def tela_esqueci_senha():
    janela2 = [[sg.Text('Usuario:')],
               [sg.Input(key='Usuario')],
               [sg.Text('E-mail:')],
               [sg.Input(key='email')],
               [sg.Button('Alterar Senha'), sg.Button('Voltar')]]
    return sg.Window('Esqueci a Senha', janela2, finalize=True)
def tela_menu_admin():
    janela3 = [[sg.Button('Novo Cliente'), sg.Button('Novo Usuario')],
               [sg.Button('Consultar Cliente'), sg.Button('Excluir Usuario')],
               [sg.Button('Nova Venda'), sg.Button('Novo Produto')],
               [sg.Button('Consultar Venda'), sg.Button('Consultar Produto')],
               ]
    return sg.Window('Menu de Opções', janela3, finalize=True, element_justification='center')
def tela_menu_user():
    janela4 = [[sg.Button('Novo Cliente')],
               [sg.Button('Consultar Cliente')],
               [sg.Button('Nova Venda')],
               [sg.Button('Consultar Venda')],
               ]
    return sg.Window('Menu de Opções', janela4, finalize=True, element_justification='center')
def tela_cadastrar_usuario():
    janela5 = [[sg.Text('Digite o Usuario:')],
               [sg.Input(key='usuario')],
               [sg.Text('Digite a Senha:')],
               [sg.Input(key='senha')],
               [sg.Text('Repita a Senha:')],
               [sg.Input(key='repsenha')],
               [sg.Text('Digite o E-mail')],
               [sg.Input(key='email')],
               [sg.Button('Cadastrar'), sg.Button('Voltar')],
    ]
    return sg.Window('Cadastrar novo usuario', janela5, finalize=True)
def tela_exclusao():
    janela6 = [[sg.Input('Selecione o usuario a ser excluido:')],
               ["sg.Combo()"],
               [sg.Button('Confirmar'), sg.Button('Voltar')]]
    return sg.Window('Exclusão', janela6, finalize=True)
def tela_cadastro_cliente():
    frame1 = [[sg.Text('Nome: '), sg.Input(key='nome'), sg.Text('CPF:'), sg.Input(key='cpf'), sg.Button('Validar')],
              [sg.Text('Telefone: '), sg.Input(key='telefone'), sg.Text('E-mail:'), sg.Input(key='email')]]

    frame2 = [[sg.Text('CEP:'),sg.Input(key='cep'), sg.Button('Verificar')],
              [sg.Text('Endereço: '), sg.Input(key='endereco'), sg.Text('Nº:'), sg.Input(key='num')],
              [sg.Text('Bairro: '), sg.Input(key='bairro'), sg.Text('Cidade:'), sg.Input(key='cidade'),
               sg.Text('Estado:'), sg.Input(key='estado')]]
    janela7 = [[sg.Text('Cadastro de Clientes')],
               [sg.Frame('', frame1)],
               [sg.Frame('', frame2)],
               [sg.Button('Cadastrar'), sg.Button('Voltar')]]

    return sg.Window('Cadastro de Cliente', janela7, finalize=True)
def tela_cadastro_produtos():
    janela8 = [[sg.Text('Produto: '), sg.Input(key='produto'), sg.Text('Marca:'), sg.Input(key='marca')],
               [sg.Text('Unidade:'), sg.Combo(['Unitario', 'Kg', 'Pacote', 'Caixa'], size=(15,1)), sg.Text('Valor'), sg.Input(key='valor')],
               [sg.Button('Cadastrar'), sg.Button('Voltar')]]
    return sg.Window('Cadastro de Produtos', janela8, finalize=True)






janela = tela_cadastro_produtos()
while True:
    janela, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break

janela.close()