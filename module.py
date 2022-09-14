import pymongo
from bson.objectid import ObjectId


class Produto:
    # variaveis para conexão com o banco, preencher com as suas:
    host = 'localhost'
    port = 27017
    nome_banco = 'teste-database'
    nome_colecao = 'produtos'

    client = pymongo.MongoClient(host, port)
    db = client[nome_banco]
    col = db[nome_colecao]

    propriedades_banco = ['nome', 'imagem', 'preco', 'descricao', 'marca']

    def __init__(self):
        self._nome = ''
        self._preco = 0.00
        self._descricao = ''
        self._imagem = ''
        self._marca = ''

    # "Getters"
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def descricao(self):
        return self._descricao

    @property
    def imagem(self):
        return self._imagem

    @property
    def marca(self):
        return self._marca

    # "Setters"
    @nome.setter
    def nome(self, value):
        if len(value) <= 2:
            print("Insira um valor Válido!")
        self._nome = value

    @preco.setter
    def preco(self, value):
        if value < 0.01:
            print("Valor Inválido!")

        self._preco = value

    @descricao.setter
    def descricao(self, value):
        if len(value) <= 2:
            print("Insira um valor Válido!")
        self._descricao = value

    @imagem.setter
    def imagem(self, value):
        self._imagem = value

    @marca.setter
    def marca(self, value):
        self._marca = value

    # metodo para listar as informações
    def listar_info(self):
        print(f'Nome: {self.nome}\n'
              f'Preco: {self.preco}\n'
              f'Descrição: {self.descricao}\n'
              f'Image: {self.imagem}\n'
              f'Marca: {self.marca}')

    # Métodos de CRUD

    # adicionar no banco
    def inserir_banco(self):
        dados = {
            "nome": self.nome,
            "descricao": self.descricao,
            "imagem": self.imagem,
            "preco": self.preco,
            "marca": self.marca}
        x = self.col.insert_one(dados).inserted_id
        print(f'Id: {x}')

    # nessas funções são necessários adicionar o valor do "id" do dado desejado

    def buscar_banco(self, valor):
        # função para buscar o dado no banco, através do ID
        # valor = "id" do documento no banco
        print(self.col.find_one({'_id': ObjectId(valor)}))

    def atualizar_banco(self, valor, nome_campo, novo_valor):
        # função para atualizar determinado dado no banco de dados através do ID
        # nome do campo é o campo desejado (nome, descricao, imagem ou preco)
        # o valor é o novo valor a ser passado para o banco
        # o parametro valo corresponde "id" do documento no banco
        if nome_campo not in self.propriedades_banco:
            print('Operação Inválida pois o nome da propriedade não existe')

        self.col.update_one({'_id': ObjectId(valor)}, {'$set': {nome_campo: novo_valor}})

    def deletar_banco(self, valor):
        # valor = "id" do documento no banco
        # função para deletar determinado documento no banco através do ID
        self.col.delete_one({'_id': ObjectId(valor)})

    # função para listar tudo
    def listar_all(self):
        documentos = self.col.find()
        lista_documentos = []
        for x in documentos:
            lista_documentos.append(x)
            print(x)
