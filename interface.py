import PySimpleGUI as sg
from funcoes_banco import *
from main import dados

sg.theme('DarkPurple')

def t_login():
    jan1 = [[sg.Text('Usuario:')],
               [sg.Input(key='-usuario-', size=(30,1))],
               [sg.Text('Senha:')],
               [sg.Input(key='-senha-', size=(30,1), password_char='*')],
               [sg.Button('Login'), sg.Push(), sg.Button('Esqueci a Senha')]]
    return sg.Window('t de Login', jan1, finalize=True)
def t_esqueci_senha():
    jan2 = [[sg.Text('Usuario:')],
               [sg.Input(key='-usuario-', size=(30,1))],
               [sg.Text('E-mail:')],
               [sg.Input(key='-email-', size=(30,1))],
               [sg.Button('Alterar Senha'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Esqueci a Senha', jan2, finalize=True)
def t_menu_admin():
    jan3 = [[sg.Button('Novo Cliente', size=(17,1)), sg.Button('Novo Usuario', size=(17,1))],
               [sg.Button('Consultar Cliente', size=(17,1)), sg.Button('Excluir Usuario', size=(17,1))],
               [sg.Button('Nova Venda', size=(17,1)), sg.Button('Novo Produto', size=(17,1))],
               [sg.Button('Consultar Venda', size=(17,1)), sg.Button('Consultar Produto', size=(17,1))],
               ]
    return sg.Window('Menu de Opções', jan3, finalize=True, element_justification='center')
def t_menu_user():
    jan4 = [[sg.Button('Novo Cliente')],
               [sg.Button('Consultar Cliente')],
               [sg.Button('Nova Venda')],
               [sg.Button('Consultar Venda')],
               ]
    return sg.Window('Menu de Opções', jan4, finalize=True, element_justification='center')
def t_cadastrar_usuario():
    jan5 = [[sg.Text('Digite o Usuario:')],
               [sg.Input(key='-usuario-', size=(20,1))],
               [sg.Text('Digite a Senha:')],
               [sg.Input(key='-senha-', size=(15,1), password_char='*')],
               [sg.Text('Repita a Senha:')],
               [sg.Input(key='-repsenha-', size=(15,1), password_char='*')],
               [sg.Text('Digite o E-mail')],
               [sg.Input(key='-email-', size=(30,1))],
               [sg.Button('Cadastrar'), sg.Push(), sg.Button('Voltar')],
    ]
    return sg.Window('Cadastrar novo usuario', jan5, finalize=True)
def t_exclusao():
    usuarios = retorna_lista_user_bd()
    jan6 = [[sg.Text('Selecione o usuario a ser excluido:')],
               [sg.Combo(usuarios, size=(20,1), key='del_selecao')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Exclusão de Usuarios', jan6, finalize=True)
def t_cadastro_cliente():
    frame1 = [[sg.Text('Nome: '), sg.Input(key='-nome-', size=(40,1)), sg.Text('CPF:'), sg.Input(key='-cpf-', size=(15,1)), sg.Button('Validar', size=(10,1))],
              [sg.Text('Telefone: '), sg.Input(key='-telefone-', size=(20,1)), sg.Text('E-mail:'), sg.Input(key='-email-', size=(45,1))]]

    frame2 = [[sg.Text('CEP:'),sg.Input(key='-cep-', size=(15,1)), sg.Button('Verificar', size=(10,1))],
              [sg.Text('Endereço: '), sg.Input(key='-endereco-', size=(58,1)), sg.Text('Nº:'), sg.Input(key='-num-', size=(10,1))],
              [sg.Text('Bairro: '), sg.Input(key='-bairro-', size=(25,1)), sg.Text('Cidade:'), sg.Input(key='-cidade-', size=(25,1)),
               sg.Text('Estado:'), sg.Input(key='-estado-', size=(7,1))]]
    jan7 = [[sg.Text('Cadastro de Clientes')],
               [sg.Frame('Cliente', frame1)],
               [sg.Frame('Endereço', frame2)],
               [sg.Button('Cadastrar', size=(10,1)), sg.Button('Voltar', size=(10,1))]]

    return sg.Window('Cadastro de Cliente', jan7, finalize=True)
def t_cadastro_produtos():
    jan8 = [[sg.Text('Produto: '), sg.Input(key='-produto-', size=(30,1)), sg.Text('Marca:'), sg.Input(key='-marca-', size=(20,1))],
               [sg.Text('Unidade:'), sg.Combo(['Unitario', 'Kg', 'Pacote', 'Caixa'], key='-unidade-', size=(15,1)), sg.Text('Valor'), sg.Input(key='-valor-', size=(15,1))],
               [sg.Button('Cadastrar'), sg.Button('Voltar')]]
    return sg.Window('Cadastro de Produtos', jan8, finalize=True)
def t_nova_venda():
    pagamento = ['Dinheiro', 'Cartão de Debito', 'Cartão de Credito', 'Cheque']
    frame1 = [[sg.Table(values=dados, headings=['Produto', 'Marca', 'Valor Unitario', 'Quant.', 'Valor Total'],
                        key='-tabela-', col_widths=[16,16,16,8,12], auto_size_columns=False, justification='left',
                        background_color='gray', text_color='black', enable_events=True)]]

    frame2 = [[sg.Text('Rua:'), sg.Input(size=(40,1), key='-endereco-'), sg.Text('Numero:'),
               sg.Input(size=(8,1), key='-num-'), sg.Text('Cidade:'), sg.Input(size=(25,1), key='-cidade-')]]

    frame3 = [[sg.Text('Forma de Pagto'), sg.Combo(pagamento, key='-pagto-'), sg.Push(),
               sg.Text('Valor Total: R$', font=("Helvetica", 16)),
               sg.Input(key='-valortotal-', size=(10,1), font=("Helvetica", 16))]]

    jan9 = [[sg.Text('Cliente:'), sg.Input('',key='-cliente-', size=(60,1)),sg.Push(), sg.Button('Selecione o Cliente')],
               [sg.Frame('Endereço', frame2, size=(720,50))],
               [sg.Frame('Produtos', frame1), sg.Button('Adicionar')],
               [sg.Frame('Pagamento', frame3, size=(720,60))],
               [sg.Button('Finalizar Venda'), sg.Button('Voltar')]]
    return sg.Window('Nova Venda', jan9, finalize=True)
def t_redefinir_senha():
    jan10 = [[sg.Text('Digite a nova senha: '), sg.Input(key='-novasenha-', size=(20,1), password_char='*')],
                [sg.Text('Repita a nova senha: '), sg.Input(key='-repnovasenha-', size=(20,1), password_char='*')],
                [sg.Button('Redefinir'), sg.Push(), sg.Button('Cancelar')]]

    return sg.Window('Redefinição de Senha', jan10, finalize=True)
def t_consulta_cliente():
    clientes = consulta_clientes_bd()
    jan11 = [[sg.Table(clientes, justification='left', headings=['ID', 'NOME', 'CPF', 'TELEFONE', 'EMAIL', 'CEP', 'ENDERECO', 'NUM', 'BAIRRO', 'CIDADE', 'ESTADO'])],
                [sg.Button('Voltar'), sg.Push(), sg.Button('Excluir')]]

    return sg.Window('Consulta de Clientes', jan11, finalize=True)
def t_consulta_produtos():
    produtos = consulta_produtos_bd()
    jan12 = [[sg.Table(produtos, justification='left', headings=['ID', 'PRODUTO', 'MARCA', 'UNIDADE', 'VALOR'])],
                [sg.Button('Voltar'), sg.Push(), sg.Button('Excluir')]]

    return sg.Window('Consulta de Produtos', jan12, finalize=True)
def t_consulta_vendas():
    vendas = consulta_vendas_bd()
    jan13 = [[sg.Table(vendas, justification='left', headings=['ID', 'DATA', 'CLIENTE', 'RUA', 'NUMERO', 'CIDADE', 'PAGAMENTO', 'VALOR'])],
                [sg.Button('Voltar')]]

    return sg.Window('Consulta de Vendas', jan13, finalize=True)
def t_excluir_produto():
    produtos = retornar_produto_bd()
    jan14 = [[sg.Text('Selecione o produto a ser excluido:')],
               [sg.Combo(produtos, size=(20,1), key='del_selecao_prod')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Exclusão de Produto', jan14, finalize=True)
def t_excluir_cliente():
    clientes = retornar_cliente_bd()
    jan15 = [[sg.Text('Selecione o cliente a ser excluido:')],
               [sg.Combo(clientes, size=(20,1), key='del_selecao_cli')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Exclusão de Cliente', jan15, finalize=True)
def t_cons_cliente():
    clientes = retornar_cliente_bd()
    jan16 = [[sg.Text('Selecione o cliente:')],
               [sg.Combo(clientes, size=(20,1), key='compra_selecao_cli')],
               [sg.Button('Confirmar'), sg.Push(), sg.Button('Voltar')]]
    return sg.Window('Seleção de Cliente', jan16, finalize=True)
def t_adiciona_produto():
    lista = retorna_lista_produto_bd()
    jan17 = [[sg.Text('Selecione o Produto:')],
                [sg.Combo(lista, size=(15,1), key='-selec_prod-'), sg.Spin([1,2,3,4,5,6,7,8,9], initial_value=1, size=(3,1))],
                [sg.Button('Adicionar'), sg.Button('Cancelar')]]

    return sg.Window('Adiciona Produto', jan17, finalize=True)

jan1, jan2, jan3, jan4, jan5, jan6, jan7, jan8, jan9, jan10, \
jan11, jan12, jan13, jan14, jan15, jan16, jan17 = t_login(), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None