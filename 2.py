class Quadrado:
  #construtor
  def __init__(self,lado):
    self.lado = lado
    
 #metodos
  def retorna_lado(self):
    print(self.lado)
  def troca_lado(self,nlado):
    self.lado = nlado
  def area(self):
    area = self.lado**2
    return area


dadin = Quadrado(20)
dadin.retorna_lado()
print(f"a area vai ser: {dadin.area()}")
x = input("fale o novo tamanho do lado: ")
dadin.troca_lado(x)
dadin.retorna_lado()