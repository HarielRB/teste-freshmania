from module import Produto


p1 = Produto()

p1.nome = "Queijo Minas"
p1.descricao = "Lorem Ipsum"
p1.preco = 15.99
p1.imagem = 'URL_de_Imagem'
p1.marca = 'Aviacao'
p1.listar_info()
#p1.inserir_banco()
p1.buscar_banco('632127a85bc845a057c62d65')
p1.listar_all()
