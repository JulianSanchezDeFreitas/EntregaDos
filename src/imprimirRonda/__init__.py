def estructura_ordenada(diccionario):
    """ Esta funcion recibe un diccionario por parametro y devuelve en su lugar una lista de tuplas ordenadas por puntaje"""
    valores_ordenados = []
    for keys, value in diccionario.items():
        valores_ordenados.append((keys, value))
    valores_ordenados = sorted(valores_ordenados, key= lambda c : c[1]["puntajes"], reverse=True)
    return valores_ordenados

def imprimir_ronda(diccionario):
    """ Esta funcion imprime una ronda de un diccionario"""
    tabla_ordenada = estructura_ordenada(diccionario)
    print(f"Jugador    | Asesinatos       | Asistencias     | Muertes     | MVPs       | Puntaje   ")
    for jugador in tabla_ordenada:
        print(f"{jugador[0] if len(jugador[0])==6 else (f"{jugador[0]} ")}   |         {jugador[1]["kills"]}     |          {jugador[1]["assists"]}      |       {jugador[1]["deaths"]}        |      {jugador[1]["MVPs"]}       |      {jugador[1]["puntajes"]}")
