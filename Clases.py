import os
os.system('clear')



class Jugador1:
   def __init__(self, nombre,apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
   def portugal(self):
       print(f"{self.nombre} {self.apellido} es portugués")
jugador1 = Jugador1("Cristiano","Ronaldo")
print(jugador1.nombre , jugador1.apellido , "es el jugador 1")
jugador1.portugal()
   
       
class Jugador2:
    def __init__(self, nombre,apellido)-> None:
      self.nombre_apellido = f"{nombre} {apellido}"
    def argentina(self):
      print(f"{self.nombre_apellido} es argentino")
    def francia(self):
      print(f"{self.nombre_apellido} es francés") 
    
jugador2 = Jugador2("Lionel", "Messi")
print(jugador2.nombre_apellido , "es el jugador 2")
jugador2.argentina()
jugador3 = Jugador2("Karim" , "Benzemá")
print(jugador3.nombre_apellido , "es el jugador 3")
jugador3.francia()

