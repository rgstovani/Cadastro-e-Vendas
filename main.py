import PySimpleGUI as sg
#from addrow import *

def tela_login():
    janela1 = [[sg.Text('Usuario:')],
               [sg.Input(key='-usuario-')],
               [sg.Text('Senha:')],
               [sg.Input(key='-senha-')],
               [sg.Button('Login'), sg.Button('Esqueci a Senha')]]
    return sg.Window('Tela de Login', janela1, finalize=True)
def tela_esqueci_senha():
    janela2 = [[sg.Text('Usuario:')],
               [sg.Input(key='-usuario-')],
               [sg.Text('E-mail:')],
               [sg.Input(key='-email-')],
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
               [sg.Input(key='-usuario-')],
               [sg.Text('Digite a Senha:')],
               [sg.Input(key='-senha-')],
               [sg.Text('Repita a Senha:')],
               [sg.Input(key='-repsenha-')],
               [sg.Text('Digite o E-mail')],
               [sg.Input(key='-email-')],
               [sg.Button('Cadastrar'), sg.Button('Voltar')],
    ]
    return sg.Window('Cadastrar novo usuario', janela5, finalize=True)
def tela_exclusao():
    janela6 = [[sg.Text('Selecione o usuario a ser excluido:')],
               [sg.Combo('usuarios', size=(20,1))],
               [sg.Button('Confirmar'), sg.Button('Voltar')]]
    return sg.Window('Exclusão', janela6, finalize=True)
def tela_cadastro_cliente():
    frame1 = [[sg.Text('Nome: '), sg.Input(key='-nome-'), sg.Text('CPF:'), sg.Input(key='-cpf-'), sg.Button('Validar')],
              [sg.Text('Telefone: '), sg.Input(key='-telefone-'), sg.Text('E-mail:'), sg.Input(key='-email-')]]

    frame2 = [[sg.Text('CEP:'),sg.Input(key='cep'), sg.Button('Verificar')],
              [sg.Text('Endereço: '), sg.Input(key='-endereco-'), sg.Text('Nº:'), sg.Input(key='-num-')],
              [sg.Text('Bairro: '), sg.Input(key='-bairro-'), sg.Text('Cidade:'), sg.Input(key='-cidade-'),
               sg.Text('Estado:'), sg.Input(key='-estado-')]]
    janela7 = [[sg.Text('Cadastro de Clientes')],
               [sg.Frame('', frame1)],
               [sg.Frame('', frame2)],
               [sg.Button('Cadastrar'), sg.Button('Voltar')]]

    return sg.Window('Cadastro de Cliente', janela7, finalize=True)
def tela_cadastro_produtos():
    janela8 = [[sg.Text('Produto: '), sg.Input(key='-produto-'), sg.Text('Marca:'), sg.Input(key='-marca-')],
               [sg.Text('Unidade:'), sg.Combo(['Unitario', 'Kg', 'Pacote', 'Caixa'], size=(15,1)), sg.Text('Valor'), sg.Input(key='-valor-')],
               [sg.Button('Cadastrar'), sg.Button('Voltar')]]
    return sg.Window('Cadastro de Produtos', janela8, finalize=True)
def nova_venda():
    pagamento = ['Dinheiro', 'Cartão de Debito', 'Cartão de Credito', 'Cheque']
    dados = 'teste'
    frame1 = [[sg.Table(dados, headings=['Quant.', 'Produto', 'Valor Unitario', 'Valor Total'])]]
    frame2 = [[sg.Text('Endereço:'), sg.Text('Numero:'), sg.Text('Cidade:')]]
    frame3 = [[sg.Text('Forma de Pagto'), sg.Combo(pagamento), sg.Text('Valor Total'), sg.Text(key='-valortotal-')]]

    janela9 = [[sg.Text('Cliente:')],
               [sg.Frame('Endereço', frame2)],
               [sg.Frame('Produtos', frame1), sg.Button('Adicionar')],
               [sg.Frame('Pagamento', frame3)],
               [sg.Button('Finalizar Venda'), sg.Button('Voltar')]]
    return sg.Window('Nova Venda', janela9, finalize=True)

janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9 = tela_login(), None, None, None, None, None, None, None, None

while True:
    janela, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break

#Interações Janela 1 - Tela Login
    if janela == janela1 and eventos == 'Login':
        janela1.hide()
        janela3 = tela_menu_admin()
    if janela == janela1 and eventos == 'Esqueci a Senha':
        janela1.hide()
        janela2 = tela_esqueci_senha()

#Interações Janela 2 - Alterar Senha
    if janela == janela2 and eventos == 'Alterar Senha':
        pass
    if janela == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1 = tela_login()

#Interações Janela 3 - Menu ADM
    if janela == janela3 and eventos == 'Novo Cliente':
        janela3.hide()
        janela7 = tela_cadastro_cliente()
    if janela == janela3 and eventos == 'Consultar Cliente':
        pass
    if janela == janela3 and eventos == 'Nova Venda':
        janela3.hide()
        janela9 = nova_venda()
    if janela == janela3 and eventos == 'Consultar Venda':
        pass
    if janela == janela3 and eventos == 'Novo Usuario':
        janela3.hide()
        janela5 = tela_cadastrar_usuario()
    if janela == janela3 and eventos == 'Excluir Usuario':
        janela3.hide()
        janela6 = tela_exclusao()
    if janela == janela3 and eventos == 'Novo Produto':
        janela3.hide()
        janela8 = tela_cadastro_produtos()
    if janela == janela3 and eventos == 'Consultar Produto':
        pass

# Interações Janela 4 - Menu User



# Interações Janela 5 - Cadastro de Usuario
    if janela == janela5 and eventos == 'Cadastrar':
        pass
    if janela == janela5 and eventos == 'Voltar':
        janela5.hide()
        janela3 = tela_menu_admin()

# Interações Janela 6 - Exclusão de Usuario
    if janela == janela6 and eventos == 'Confirmar':
        pass
    if janela == janela6 and eventos == 'Voltar':
        janela6.hide()
        janela3 = tela_menu_admin()

# Interações Janela 7 - Cadastro de Cliente
    if janela == janela7 and eventos == 'Validar':
        pass
    if janela == janela7 and eventos == 'Verificar':
        pass
    if janela == janela7 and eventos == 'Cadastrar':
        pass
    if janela == janela7 and eventos == 'Voltar':
        janela7.hide()
        janela3 = tela_menu_admin()

# Interações Janela 8 - Cadastro de Produtos
    if janela == janela8 and eventos == 'Cadastrar':
        pass
    if janela == janela8 and eventos == 'Voltar':
        janela8.hide()
        janela3 = tela_menu_admin()

# Interações Janela 9 - Nova Venda
    if janela == janela9 and eventos == 'Finalizar Venda':
        pass
    if janela == janela9 and eventos == 'Voltar':
        janela9.hide()
        janela3 = tela_menu_admin()

janela.close()