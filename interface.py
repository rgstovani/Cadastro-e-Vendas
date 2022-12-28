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
               [sg.Text('Unidade:'), sg.Combo(['Unitario', 'Kg', 'Pacote', 'Caixa'], key='-unidade-', size=(15,1)), sg.Text('Valor'), sg.Input(key='-valor-', size=(15,1))],
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
def tela_consulta_cliente():
    clientes = consulta_clientes_bd()
    janela11 = [[sg.Table(clientes, justification='left', headings=['ID', 'NOME', 'CPF', 'TELEFONE', 'EMAIL', 'CEP', 'ENDERECO', 'NUM', 'BAIRRO', 'CIDADE', 'ESTADO'])],
                [sg.Button('Voltar')]]

    return sg.Window('Consulta de Clientes', janela11, finalize=True)
def tela_consulta_produtos():
    produtos = consulta_produtos_bd()
    janela12 = [[sg.Table(produtos, justification='left', headings=['ID', 'PRODUTO', 'MARCA', 'UNIDADE', 'VALOR'])],
                [sg.Button('Voltar')]]

    return sg.Window('Consulta de Produtos', janela12, finalize=True)
def tela_consulta_vendas():
    # vendas = tela_consulta_vendas()
    janela13 = [[sg.Table('vendas', justification='left', headings=['ID', 'PRODUTO', 'MARCA', 'UNIDADE', 'VALOR'])],
                [sg.Button('Voltar')]]

    return sg.Window('Consulta de Vendas', janela13, finalize=True)


janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, \
janela11, janela12, janela13 = tela_login(), None, None, None, None, None, None, None, None, None, None, None, None

