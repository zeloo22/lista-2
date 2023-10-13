class Retangulo:
  def __init__(self, comprimento, largura):
    self.comprimento = comprimento
    self.largura = largura
    
    
  def trocar_valores(self, ncompri, nlarg):
    self.comprimento = ncompri
    self.comprimento = nlarg
   
  def calc_area(self):
    area = self.comprimento * self.largura
    return area
   
  def calc_perimetro(self):
    perime = self.comprimento*2 + self.largura*2
    return perime
  
  def retorna_lados(self):
    print(f"comprimento: {self.comprimento}")
    print(f"largura: {self.largura}")
  