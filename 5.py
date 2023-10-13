class Conta:
  def __init__(self, numero, nome, saldo=0):
    self.numero = numero
    self.nome = nome
    self.saldo = saldo
  
  def altera_nome(self, nnome):
    self.nome = nnome
  
  def deposito(self, valor):
    self.saldo += valor
  
  def saque(self, valor):
    if self.saldo < valor:
      print("voce nao tem saldo suficiente ")
    else:
      self.saldo -= valor
    