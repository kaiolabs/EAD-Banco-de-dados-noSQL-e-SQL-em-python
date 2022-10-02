from pymongo import MongoClient

#Inicializa o cliente do MongoDB
client = MongoClient('localhost', 27017)

#Criando o banco de dados
db = client['EAD']

#Criando a coleção
collection = db['alunos']

#Inserindo um documento se o nome já existir, dara uma mensagem de erro e não irá inserir
def insert_document(name, surname, age, course):
   # verifica se o nome já existe
    if collection.find_one({'nome': name}):
        print(f'Aluno {name} já cadastrado') 
    else:
        #Insere o documento
        collection.insert_one({'nome': name, 'sobrenome': surname, 'idade': age, 'curso': course})
        print(f'Documentos do aluno {name} inserido com sucesso')


# insert_document('Kaio', 'Vinicius', 19, 'Engenharia da computação')
# insert_document('Lucas', 'alves', 19, 'Ciência da computação')
# insert_document('Julia', 'Silva', 19, 'Administração')
# insert_document('Maria', 'tedesco', 19, 'Letras')

