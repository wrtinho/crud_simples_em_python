from Produto import Produtos

class Estoque: 
  def __init__(self):
    self.__produtos = [
      Produtos("teste", 20),
    ]
  
  def allprodutos(self):
    all=[]
    for i in self.__produtos:
      all.append(i.nome)
    return all

  def allprodutos_com_quantidade(self):
    all=[]
    for i in self.__produtos:
      all.append(f" Produto: {i.nome} \t Quantidade: {i.quantidade}")
    return all


  def cadastrarProduto(self,nome, quantidade):
    produtoExiste = False
    for i in self.__produtos:
      if i.nome == nome:
        return False

    if not produtoExiste:
      produto = Produtos(nome, quantidade)
      self.__produtos.append(produto)
      return True

  def listarProdutos(self):
    # print("_______________________________________________________________________________")
    # print("Listagem de Produtos")
    # print("_______________________________________________________________________________")
    for i in self.__produtos:
      print("Nome:", i.nome)
      # print("Quantidade:", i.quantidade)
      # print("_______________________________________________________________________________")

  def buscarProduto(self, nome):
    for i in self.__produtos:
      if i.nome == nome:
        return i
    return False

  def exluirProduto(self, produto: Produtos):
    if isinstance(produto, Produtos):
      self.__produtos.remove(produto)
      return True
    else:
      return False

  def produtoExiste(self, nome):
    for i in self.__produtos:
      if i.nome == nome:
        return i

    return False

  def tem_qtd_disponivel(self, nome, quantidade):
    produto = self.produtoExiste(nome)
    if produto:
      if(produto.quantidade - quantidade >= 0):
        return True
    return False

  def qtd(self,produto):
    return produto.quantidade

  def AttLista(self):
    for i in self.__produtos:
      if i.quantidade == 0:
        self.__produtos.remove(i)
