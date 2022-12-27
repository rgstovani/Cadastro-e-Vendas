import sqlite3
from hashlib import sha256

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

