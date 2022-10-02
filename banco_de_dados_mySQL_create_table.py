import sqlite3

# Criando uma conexão
conn = sqlite3.connect('EAD.db')

# Criando um cursor
c = conn.cursor()

# Criando uma tabela
c.execute('''CREATE TABLE alunos(nome text, sobrenome text, idade integer, curso text)''')

# Inserindo um registro
c.execute("INSERT INTO alunos VALUES ('Kaio', 'Vinicius', 19, 'Engenharia da computação')")

# Salvando as alterações    
conn.commit()
