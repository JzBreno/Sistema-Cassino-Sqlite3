import sqlite3 
from pathlib import Path
ROOT_PATH = Path(__file__).parent


def Createtable(con):
    con.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150), cpf VARCHAR(11), points INT(1000))")

def InsertRegister(cur, con, data):
    try:
        cur.execute("INSERT INTO clientes ( nome, email,cpf, points) VALUES (?,?,?,?);", (data))
        #data eh uma tupla na ordem de entrada
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def Updateregister(cur, con, data):
    
    try:
        cur.execute("UPDATE clientes SET nome = ?, email = ?, cpf = ?, points = ? WHERE id = ?", data)
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def Deleteregister(cur, con, data):
    try:
        cur.execute("DELETE FROM clientes WHERE id = ?", data)
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def InsertMany(cur, con, data):
    try:
        cur.executemany('INSERT INTO clientes (nome, email, cfp, points) VALUES (?,?,?,?)', data)
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def Search_Client(cur, data):
    cur.row_factory = sqlite3.Row
    try:
        cur.execute("SELECT * FROM clientes WHERE id=?", (data))
        return cur.fetchone()
    except Exception as e:
        print(f"Current error: {e}")

def List_Clients(cur):
    try:
        cur.execute("SELECT * FROM clientes")
        return cur.fetchall()
    except Exception as e:
        print(f"Current error: {e}")