while True:
    cria_bd()
    janela, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break

    if janela == janela1:   #Interações Janela 1 - Tela Login
        if eventos == 'Login':
            if (valores['-usuario-'] == 'admin') and (valores['-senha-'] == 'admin'):
                janela1.hide()
                janela3 = tela_menu_admin()
            else:
                login = teste_login(valores['-usuario-'], valores['-senha-'])
                if login == False:
                    sg.Popup('Usuario/senha invalido.')
                if login == True:
                    janela1.hide()
                    janela3 = tela_menu_admin()

        if eventos == 'Esqueci a Senha':
            janela1.hide()
            janela2 = tela_esqueci_senha()

    if janela == janela2:   #Interações Janela 2 - Alterar Senha
        if eventos == 'Alterar Senha':
            janela2.disable()
            janela10 = tela_redefinir_senha()
        if eventos == 'Voltar':
            janela2.hide()
            janela1 = tela_login()

    if janela == janela3:   #Interações Janela 3 - Menu ADM
        if eventos == 'Novo Cliente':
            janela3.hide()
            janela7 = tela_cadastro_cliente()
        if eventos == 'Consultar Cliente':
            janela3.hide()
            janela11 = tela_consulta_cliente()
        if eventos == 'Nova Venda':
            janela3.hide()
            janela9 = tela_nova_venda()
        if eventos == 'Consultar Venda':
            janela3.hide()
            janela13 = tela_consulta_vendas()
        if eventos == 'Novo Usuario':
            janela3.hide()
            janela5 = tela_cadastrar_usuario()
        if eventos == 'Excluir Usuario':
            janela3.hide()
            janela6 = tela_exclusao()
        if eventos == 'Novo Produto':
            janela3.hide()
            janela8 = tela_cadastro_produtos()
        if eventos == 'Consultar Produto':
            janela3.hide()
            janela12 = tela_consulta_produtos()
    # Interações Janela 4 - Menu User



    if janela == janela5:   # Interações Janela 5 - Cadastro de Usuario
        if eventos == 'Cadastrar':
            cadastra_user(valores['-usuario-'], valores['-senha-'], valores['-email-'])
            sg.PopupOK('Usuario Cadastrado')
            janela5.hide()
            janela5 = tela_cadastrar_usuario()
        if eventos == 'Voltar':
            janela5.hide()
            janela3 = tela_menu_admin()

    if janela == janela6:   # Interações Janela 6 - Exclusão de Usuario
        if eventos == 'Confirmar':
            pass
        if eventos == 'Voltar':
            janela6.hide()
            janela3 = tela_menu_admin()

    if janela == janela7:   # Interações Janela 7 - Cadastro de Cliente
        if eventos == 'Validar':
            validade_cpf = validador_cpf(valores['-cpf-'])
            if validade_cpf == True:
                sg.Popup('CPF Valido.')
            if validade_cpf == False:
                sg.Popup('CPF Invalido.')

        if eventos == 'Verificar':
            cep = valores['-cep-']
            cep = cep.replace('-','').replace('.', '').replace(' ','')
            if len(cep) == 8:
                r = consulta_cep(cep)
                janela7['-endereco-'].update(r[1])
                janela7['-bairro-'].update(r[2])
                janela7['-cidade-'].update(r[3])
                janela7['-estado-'].update(r[4])
            else:
                sg.Popup('CEP invalido.')

        if eventos == 'Cadastrar':
            if valores['-nome-'] or valores['-cpf-'] or valores['-telefone-'] or valores['-email-'] or \
                    valores['-cep-'] or valores['-endereco-'] or valores['-num-'] or valores['-bairro-'] or \
                    valores['-cidade-'] or valores['-estado-'] != "":
                validade_cpf = validador_cpf(valores['-cpf-'])
                if validade_cpf == True:
                    add_clientes_bd(valores['-nome-'], valores['-cpf-'], valores['-telefone-'], valores['-email-'],
                                    valores['-cep-'], valores['-endereco-'], valores['-num-'], valores['-bairro-'],
                                    valores['-cidade-'], valores['-estado-'])
                    sg.Popup('Cliente Cadastrado\ncom sucesso!')
                    janela7.hide()
                    janela7 = tela_cadastro_cliente()
                else:
                    sg.Popup('Verifique o CPF do Cliente.')
            else:
                sg.Popup('Preencha todos os campos.')

        if eventos == 'Voltar':
            janela7.hide()
            janela3 = tela_menu_admin()

    if janela == janela8:   # Interações Janela 8 - Cadastro de Produtos
        if eventos == 'Cadastrar':
            if valores['-produto-'] or valores['-marca-'] or valores['-unidade-'] or valores['-valor-'] != "":
                add_produtos_bd(valores['-produto-'],valores['-marca-'],valores['-unidade-'],valores['-valor-'])
                sg.Popup('Produto cadastrado.')
                janela8.hide()
                janela8 = tela_cadastro_produtos()
            else:
                sg.Popup('Preencha todos os campos.')

        if eventos == 'Voltar':
            janela8.hide()
            janela3 = tela_menu_admin()


    if janela == janela9:   # Interações Janela 9 - Nova Venda
        if eventos == 'Adicionar':
            pass

        if eventos == 'Finalizar Venda':
            pass

        if eventos == 'Voltar':
            janela9.hide()
            janela3 = tela_menu_admin()

    if janela == janela10:  # Interações Janela 10 - Redefinir Senha
        if eventos == 'Redefinir':
            pass

        if eventos == 'Cancelar':
            janela2.hide()
            janela10.hide()
            janela1 = tela_login()

    if janela == janela11:  # Interações Janela 11 - Consulta Clientes
        if eventos == 'Voltar':
            janela11.hide()
            janela3 = tela_menu_admin()

    if janela == janela12:  # Interações Janela 12 - Consulta Clientes
        if eventos == 'Voltar':
            janela12.hide()
            janela3 = tela_menu_admin()

    if janela == janela13:  # Interações Janela 13 - Consulta Vendas
        if eventos == 'Voltar':
            janela13.hide()
            janela3 = tela_menu_admin()

janela.close()