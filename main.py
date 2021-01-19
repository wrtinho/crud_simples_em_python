from Estoque import *
from Funcionario import *
from menu import menu
from Pessoa import *
from Produto import *

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from sign_up import Sign_Up
from login import Login
from home import Home
from comprar import Comprar
from vender import Vender




estoque = Estoque()

clientes = [
  Usuario("Joao", "1"), 
]

funcionarios = [
  Funcionario("Ricardo","Vendendor", "1"), 
]

def is_funcionario(pessoa):
  return isinstance(pessoa, Funcionario)

def is_cliente(pessoa):
  return (isinstance(pessoa, Usuario) and not(is_funcionario(pessoa)))

def cadastro_usuario(nome,ocupacao,cpf,senha):
    user=Usuario(nome,cpf)
    clientes.append(user)
    return user
 

  
def cadastro_funcionario(nome,ocupacao,cpf,senha):
  user=Funcionario(nome,ocupacao,cpf)
  funcionarios.append(user)
  return user


def id_existe(Id,lista):
  for i in lista:
    if (i.id == Id):
      return i
  return False

def mostra_login(user):
  if is_funcionario(user):
    return f'Logado como funcionario: {user.nome}'

  if is_cliente(user): 
    return f'Logado como Cliente: {user.nome}'
  else:
    return 'Voce não esta logado'



class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow() 
        self.stack1 = QtWidgets.QMainWindow() 
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow() 
        self.stack4 = QtWidgets.QMainWindow() 

        self.tela_home = Home()
        self.tela_home.setupUi(self.stack0)
        
        self.tela_cadastro = Sign_Up()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_login = Login()
        self.tela_login.setupUi(self.stack2)

        self.tela_compra = Comprar()
        self.tela_compra.setupUi(self.stack3)

        self.tela_vender = Vender()
        self.tela_vender.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)



logado="Não logado"
def logadocom():
  return logado

def setlogado(value):
  global logado
  logado = value
class Main(QMainWindow,Ui_Main):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        
        #TELA HOME
        self.tela_home.pushButton_2.clicked.connect(self.abrirTelaCadastro)
        self.tela_home.pushButton_5.clicked.connect(self.botaoVoltar)

        self.tela_home.pushButton_3.clicked.connect(self.abrirTelaCompra)
        self.tela_home.pushButton_4.clicked.connect(self.abrirTelaVenda)

        self.tela_home.label_2.setText(logadocom())

        
       
       
        #TELA LOGIN
        self.tela_login.pushButton_8.clicked.connect(self.botaoLogar)
        self.tela_login.pushButton_5.clicked.connect(self.botaoVoltar)
        self.tela_login.label_9.setText(logadocom())

       

        #TELA CADASTRO
        self.tela_cadastro.pushButton.clicked.connect(self.abrirTelaLogin)
        self.tela_cadastro.pushButton_8.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.pushButton_5.clicked.connect(self.botaoVoltar)
        self.tela_cadastro.label_9.setText(logadocom())


        #COMPRAR
        estoque.AttLista()
        self.tela_compra.comboBox.addItems(estoque.allprodutos())
        self.tela_compra.pushButton_8.clicked.connect(self.botaoCompra)
        self.tela_compra.pushButton_5.clicked.connect(self.botaoVoltar)

        #VENDER
        estoque.AttLista()
        self.tela_vender.comboBox.addItems(estoque.allprodutos())
        self.tela_vender.pushButton_8.clicked.connect(self.botaoVender)
        self.tela_vender.pushButton_5.clicked.connect(self.botaoVoltar)
        

            
