import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE pessoa (nome TEXTO, email TEXTO, telefone TEXTO, data_nasc TEXTO)')
conn.close()