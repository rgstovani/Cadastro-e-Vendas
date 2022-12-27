import PySimpleGUI as sg
from funcoes_banco import *

sg.theme('DarkPurple')

def tela_login():
    janela1 = [[sg.Text('Usuario:')],
               [sg.Input(key='-usuario-', size=(30,1))],
               [sg.Text('Senha:')],
               [sg.Input(key='-senha-', size=(30,1), password_char='*')],
               [sg.Button('Login'), sg.Push(), sg.Button('Esqueci a Senha')]]
    return sg.Window('Tela de Login', janela1, finalize=True)
def tela_esqueci_senha():
    janela2 = [[sg.Text('Usuario:')],
               [sg.Input(key='-usuario-', size=(30,1))],
               [sg.Text('E-mail:')],
               [sg.Input(key='-email-', size=(30,1))],
               [sg.Button('Alterar Senha'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Esqueci a Senha', janela2, finalize=True)
def tela_menu_admin():
    janela3 = [[sg.Button('Novo Cliente', size=(17,1)), sg.Button('Novo Usuario', size=(17,1))],
               [sg.Button('Consultar Cliente', size=(17,1)), sg.Button('Excluir Usuario', size=(17,1))],
               [sg.Button('Nova Venda', size=(17,1)), sg.Button('Novo Produto', size=(17,1))],
               [sg.Button('Consultar Venda', size=(17,1)), sg.Button('Consultar Produto', size=(17,1))],
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
               [sg.Input(key='-usuario-', size=(20,1))],
               [sg.Text('Digite a Senha:')],
               [sg.Input(key='-senha-', size=(15,1))],
               [sg.Text('Repita a Senha:')],
               [sg.Input(key='-repsenha-', size=(15,1))],
               [sg.Text('Digite o E-mail')],
               [sg.Input(key='-email-', size=(30,1))],
               [sg.Button('Cadastrar'), sg.Push(), sg.Button('Voltar')],
    ]
    return sg.Window('Cadastrar novo usuario', janela5, finalize=True)
def tela_exclusao():
    janela6 = [[sg.Text('Selecione o usuario a ser excluido:')],
               [sg.Combo('usuarios', size=(20,1))],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Exclusão', janela6, finalize=True)
def tela_cadastro_cliente():
    frame1 = [[sg.Text('Nome: '), sg.Input(key='-nome-', size=(40,1)), sg.Text('CPF:'), sg.Input(key='-cpf-', size=(15,1)), sg.Button('Validar', size=(10,1))],
              [sg.Text('Telefone: '), sg.Input(key='-telefone-', size=(20,1)), sg.Text('E-mail:'), sg.Input(key='-email-', size=(45,1))]]

    frame2 = [[sg.Text('CEP:'),sg.Input(key='-cep-', size=(15,1)), sg.Button('Verificar', size=(10,1))],
              [sg.Text('Endereço: '), sg.Input(key='-endereco-', size=(58,1)), sg.Text('Nº:'), sg.Input(key='-num-', size=(10,1))],
              [sg.Text('Bairro: '), sg.Input(key='-bairro-', size=(25,1)), sg.Text('Cidade:'), sg.Input(key='-cidade-', size=(25,1)),
               sg.Text('Estado:'), sg.Input(key='-estado-', size=(7,1))]]
    janela7 = [[sg.Text('Cadastro de Clientes')],
               [sg.Frame('Cliente', frame1)],
               [sg.Frame('Endereço', frame2)],
               [sg.Button('Cadastrar', size=(10,1)), sg.Button('Voltar', size=(10,1))]]

    return sg.Window('Cadastro de Cliente', janela7, finalize=True)
def tela_cadastro_produtos():
    janela8 = [[sg.Text('Produto: '), sg.Input(key='-produto-', size=(30,1)), sg.Text('Marca:'), sg.Input(key='-marca-', size=(20,1))],
               [sg.Text('Unidade:'), sg.Combo(['Unitario', 'Kg', 'Pacote', 'Caixa'], size=(15,1)), sg.Text('Valor'), sg.Input(key='-valor-', size=(15,1))],
               [sg.Button('Cadastrar'), sg.Button('Voltar')]]
    return sg.Window('Cadastro de Produtos', janela8, finalize=True)
def tela_nova_venda():
    pagamento = ['Dinheiro', 'Cartão de Debito', 'Cartão de Credito', 'Cheque']
    dados = 'teste'
    frame1 = [[sg.Table(dados, def_col_width=16, auto_size_columns=False, headings=['Quant.', 'Produto', 'Valor Unitario', 'Valor Total'])]]
    frame2 = [[sg.Text('Endereço:'), sg.Text(size=(30,1)), sg.Text('Numero:'), sg.Text(size=(8,1)), sg.Text('Cidade:'), sg.Text(size=(20,1))]]
    frame3 = [[sg.Text('Forma de Pagto'), sg.Combo(pagamento), sg.Text('Valor Total'), sg.Text(key='-valortotal-', size=(10,1))]]

    janela9 = [[sg.Text('Cliente:'), sg.Text('')],
               [sg.Frame('Endereço', frame2)],
               [sg.Frame('Produtos', frame1), sg.Button('Adicionar')],
               [sg.Frame('Pagamento', frame3)],
               [sg.Button('Finalizar Venda'), sg.Button('Voltar')]]
    return sg.Window('Nova Venda', janela9, finalize=True)
def tela_redefinir_senha():
    janela10 = [[sg.Text('Digite a nova senha: '), sg.Input(key='-novasenha-', size=(20,1))],
                [sg.Text('Repita a nova senha: '), sg.Input(key='-repnovasenha-', size=(20,1))],
                [sg.Button('Redefinir'), sg.Push(), sg.Button('Cancelar')]]

    return sg.Window('Redefinição de Senha', janela10, finalize=True)

janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, janela11 = tela_login(), None, None, None, None, None, None, None, None, None, None

while True:
    cria_bd_usuarios()
    cria_bd_clientes()
    janela, eventos, valores = sg.read_all_windows()
    print(eventos, valores)
    if eventos == sg.WIN_CLOSED:
        break

    #Interações Janela 1 - Tela Login
    if janela == janela1 and eventos == 'Login':
        login = teste_login(valores['-usuario-'], valores['-senha-'])
        if login == False:
            sg.Popup('Usuario/senha invalido.')
        if login == True:
            janela1.hide()
            janela3 = tela_menu_admin()

    if janela == janela1 and eventos == 'Esqueci a Senha':
        janela1.hide()
        janela2 = tela_esqueci_senha()

    #Interações Janela 2 - Alterar Senha
    if janela == janela2 and eventos == 'Alterar Senha':
        janela2.disable()
        janela10 = tela_redefinir_senha()
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
        janela9 = tela_nova_venda()
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
        cadastra_user(valores['-usuario-'], valores['-senha-'], valores['-email-'])
        sg.PopupOK('Usuario Cadastrado')
        janela5.hide()
        janela5 = tela_cadastrar_usuario()

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
        add_clientes_bd(valores['-nome-'], valores['-cpf-'], valores['-telefone-'], valores['-email-'],
                        valores['-cep-'], valores['-endereco-'], valores['-num-'], valores['-bairro-'],
                        valores['-cidade-'], valores['-estado-'])
        janela7.hide()
        janela7 = tela_cadastro_cliente()
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
    if janela == janela9 and eventos == 'Adicionar':
        pass
    if janela == janela9 and eventos == 'Finalizar Venda':
        pass
    if janela == janela9 and eventos == 'Voltar':
        janela9.hide()
        janela3 = tela_menu_admin()

    # Interações Janela 10 - Redefinir Senha
    if janela == janela10 and eventos == 'Redefinir':
        pass
    if janela == janela10 and eventos == 'Cancelar':
        janela2.hide()
        janela10.hide()
        janela1 = tela_login()

janela.close()