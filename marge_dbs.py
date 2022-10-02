import sqlite3

from pymongo import MongoClient

from banco_de_dados_mySQL_insert_table import insert_document

# Crie uma função que sincronize um banco de dados relacional com um não-relacional, ou vice-versa.

# Inicializa os clientes do MongoDB e do SQLite
client = MongoClient('localhost', 27017)
conn = sqlite3.connect('EAD.db')


# Checa se o banco de dados EAD tem novos dados para serem inseridos no MongoDB
def check_new_data_sqlite():
    # Cria um cursor para o banco de dados EAD.db
    c = conn.cursor()
    # Seleciona todos os dados da tabela alunos
    c.execute("SELECT * FROM alunos")
    # Pega todos os dados da tabela alunos
    data = c.fetchall()
    # Fecha a conexão
    conn.close()
    # Retorna os dados
    return data

# Checa se há novos dados no MongoDB
def check_new_data_mongo():
    # Cria o banco de dados EAD
    db = client['EAD']
    # Cria a coleção alunos
    collection = db['alunos']
    # Pega todos os dados da coleção alunos
    data = collection.find()
    # Retorna uma lista com os dados da coleção alunos
    return list(data)
    

# função que sincroniza os dados do banco de dados relacional com o não-relacional
def sync_data():
    # Pega os dados do banco de dados relacional
    data = check_new_data_sqlite()
    collection = check_new_data_mongo()
    
    # Percorre os dados do banco de dados não-relacional e verifica se o nome já existe no banco de dados relacional
    for i in collection:
        for j in data:
            # se nome já existir, não insere
            if i['nome'] == j[0] and i['sobrenome']:
                print(f'Aluno {i["nome"]} já cadastrado')
                break
        # se nome não existir, insere
        else:
            insert_document(i['nome'], i['sobrenome'], i['idade'], i['curso'])
          
   

sync_data() # chama a função que sincroniza os bancos de dados relacional e não-relacional
