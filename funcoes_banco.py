import sqlite3
from hashlib import sha256

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
