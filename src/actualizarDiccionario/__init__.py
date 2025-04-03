from src.funciones import decidir_mvp, calcular_puntaje
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
 
