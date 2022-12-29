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
               [sg.Input(key='-senha-', size=(15,1), password_char='*')],
               [sg.Text('Repita a Senha:')],
               [sg.Input(key='-repsenha-', size=(15,1), password_char='*')],
               [sg.Text('Digite o E-mail')],
               [sg.Input(key='-email-', size=(30,1))],
               [sg.Button('Cadastrar'), sg.Push(), sg.Button('Voltar')],
    ]
    return sg.Window('Cadastrar novo usuario', janela5, finalize=True)
def tela_exclusao():
    usuarios = retorna_lista_user_bd()
    janela6 = [[sg.Text('Selecione o usuario a ser excluido:')],
               [sg.Combo(usuarios, size=(20,1), key='del_selecao')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Exclusão de Usuarios', janela6, finalize=True)
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
    frame1 = [[sg.Table(values=dados, headings=['Produto', 'Marca', 'Valor Unitario', 'Quant.', 'Valor Total'],
                        key='-tabela-', col_widths=[16,16,16,8,12], auto_size_columns=False, justification='left',
                        background_color='gray', text_color='black', enable_events=True)]]
    frame2 = [[sg.Text('Rua:'), sg.Input(size=(30,1), key='-endereco-'), sg.Text('Numero:'),
               sg.Input(size=(8,1), key='-num-'), sg.Text('Cidade:'), sg.Input(size=(20,1), key='-cidade-')]]
    frame3 = [[sg.Text('Forma de Pagto'), sg.Combo(pagamento), sg.Push(), sg.Text('Valor Total: R$', font=("Helvetica", 16)),
               sg.Input(key='-valortotal-', size=(10,1), font=("Helvetica", 20))]]

    janela9 = [[sg.Text('Cliente:'), sg.Input('',key='-cliente-'),sg.Push(), sg.Button('Selecione o Cliente')],
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
                [sg.Button('Voltar'), sg.Push(), sg.Button('Excluir')]]

    return sg.Window('Consulta de Clientes', janela11, finalize=True)
def tela_consulta_produtos():
    produtos = consulta_produtos_bd()
    janela12 = [[sg.Table(produtos, justification='left', headings=['ID', 'PRODUTO', 'MARCA', 'UNIDADE', 'VALOR'])],
                [sg.Button('Voltar'), sg.Push(), sg.Button('Excluir')]]

    return sg.Window('Consulta de Produtos', janela12, finalize=True)
def tela_consulta_vendas():
    # vendas = tela_consulta_vendas()
    janela13 = [[sg.Table('vendas', justification='left', headings=['ID', 'PRODUTO', 'MARCA', 'UNIDADE', 'VALOR'])],
                [sg.Button('Voltar')]]

    return sg.Window('Consulta de Vendas', janela13, finalize=True)
def tela_excluir_produto():
    produtos = retornar_produto_bd()
    janela14 = [[sg.Text('Selecione o produto a ser excluido:')],
               [sg.Combo(produtos, size=(20,1), key='del_selecao_prod')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Exclusão de Produto', janela14, finalize=True)
def tela_excluir_cliente():
    clientes = retornar_cliente_bd()
    janela15 = [[sg.Text('Selecione o cliente a ser excluido:')],
               [sg.Combo(clientes, size=(20,1), key='del_selecao_cli')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Exclusão de Cliente', janela15, finalize=True)
def tela_cons_cliente():
    clientes = retornar_cliente_bd()
    janela16 = [[sg.Text('Selecione o cliente:')],
               [sg.Combo(clientes, size=(20,1), key='compra_selecao_cli')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Seleção de Cliente', janela16, finalize=True)
def tela_adiciona_produto():
    lista = retorna_lista_produto_bd()
    janela17 = [[sg.Text('Selecione o Produto:')],
                [sg.Combo(lista, size=(15,1), key='-selec_prod-'), sg.Spin([1,2,3,4,5,6,7,8,9], initial_value=1, size=(3,1))],
                [sg.Button('Adicionar'), sg.Button('Cancelar')]]

    return sg.Window('Adiciona Produto', janela17, finalize=True)


janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, \
janela11, janela12, janela13, janela14, janela15, janela16, janela17 = tela_login(), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

dados = []
v = []

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
            if valores['-senha-'] == valores['-repsenha-']:
                cadastra_user(valores['-usuario-'], valores['-senha-'], valores['-email-'])
                sg.PopupOK('Usuario Cadastrado')
                janela5.hide()
                janela5 = tela_cadastrar_usuario()
            else:
                sg.Popup('As Senhas não coincidem.')
        if eventos == 'Voltar':
            janela5.hide()
            janela3 = tela_menu_admin()

    if janela == janela6:   # Interações Janela 6 - Exclusão de Usuario
        if eventos == 'Confirmar':
            selecao = valores['del_selecao']
            deleta_user_bd(selecao)
            sg.PopupOK('Usuario deletado.')
            janela6.hide()
            janela6 = tela_exclusao()

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
            if valores['-nome-'] and valores['-cpf-'] and valores['-telefone-'] and valores['-email-'] and \
                    valores['-cep-'] and valores['-endereco-'] and valores['-num-'] and valores['-bairro-'] and \
                    valores['-cidade-'] and valores['-estado-'] != "":
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
        if eventos == 'Selecione o Cliente':
            janela9.disable()
            janela16 = tela_cons_cliente()

        if eventos == 'Adicionar':
            janela9.disable()
            janela17 = tela_adiciona_produto()

        if eventos == 'Finalizar Venda':

            pass


        if eventos == 'Voltar':
            dados = []
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
        if eventos == 'Excluir':
            janela11.disable()
            janela15 = tela_excluir_cliente()

        if eventos == 'Voltar':
            janela11.hide()
            janela3 = tela_menu_admin()

    if janela == janela12:  # Interações Janela 12 - Consulta Produtos
        if eventos == 'Excluir':
            janela12.disable()
            janela14 = tela_excluir_produto()

        if eventos == 'Voltar':
            janela12.hide()
            janela3 = tela_menu_admin()

    if janela == janela13:  # Interações Janela 13 - Consulta Vendas
        if eventos == 'Voltar':
            janela13.hide()
            janela3 = tela_menu_admin()

    if janela == janela14:  # Interações Janela 14 - Exclusão de Produtos
        if eventos == 'Confirmar':
            selecao = valores['del_selecao_prod']
            deleta_produto_bd(selecao)
            sg.PopupOK('Produto deletado.')
            janela12.close()
            janela12 = tela_consulta_produtos()
            janela14.hide()

        if eventos == 'Voltar':
            janela12.enable()
            janela14.hide()

    if janela == janela15:  # Interações Janela 14 - Exclusão de Clientes
        if eventos == 'Confirmar':
            selecao = valores['del_selecao_cli']
            deleta_cliente_bd(selecao)
            sg.PopupOK('cliente deletado.')
            janela11.close()
            janela11 = tela_consulta_cliente()
            janela15.hide()

        if eventos == 'Voltar':
            janela11.enable()
            janela15.hide()

    if janela == janela16:  # Interações Janela 16 - Exclusão de Clientes
        if eventos == 'Confirmar':
            selecao = valores['compra_selecao_cli']
            info_cliente = retornar_info_cliente_bd(selecao)
            janela9.enable()
            janela9['-cliente-'].update(info_cliente[0][0])
            janela9['-endereco-'].update(info_cliente[0][5])
            janela9['-num-'].update(info_cliente[0][6])
            janela9['-cidade-'].update(info_cliente[0][8])
            janela16.hide()

        if eventos == 'Voltar':
            janela9.enable()
            janela16.hide()

    if janela == janela17:

        if eventos == 'Adicionar':
            if valores['-selec_prod-'] != '':
                produto = valores['-selec_prod-']
                quant = int(valores[0])
                iprod = (retornar_info_produto_bd(produto))
                v_total = (int(iprod[0][3]) * quant)
                v.append(int(v_total))

                print(sum(v))

                dados.append([iprod[0][0], iprod[0][1], iprod[0][3], quant, v_total])

                janela9['-tabela-'].update(values=dados)
                janela9['-valortotal-'].update(sum(v))

                janela9.enable()
                janela17.hide()


        if eventos == 'Cancelar':
            janela9.enable()
            janela17.hide()

    print(eventos, valores)
janela.close()

