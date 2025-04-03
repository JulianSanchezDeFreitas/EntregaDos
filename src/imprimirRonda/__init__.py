def estructura_ordenada(diccionario):
    valores_ordenados = []
    for keys, value in diccionario.items():
        valores_ordenados.append((keys, value))
    valores_ordenados = sorted(valores_ordenados, key= lambda c : c[1]["puntajes"], reverse=True)
    print(valores_ordenados)
        

    return valores_ordenados
def imprimir_ronda(diccionario):
    estructura_nueva = estructura_ordenada(diccionario)
    """ Esta funcion imprime una ronda de un diccionario"""
    print(f"Jugador    | Asesinatos       | Asistencias     | Muertes     | MVPs       | Puntaje   ")
    for nombre in diccionario.items():
        print(f"{nombre[0]}   |         {nombre[1]["kills"]}     |          {nombre[1]["assists"]}      |       {nombre[1]["deaths"]}        |      {nombre[1]["MVPs"]}       |         {nombre[1]["puntajes"]}")
