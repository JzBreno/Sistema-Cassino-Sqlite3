import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent
import sql3

con = sqlite3.connect(ROOT_PATH / 'MeuBanco.db')
cur = con.cursor()


def InserirJogador():
    try:
        nome = input('Insira o Nome do Jogador: ').upper()
        email = input('Insira o Email do Jogador: ').upper()
        cpf = input('Insira o CPF do jogador(apenas numeros): ').upper()
        pontuacao = 0
    except Exception as e:
        print(f"Current error: {e}")
    
    sql3.InsertRegister(cur, con, (nome, email, cpf, pontuacao))

def MostrarClientes():
    clientes = sql3.List_Clients(cur)
    j = 0
    for i in clientes:
        print(f'Nome do Jogador: {clientes[j][1]} | Pontos: {clientes[j][4]}')
        j+=1

def AtualizarPontos():
    id, nome, email, cpf, point = LocalizarCliente2()

    try:
        newpoint = int(input('Digite a pontuacao: '))
    except Exception as e:
        print(f"Current error: {e}")

    point += newpoint
    data = (nome, email, cpf, point, id)

    sql3.Updateregister(cur, con, data)

def LocalizarCliente():
    try:
        id = int(input('Insira o Id que deseja Atualizar: '))
    except Exception as e:
        print(f"Current error: {e}")
    cliente = dict(sql3.Search_Client(cur,(id,)))
    print('Cliente localizado!')
    print(f"Nome do Jogador: {cliente['nome']} | Pontos: {cliente['points']}")

def LocalizarCliente2():
    id = int(input('Insira o Id que deseja Atualizar a pontuacao: '))
    cliente = dict(sql3.Search_Client(cur,(id,)))
    return cliente['id'],cliente['nome'], cliente['email'],cliente['cpf'], cliente['points']

def DeletarCliente():
    try:
        id = int(input('Digite o Id do cliente que deseja Deletar: '))
        data = (id, )
    except Exception as e:
        print(f"Current error: {e}")
    
    sql3.Deleteregister(cur, con, data)

