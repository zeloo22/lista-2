class Televisao:
  def __init__(self, volume=10, canal):
    self.volume = volume
    self.canal = canal
    
  def informa_canal(self, ncanal):
    self.canal = ncanal 
    
  def aumenta_volume(self):
    self.volume += 10
    
  def diminui_volume(self):
    self.volume -= 10