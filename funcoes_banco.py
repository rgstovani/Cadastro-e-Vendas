import sqlite3
from hashlib import sha256
import requests

def cria_bd():
    cria_bd_usuarios()
    cria_bd_clientes()
    cria_bd_produtos()
    cria_bd_vendas()

###################### USERS ######################

def cria_bd_usuarios():
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    USER TEXT NOT NULL,
    PASSWORD TEXT NOT NULL,
    EMAIL TEXT NOT NULL);
    ''')
    conn.commit()
    conn.close()
def add_user_bd(usuario, senha, email):
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users VALUES (:USER, :PASSWORD, :EMAIL)
    ''', {"USER": usuario, "PASSWORD": senha,  "EMAIL": email})
    conn.commit()
    conn.close()
def consulta_user_bd(usuario, senha):
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE (USER=? AND PASSWORD=?)
    ''', (usuario, senha))
    teste_login = cursor.fetchone()
    conn.commit()
    conn.close()

    if teste_login is None:
        return False
    if (usuario in teste_login) and (senha in teste_login):
        return True
    else:
        return False
def cadastra_user(usuario, senha, email):
    hashsenha = sha256(senha.encode()).hexdigest()
    add_user_bd(usuario, hashsenha, email)
def teste_login(usuario, senha):
    testesenha = sha256(senha.encode()).hexdigest()
    return (consulta_user_bd(usuario, testesenha))

###################### CLIENTES ######################

def cria_bd_clientes():
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
    NOME TEXT NOT NULL,
    CPF TEXT NOT NULL,
    TELEFONE TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    CEP TEXT NOT NULL,
    ENDERECO TEXT NOT NULL,
    NUM TEXT NOT NULL,
    BAIRRO TEXT NOT NULL,
    CIDADE TEXT NOT NULL,
    ESTADO TEXT NOT NULL);
    ''')
    conn.commit()
    conn.close()
def add_clientes_bd(nome, cpf, telefone, email, cep, endereco, num, bairro, cidade, estado):
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO clientes VALUES (:NOME, :CPF, :TELEFONE, :EMAIL, :CEP, :ENDERECO, :NUM, :BAIRRO, :CIDADE, :ESTADO)
    ''', {"NOME": nome, "CPF": cpf, "TELEFONE": telefone, "EMAIL": email, "CEP": cep, "ENDERECO": endereco, "NUM": num, "BAIRRO": bairro, "CIDADE": cidade, "ESTADO": estado})
    conn.commit()
    conn.close()
def consulta_clientes_bd():
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT oid, * FROM clientes''')
    dados = cursor.fetchall()
    conn.commit()
    conn.close()
    return dados

###################### PRODUTOS ######################

def cria_bd_produtos():
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
    PRODUTO TEXT NOT NULL,
    MARCA TEXT NOT NULL,
    UNIDADE TEXT NOT NULL,
    VALOR TEXT NOT NULL);
    ''')
    conn.commit()
    conn.close()
def add_produtos_bd(produto, marca, unidade, valor):
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO produtos VALUES (:PRODUTO, :MARCA, :UNIDADE, :VALOR)
    ''', {"PRODUTO": produto, "MARCA": marca, "UNIDADE": unidade, "VALOR": valor})
    conn.commit()
    conn.close()
def consulta_produtos_bd():
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT oid, * FROM produtos''')
    dados = cursor.fetchall()
    conn.commit()
    conn.close()
    return dados

###################### VENDAS ######################

def cria_bd_vendas():
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
    PRODUTO TEXT NOT NULL,
    MARCA TEXT NOT NULL,
    UNIDADE TEXT NOT NULL,
    VALOR TEXT NOT NULL);
    ''')
    conn.commit()
    conn.close()
def add_vendas_bd(produto, marca, unidade, valor):
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO vendas VALUES (:PRODUTO, :MARCA, :UNIDADE, :VALOR)
    ''', {"PRODUTO": produto, "MARCA": marca, "UNIDADE": unidade, "VALOR": valor})
    conn.commit()
    conn.close()
def consulta_vendas_bd():
    conn = sqlite3.connect('App_Dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT oid, * FROM vendas''')
    dados = cursor.fetchall()
    conn.commit()
    conn.close()
    return dados

###################### FUNÇÕES GERAIS ######################

def validador_cpf(cpf):
    invalido = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666',
                '77777777777', '88888888888', '99999999999']
    ### Verifica o Input
    while True:
        # cpf = str(valores['entrada_cpf'])
        if cpf.isnumeric():
            if len(cpf) != 11 or cpf in invalido:
                return False
            else:
                 break
        else:
            return False

    ### Validação do primeiro Digito
    digito1 = int(cpf[9:10])
    verificador1 = 0
    for i, v1 in zip(range(1, 10), range(10, 1, -1)):
        verificador1 += int(cpf[i - 1:i]) * v1
    v1 = (11 - (verificador1 % 11))
    if (v1 == 10) or (v1 == 11):
        v1 = 0
    else:
        pass

    ### Validação do segundo Digito
    digito2 = int(cpf[10:])
    verificador2 = 0
    for i, v2 in zip(range(1, 11), range(11, 1, -1)):
        verificador2 += int(cpf[i - 1:i]) * v2
    v2 = (11 - (verificador2 % 11))
    if (v2 == 10) or (v2 == 11):
        v2 = 0
    else:
        pass

    ### Verifica validade CPF
    if v1 == digito1:
        if v2 == digito2:
            return True
        else:
            return False
    else:
        return False
def consulta_cep(cep):
    link = (f'http://viacep.com.br/ws/{cep}/json/')
    resposta = requests.get(link)
    end = resposta.json()
    cep = end['cep']
    logradouro = end['logradouro']
    bairro = end['bairro']
    localidade = end['localidade']
    uf = end['uf']
    return cep, logradouro, bairro, localidade, uf
