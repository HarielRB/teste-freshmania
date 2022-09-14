from flask import Flask
import pymongo
from bson.objectid import ObjectId


app = Flask(__name__)

host = 'localhost'
port = 27017
nome_banco = 'teste-database'
nome_colecao = 'produtos'


@app.route('/')
def inicial():
    return '<h1>Eu sou uma API em FLask</h1>' \
            f'<a href="/listar">Visualizar API em formato JSON</a>' \
           f'<p>A url para <b>excluir</b> deve ser passada com o Id do documento a ser excluido no banco</p>' \
           f'<h4>Atenção para realizar a exclusão do valor</h4>'


@app.route('/listar', methods=['GET'])
def listar():
    client = pymongo.MongoClient(host, port)
    db = client[nome_banco]
    mycol = db[nome_colecao]
    lista_do_banco = mycol.find()
    base_dados = []
    for i in lista_do_banco:
        i['_id'] = str(i['_id'])
        base_dados.append(i)

    return {'produtos': base_dados}


@app.route('/excluir/<valor>', methods=['DELETE'])
def excluir(valor):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['teste-database']
    mycol = db['produtos']
    mycol.delete_one({'_id': ObjectId(valor)})
    return f'<p>Produto {valor} excluido do banco</p>' \
           f'<a href =/listar >Voltar para listagem</a>'


'''@app.route('/criar')
def criar():
    produto = Produto()
    produto.nome = 'Abacate'
    produto.imagem = 'Url de imagem'
    produto.preco = 8.95
    produto.descricao = 'Lorem Ipsum'
    produto.inserir_banco()

    return f'<p>Produto {produto.nome} cadastrado com Sucesso!</p>'
'''

if __name__ == '__main__':
    app.run(debug=True)
