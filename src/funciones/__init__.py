def calcular_puntaje(stats):
    """ Esta funcion devuelve el puntaje de un jugador en esa ronda"""
    return stats["kills"]*3 + stats["assists"]*1 + (-1 if stats["deaths"] else 0) 
 
def decidir_mvp(ronda):
    """Esta funcion decide el mvp de cada ronda""" # preguntar otra forma de hacerlo
    max = 0
    for jugador, stats in ronda.items():  
        puntaje = calcular_puntaje(stats) 
        if puntaje>max: 
            max = puntaje
            jugador_mvp = jugador # me quedo con el nombre y la puntuacion maxima de cada jugador y comparo con el que sigue
    return jugador_mvp  

def inicializar_diccionario (dic_a, ronda):
    """ Esta funcion inicializa un diccionario con sus valores en 0"""
    for nombre in ronda:
        dic_a[nombre] = dict(kills = 0 ,assists  = 0 , deaths = 0, MVPs = 0 , puntajes = 0   )
    return dic_a
    
    
def actualizar_diccionario(dic_a, ronda):
    """ Esta funcion actualiza mi tabla/ diccionario por ronda""" # asigno de la tabla principal los valores correspondientes a mi tabla nueva
    mvp_ronda = decidir_mvp(ronda)
    for jugador ,stats in ronda.items():
        dic_a[jugador]["kills"] += stats["kills"]
        dic_a[jugador]["assists"] += stats["assists"]
        if mvp_ronda == jugador:
            dic_a[jugador]["MVPs"] +=1
        if stats["deaths"]==True:
            dic_a[jugador]["deaths"] +=1
        dic_a[jugador]["puntajes"] += calcular_puntaje(stats)
     # agregar una forma de ordenar la lista   

def imprimir_ronda(diccionario):
    """ Esta funcion imprime una ronda de un diccionario"""
    print(f"Jugador    | Asesinatos       | Asistencias     | Muertes     | MVPs       | Puntaje   ")
    for nombre in diccionario.items():
        print(f"{nombre[0]}   |         {nombre[1]["kills"]}     |          {nombre[1]["assists"]}      |       {nombre[1]["deaths"]}        |      {nombre[1]["MVPs"]}       |         {nombre[1]["puntajes"]}")
