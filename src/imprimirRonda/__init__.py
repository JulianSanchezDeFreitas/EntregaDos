def imprimir_ronda(diccionario):
    """ Esta funcion imprime una ronda de un diccionario"""
    print(f"Jugador    | Asesinatos       | Asistencias     | Muertes     | MVPs       | Puntaje   ")
    for nombre in diccionario.items():
        print(f"{nombre[0]}   |         {nombre[1]["kills"]}     |          {nombre[1]["assists"]}      |       {nombre[1]["deaths"]}        |      {nombre[1]["MVPs"]}       |         {nombre[1]["puntajes"]}")