#TELA HOME



    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(2)

    def botaoCadastra(self):
        nome =      self.tela_cadastro.lineEdit_8.text()
        ocupacao =  self.tela_cadastro.lineEdit_6.text()
        cpf =       self.tela_cadastro.lineEdit_5.text()
        senha =     self.tela_cadastro.lineEdit_7.text()
        if not(self.tela_cadastro.radioButton.isChecked() and self.tela_cadastro.radioButton_2.isChecked()):
          QMessageBox.information(None,'POOII','Voce deve escolher entre Cliente ou Funcionario')

        if (self.tela_cadastro.radioButton.isChecked()):
          if not(nome == '' or ocupacao == '' or cpf == '' or senha == ''):
              cadastro_usuario(nome,ocupacao,cpf,senha)
              QMessageBox.information(None,'StorageControl','Cadastro realizado')
              self.QtStack.setCurrentIndex(2)
              self.tela_cadastro.lineEdit_5.setText('')
              self.tela_cadastro.lineEdit_6.setText('')
              self.tela_cadastro.lineEdit_7.setText('')
              self.tela_cadastro.lineEdit_8.setText('')
          else:
              QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos')
  

        if (self.tela_cadastro.radioButton_2.isChecked()):
          if not(nome == '' or ocupacao == '' or cpf == '' or senha == ''):
              cadastro_funcionario(nome,ocupacao,cpf,senha)
              QMessageBox.information(None,'StorageControl','Cadastro realizado')
              self.QtStack.setCurrentIndex(2)
              self.tela_cadastro.lineEdit_5.setText('')
              self.tela_cadastro.lineEdit_6.setText('')
              self.tela_cadastro.lineEdit_7.setText('')
              self.tela_cadastro.lineEdit_8.setText('')
          else:
            QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos')              
  
    def botaoLogar(self):
      nome =      self.tela_login.lineEdit_8.text()
      cpf =       self.tela_login.lineEdit_5.text()
      senha =     self.tela_login.lineEdit_7.text()
        
      
      if (self.tela_login.radioButton.isChecked()):
        user=id_existe(cpf, clientes)
        if(is_cliente(user)):
          self.tela_login.lineEdit_5.setText('')
          self.tela_login.lineEdit_7.setText('')
          self.tela_login.lineEdit_8.setText('')

          setlogado(user.nome)
          self.tela_login.label_9.setText('Olá '+logadocom())
          QMessageBox.information(None,'POOII',f'Bem vindo {user.nome}')
          self.QtStack.setCurrentIndex(0)
          self.tela_home.label_2.setText('Olá '+user.nome)

        else:
            QMessageBox.information(None,'POOII','CPF não encontrado')
        
      if (self.tela_login.radioButton_2.isChecked()):
        user=id_existe(cpf, funcionarios)
        if(is_funcionario(user)):
          setlogado(user.nome)
          self.tela_login.label_9.setText('Olá '+logadocom())
          QMessageBox.information(None,'POOII',f'Bem vindo {user.nome}')
          self.QtStack.setCurrentIndex(0)
          self.tela_home.label_2.setText('Olá '+user.nome)

        else:
            QMessageBox.information(None,'POOII','CPF não encontrado')

      # if not(self.tela_cadastro.radioButton.isChecked() and self.tela_cadastro.radioButton_2.isChecked()):
      else:
          QMessageBox.information(None,'POOII','Voce deve escolher entre Cliente ou Funcionario')

    def botaoVoltar(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCompra(self):
      if self.tela_home.label_2.text() == "Não logado":
        QMessageBox.information(None,'POOII','Voce precisa logar para completar essa etapa')
      else:
        self.QtStack.setCurrentIndex(3)

    def abrirTelaVenda(self):
      if self.tela_home.label_2.text() == "Não logado":
        QMessageBox.information(None,'POOII','Voce precisa logar para completar essa etapa')
      else:
        self.QtStack.setCurrentIndex(4)
    
    def botaoCompra(self):
      self.tela_compra.label_9.setText(logadocom())
      produto=self.tela_compra.comboBox.currentText()
      quantidade = self.tela_compra.lineEdit_5.text()
      produto = estoque.buscarProduto(produto)
      if (produto):
        print(produto,quantidade)
        if venda_produtos(produto,quantidade):
          estoque.AttLista()
          QMessageBox.information(None,'POOII',f'Operação concluida,  quantidade restante {estoque.qtd(produto)}')
        else:
          QMessageBox.information(None,'POOII',f'Quantidade maior que Disponivel total {estoque.qtd(produto)}')
      else:
        QMessageBox.information(None,'POOII','Foi vendido todo estoque desse produto')
      self.QtStack.setCurrentIndex(0)
      
    def botaoVender(self):
      self.tela_vender.label_9.setText(logadocom())
      produto=self.tela_vender.comboBox.currentText()
      quantidade = self.tela_vender.lineEdit_5.text()
      produto = estoque.buscarProduto(produto)
      if (produto):
        print(produto,quantidade)
        if venda_produtos(produto,quantidade):
          estoque.AttLista()
          QMessageBox.information(None,'POOII',f'Operação concluida,  quantidade restante {estoque.qtd(produto)}')
        else:
          QMessageBox.information(None,'POOII',f'Quantidade maior que Disponivel total {estoque.qtd(produto)}')
      else:
        QMessageBox.information(None,'POOII','Foi comprado todo estoque desse produto')
      self.QtStack.setCurrentIndex(0)




app = QApplication(sys.argv)
show_main = Main()
sys.exit(app.exec_())



def main(logado=False):
  home_menu,menu_escolha_user,menu_entrar_cliente,menu_entrar_Funcionario,compra_step1,venda_step1,compra_venda_step2 = menu()



  logado=logado

  print("_______________________________________________________________________________ \n", mostra_login(logado))
  escolha=input(home_menu)

  #thead_escolha_1
  if(escolha == '1'):
    
    #escolha se é cliente ou Funcionario 1,2
    escolha=input(menu_escolha_user)

    #login_Cliente
    if(escolha == '1'):
        escolha=input(menu_entrar_cliente).split(',')

        #login
        # if (len(escolha) == 1):
        #     # user=id_existe(escolha[0], clientes)
        #     # if(is_cliente(user)):
        #       logado = user
        #       print("Logado com Sucesso")
        #     else:
        #        print("ID not Found")

        #cadastro
        if (len(escolha) == 2): 
          user=cadastro_usuario(escolha[0],escolha[1])
          logado = user
          print("Cadastro com Sucesso")
        else:
          print("voce escolheu sair")
        
        main(logado)

    #login_funcionario
    if(escolha == '2'):
      escolha=input(menu_entrar_Funcionario).split(',')
     

      if(len(escolha) == 2):
        user=id_existe(escolha[1], funcionarios)
        if(is_funcionario(user)):
          logado = user
          print("Logado com Sucesso")
        else:
            print("ID not Found")

      if(len(escolha) == 3):
        user=cadastro_funcionario(escolha[0],escolha[2],escolha[1])
        logado = user
        print("Cadastro com Sucesso")
      else:
        print("voce escolheu sair")
     
      main(logado)

    if(escolha == '3'):
      main()
    else:
      exit()
  if(escolha == '2'):

    #saber se existe produto
    if(Produtos.flag):
      estoque.listarProdutos()
      #saber se é cliente
      if is_cliente(logado):
        escolha=input(compra_step1)
        user = id_existe(escolha,funcionarios)
        if(user and escolha != 0):
          nome_prod=input("Infome o nome do produto: ")
          produto = estoque.produtoExiste(nome_prod)
          if produto:
            vendido = venda_produtos(produto)
            if vendido:
              print("Compra realizada com sucesso")
            else:
              print("Falha ao realizar a compra")
          else:
            print("Não existe esse produto no estoque")

      elif is_funcionario(logado):
        escolha=input(venda_step1)
        #recebe id
        user = id_existe(escolha,clientes)
        if(user and escolha != 0):
          nome_prod=input("Infome o nome do produto: ")
          produto = estoque.produtoExiste(nome_prod)
          if produto:
            vendido = venda_produtos(produto)
            if vendido:
              print("Venda realizada com sucesso")
            else:
              print("Falha ao realizar a venda")
          else:
            print("Não existe esse produto no estoque")
        
      main(logado)
    else:
      print("Não ha produtos cadastrados, é recomendado ir para Administração")
      main(logado)

  if(escolha == '3'):
  
    print("Bem vindo aos primeiros passos \n Primeiramente é preciso cadastrar um Funcionario \n")


    #cadastro do Funcionario
    escolha=input("""  Para efetuar cadastro insira seu nome, sua ocupação e seu identificador unico - ID (separando-os por virgula ',')
                        ex: Wellington,developer,123 \n""").split(',')
    user=cadastro_funcionario(escolha[0],escolha[2],escolha[1])
    logado = user
    print("\n Cadastro do Funcionario realizado com sucesso, agora iremos cadastrar um produto ")
    nomeProd = input("Digite o nome do produto: ")
    qtdProd = int(input("Digite a quantidade em estoque: "))


    #cadastro de Produtos
    cadastrado = estoque.cadastrarProduto(nomeProd, qtdProd)
    if cadastrado:
      print('Produto cadastrado com sucesso!')
    else:
      print('Ocorreu um erro ao cadastrar o produto, verifique se o produto ja não esta cadastrado')
    print("Muito bem agora só falta o cadastro do cliente")


    #cadastro de Clientes
    escolha=input("""\n  Para efetuar cadastro insira seu nome, sua ocupação e seu identificador unico (separando-os por virgula ',')
                        ex: Wellington,123 \n""").split(',')
    user=cadastro_usuario(escolha[0],escolha[1])
    logado = user
  
    print("Cadastro do Cliente realizado com sucesso, agora ja podemos entrar no sistema")
 
    main(logado)

  if(escolha == '4'):
    print("Area adm")
    if is_funcionario(logado):
      produto_menu = input("""Digite
      1 - Cadastrar
      2 - Buscar
      3 - Alterar
      4 - Excluir
      5 - Listar Produtos
      6 - Voltar
      0 - Sair
      """)
      if produto_menu == '1':
        nomeProd = input("Digite o nome do produto: ")
        qtdProd = int(input("Digite a quantidade em estoque: "))

        cadastrado = estoque.cadastrarProduto(nomeProd, qtdProd)
        if cadastrado:
          print('Produto cadastrado com sucesso!')
        else:
          print('Ocorreu um erro ao cadastrar o produto, verifique se o produto ja não esta cadastrado')
          
      elif produto_menu == '2':
        nome = input('Digite o nome do produto: ')
        produto = estoque.buscarProduto(nome)
        if produto: 
          print("Nome: ", produto.nome)
          print("Quantidade: ", produto.quantidade)
        else:
          print('Não possivel encontrar esse produto!')

      elif produto_menu == '3':
        nome = input('Digite o nome do produto: ')
        produto = estoque.buscarProduto(nome)
        if produto:
          produto.quantidade = int(input('Dige a nova quantidade em estoque: '))
          print('As alterações foram salvas com sucesso!')
        else:
          print('Não possivel encontrar esse produto!')

      elif produto_menu == '4':
        nome = input('Digite o nome do produto: ')
        produto = estoque.buscarProduto(nome)
        if produto:
          estoque.exluirProduto(produto)
          print('O produto foi excluido com sucesso!')
          # Produtos.flag=False
        else:
          print('Não possivel encontrar esse produto!')
      elif produto_menu == '5':
        estoque.listarProdutos()
      elif produto_menu == '0':
        exit()
    else:
      print("Voce não tem autorização para entrar aqui, Logue novamente como Funcionario")

    main(logado)
    #confere se logar é instancia de funcionario: se sim
    #CRUD de produtos

        
main()




# if estoque.produtoExiste(nome_prod):
  # 
            # qtd=int(input(compra_venda_step2))
          # produto = estoque.tem_qtd_disponivel(nome_prod,qtd)
          # if(produto):
            # venda_produtos(produto,qtd)
          # else:
            # print("Quantidade maior do que cadastrada")