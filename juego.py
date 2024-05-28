import dado


class Juego:

    """
    Explicar programa
    .. include:: README.md
    """
    __jugador1 = ""
    __jugador2 = ""
    __jugador3 = ""
    __lanzamientos = 0


    def __init__(self, jugador1, jugador2, jugador3, caras1, caras2, caras3,caras4, lanzamientos, intermedios):
        """
        Constructor de la clase juego
        :param jugador1: str
        :param jugador2: str
        :param jugador3: str
        :param caras1: int
        :param caras2: int
        :param caras3: int
        :param caras4: int
        :param lanzamientos: int
        :param intermedios: str
        """
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_jugador3(jugador3)
        self.set_lanzamientos(lanzamientos)
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(caras2)
        self.dado3 = dado.Dado(caras3)
        self.dado4 = dado.Dado(caras4)
        self.__intermedios = (intermedios in ("S", "s"))
        self.resultado1 = 0
        self.resultado2 = 0
        self.resultado3 = 0

        if (caras1 == caras2 or caras1 == caras3 or caras1 == caras4 or caras2 == caras3 or caras2 == caras4 or caras3 == caras4):
                raise Exception ("Errors cares iguals")

    def set_jugador1(self, fjugador1):
        """
        establace en nombr
        :param fjugador1: str
        :return: str
        """
        if len(fjugador1) > 20:
            raise Exception("La longitud del nom del jugador 1 no pot ser major de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        """
        establece nombre
        :param fjugador2: str
        :return: str
        """
        if len(fjugador2) > 20:
            raise Exception("La longitud del nom del jugador 2 no pot ser major de 20")
        else:
            self.__jugador2 = fjugador2

    def set_jugador3(self, fjugador3):
        """
        establece nombre
        :param fjugador3: str
        :return: str
        """
        if len(fjugador3) > 20:
            raise Exception("La longitud del nom del jugador 3 no pot ser major de 20")
        else:
            self.__jugador3 = fjugador3

    def set_lanzamientos(self, lanzamientos):
        """
        Establecer lanzamientos
        :param lanzamientos: int
        :return: int
        """
        if not 2 < lanzamientos <= 1000:
            raise Exception("El nombre de llançaments han d'estar entre 2 i 1000")
        else:
            self.__lanzamientos = lanzamientos



    def jugar(self):
        """
        juegan
        :return: str
        """
        for x in range(self.__lanzamientos):
            ptsTirada1 = self.dado1.lanzar()
            ptsTirada2 = self.dado2.lanzar()
            ptsTirada3 = self.dado3.lanzar()
            ptsTirada4 = self.dado4.lanzar()
            self.resultado1 += (ptsTirada1 + ptsTirada2 + ptsTirada3 + ptsTirada4)
            if self.__intermedios:
                print(
                    f"Llançament {x + 1}: \n {self.__jugador1}: {ptsTirada1} {ptsTirada2} {ptsTirada3} {ptsTirada4} ({(ptsTirada1 + ptsTirada2 + ptsTirada3 + ptsTirada4)})")

            ptsTirada1 = self.dado1.lanzar()
            ptsTirada2 = self.dado2.lanzar()
            ptsTirada3 = self.dado3.lanzar()
            ptsTirada4 = self.dado4.lanzar()
            self.resultado2 += (ptsTirada1 + ptsTirada2 + ptsTirada3 + ptsTirada4)
            if self.__intermedios:
                print(
                    f"{self.__jugador2}: {ptsTirada1} {ptsTirada2} {ptsTirada3} {ptsTirada4} ({(ptsTirada1 + ptsTirada2 + ptsTirada3 + ptsTirada4)})")
            ptsTirada1 = self.dado1.lanzar()
            ptsTirada2 = self.dado2.lanzar()
            ptsTirada3 = self.dado3.lanzar()
            ptsTirada4 = self.dado4.lanzar()
            self.resultado3 += (ptsTirada1 + ptsTirada2 + ptsTirada3 + ptsTirada4)
            if self.__intermedios:
                print(f"{self.__jugador3}: {ptsTirada1} {ptsTirada2} {ptsTirada3} ({(ptsTirada1 + ptsTirada2 + ptsTirada3 + ptsTirada4)}) \n")

    def mostrar(self):
        """
        Muestran
        :return: str
        """
        print(f"Resultats: \n Jugador 1: {self.__jugador1} \n Jugador 2: {self.__jugador2} \n Jugador 3: {self.__jugador3} \n Nombre de Llançaments: {self.__lanzamientos} ")
        print(f"Daus: {self.dado1.getCaras()},{self.dado2.getCaras()} i {self.dado3.getCaras()} \n Punts jugador 1: {self.resultado1} \n Punts jugador 2: {self.resultado2} \n Punts jugador 3: {self.resultado3}")
        if self.resultado1 > self.resultado2 and self.resultado1 > self.resultado3:
            print(f"El GUANYADOR es {self.__jugador1} amb {self.resultado1} punts")
        elif self.resultado2 > self.resultado1 and self.resultado2 > self.resultado3:
            print(f"El GUANYADOR es {self.__jugador2} amb {self.resultado2} punts")
        elif self.resultado3 > self.resultado1 and self.resultado3 > self.resultado2:
            print(f"El GUANYADOR es {self.__jugador3} amb {self.resultado3} punts")
        else:
            print(f"EMPAT!!!")
