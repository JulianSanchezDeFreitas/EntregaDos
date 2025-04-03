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
    
    
