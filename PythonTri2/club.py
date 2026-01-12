class Equipo :
   def __init__(self, nom_eq):
      self.nombre_equipo = nom_eq
      self.jugadores_eq = []
   def anyadir_jugador(self, jugador) :
      self.jugadores_eq.append(jugador)


class Jugador :
   # constructor
    def __init__(self, dor, nom) :
      self.dorsal = dor
      self.nombre = nom
      self.equipo = None

    def anyadir_equipo(self, equipo):
       self.equipo = equipo
       equipo.anyadir_jugador(self)


    def mostrar(self) :
      print(f'{self.dorsal}.{self.nombre}') 


#programa principal
equipo1 = Equipo("Barcelona")
equipo2 = Equipo("Real Madrid")

jugador1 = Jugador (11, "Raphinha") 
jugador2 = Jugador (6, "Vinicius") 
Jugador3 = Jugador (25, "Mijatovic")
Jugador4 = Jugador (25, "Marcelo")


jugador1.anyadir_equipo(equipo1)
jugador2.anyadir_equipo(equipo2)
Jugador3.anyadir_equipo(equipo2)
Jugador4.anyadir_equipo(equipo2)

print(f"Equipo : {equipo2.nombre_equipo}")
for jugador in equipo2.jugadores_eq : 
   jugador.mostrar()

print(f"Equipo : {equipo1.nombre_equipo}")
for jugador in equipo1.jugadores_eq : 
   jugador.mostrar()