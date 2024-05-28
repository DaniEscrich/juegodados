import dado


class Juego:
    __jugador1 = ""
    __jugador2 = ""
    __lanzamientos = 0

    def __init__(self, jugador1, jugador2, caras1, caras2, caras3, lanzamientos, intermedios):
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_lanzamientos(lanzamientos)
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(caras2)
        self.dado3 = dado.Dado(caras3)
        self.__intermedios = (intermedios in ("S", "s"))
        self.resultado1 = 0
        self.resultado2 = 0

    def set_jugador1(self, fjugador1):
        if len(fjugador1) > 20:
            raise Exception("La longitud del nombre del jugador 1 no puede ser mayor de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        if len(fjugador2) > 20 and len(fjugador2) > 20 and len(fjugador2) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__jugador2 = fjugador2

    def set_lanzamientos(self, lanzamientos):
        if not 2 < lanzamientos <= 1000:
            raise Exception("El número de lanzamientos debe de estar entre 2 y 1000")
        else:
            self.__lanzamientos = lanzamientos

    def jugar(self):
        self.resultado1 = 0
        self.resultado2 = 0
        for x in range(self.__lanzamientos):
            ptsTirada1 = self.dado1.lanzar()
            ptsTirada2 = self.dado2.lanzar()
            ptsTirada3 = self.dado3.lanzar()
            self.resultado1 += (ptsTirada1 + ptsTirada2 + ptsTirada3)
            if self.__intermedios:
                print(
                    f"Lanzamiento {x + 1}: \n {self.__jugador1}: {ptsTirada1} {ptsTirada2} {ptsTirada3} ({(ptsTirada1 + ptsTirada2 + ptsTirada3)})")

            ptsTirada1 = self.dado1.lanzar()
            ptsTirada2 = self.dado2.lanzar()
            ptsTirada3 = self.dado3.lanzar()
            self.resultado2 += (ptsTirada1 + ptsTirada2 + ptsTirada3)

            if self.__intermedios:
                print(
                    f"{self.__jugador2}: {ptsTirada1} {ptsTirada2} {ptsTirada3} ({(ptsTirada1 + ptsTirada2 + ptsTirada3)}) \n")

    def mostrar(self):
        print(
            f"Resultados: \n Jugador 1: {self.__jugador1} \n Jugador 2: {self.__jugador2}\n Numero de lanzamientos: {self.__lanzamientos} ")
        print(
            f"Dados: {self.dado1.getCaras()},{self.dado2.getCaras()} y {self.dado3.getCaras()} \n Puntos jugador 1: {self.resultado1} \n Puntos jugador 2: {self.resultado2}")
        if self.resultado1 > self.resultado2:
            print(f"El GANADOR es {self.__jugador1} con {self.resultado1} puntos")
        elif self.resultado1 == self.resultado2:
            print("Ha habido un EMPATE")
        else:
            print(f"El GANADOR es {self.__jugador2} con {self.resultado2} puntos")
