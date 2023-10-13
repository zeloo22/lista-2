class Bola:
  def __init__(self,cor, circunfer, material):
    self.cor = cor
    self.circunfer = circunfer
    self.material = material
  def mostra_cor(self):
    print(f"a cor da bola e: {self.cor}")
  def troca_cor(self,ncor):
    self.cor = ncor
   
   
tenis = Bola("verde", 10, "nylon")
tenis.mostra_cor()
x = input("fale a cor q deseja trocar: ")
tenis.troca_cor(x)
tenis.mostra_cor()