import PySimpleGUI as sg
from funcoes_banco import *
from main import dados

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

    frame2 = [[sg.Text('Rua:'), sg.Input(size=(40,1), key='-endereco-'), sg.Text('Numero:'),
               sg.Input(size=(8,1), key='-num-'), sg.Text('Cidade:'), sg.Input(size=(25,1), key='-cidade-')]]

    frame3 = [[sg.Text('Forma de Pagto'), sg.Combo(pagamento, key='-pagto-'), sg.Push(),
               sg.Text('Valor Total: R$', font=("Helvetica", 16)),
               sg.Input(key='-valortotal-', size=(10,1), font=("Helvetica", 16))]]

    janela9 = [[sg.Text('Cliente:'), sg.Input('',key='-cliente-', size=(60,1)),sg.Push(), sg.Button('Selecione o Cliente')],
               [sg.Frame('Endereço', frame2, size=(720,50))],
               [sg.Frame('Produtos', frame1), sg.Button('Adicionar')],
               [sg.Frame('Pagamento', frame3, size=(720,60))],
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
    vendas = consulta_vendas_bd()
    janela13 = [[sg.Table(vendas, justification='left', headings=['ID', 'DATA', 'CLIENTE', 'RUA', 'NUMERO', 'CIDADE', 'PAGAMENTO', 'VALOR'])],
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



