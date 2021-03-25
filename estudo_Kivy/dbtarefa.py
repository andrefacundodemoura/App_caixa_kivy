import sqlite3


def create_table():
    connectionall = sqlite3.connect('App_caixa.db')
    c_all = connectionall.cursor()
    c_all.execute('CREATE TABLE IF NOT EXISTS tarefas(Tarefa text)')
    connectionall.commit()


def insert_tarefas(tarefa):
    connectionall = sqlite3.connect('App_caixa.db')
    c_all = connectionall.cursor()
    c_all.execute(f'INSERT INTO tarefas (Tarefa) VALUES ("{tarefa}")')
    connectionall.commit()



