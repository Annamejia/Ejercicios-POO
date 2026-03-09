from Jugador import Jugador
from EquipoFut import EquipoFut

jugador1 = Jugador(1, "Carlos Marin", 25, "Delantero",  8)
jugador2 = Jugador(2, "Mateo Ocampo", 28, "Mediocampo",  7)
jugador3 = Jugador(3, "Luis Correa",26, "Defensa", 9) 

equipo_1 = EquipoFut("America FC", "Medellin", "Jorge Estrada")
equipo_1.agregar(jugador1)
equipo_1.agregar(jugador2)
equipo_1.agregar(jugador3)
equipo_1.mostrar_plantilla()

equipo_2 = EquipoFut("Nacional", "Bogotá", "Ricardo Gareca")
equipo_1.remover(jugador1)
jugador1.transferir(equipo_2)

equipo_1.mostrar_plantilla()
equipo_2.mostrar_plantilla()