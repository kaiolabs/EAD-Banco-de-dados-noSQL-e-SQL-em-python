import sqlite3

# Criando uma conexão
conn = sqlite3.connect('EAD.db')

# Criando um cursor
c = conn.cursor()

#Inserindo um documento se o nome já existir, dara uma mensagem de erro e não irá inserir
def insert_document(name, surname, age, course):
    # verifica se o nome já existe
    c.execute("SELECT * FROM alunos WHERE nome = ?", (name,))
    data = c.fetchall()
    if data:    
        print(f'Aluno {name} já cadastrado')
    else:   
        #Insere o documento
        c.execute("INSERT INTO alunos VALUES (?, ?, ?, ?)", (name, surname, age, course))
        #Salvando as alterações    
        conn.commit()
        print(f'Documentos do aluno {name} inserido com sucesso')

    # Salvando as alterações    
    conn.commit()

# insert_document('Kaio0', 'Vinicius', 19, 'Engenharia da computação')
