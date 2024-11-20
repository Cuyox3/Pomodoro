import time
import pynpunt
#variables 

#Lo voy a estar probando con segundos para ver si funciona 
def ciclo(): #Tiene que poder recibir el valor para poder reniciciar y tiene que tener la posibilidad de pausar o reiniciar en cualquier momento 
    
    t_corto = 25
    d_corto = 5
    t_largo = 45
    d_largo = 15
    print("\n")
    print (f"Empezaremos a la cuenta de 3")
    for i in range(1,4):
        print (f"Empezaremos en {i}")
        time.sleep(1)
        
    while t_corto!=0:
        print("Restan: "+str(t_corto)+" segundos de trabajo")
        t_corto-=1
        time.sleep(1)

        try:
            seleccionar = 0
            seleccionar = int(input("Si quieres pausar escribe 1\nSi quieres reiniciar escribe 2\n"))
            if seleccionar == 1:pausa()
            elif seleccionar == 2:reininio()
            else: print("-->Esa respuesta es erronea, porfavor intenta de nuevo\n")
        except ValueError: 
            print("-->Tines que ingrsar un numero\n")   

    while d_corto!=0:
        print("Restan: "+str(d_corto)+" segundos de descanso")
        d_corto-=1
        time.sleep(1)
        try:
            seleccionar= int(input("Si quieres pausar escribe 1\n"))
            if seleccionar == 1:pausa()
            else: print("-->Esa respuesta es erronea, porfavor intenta de nuevo\n")
        except ValueError: 
            print("-->Tines que ingrsar un numero\n")  

    while t_largo!=0:
        print("Restan: "+str(t_largo)+" segundos de trabajo")
        t_largo-=1
        time.sleep(1)
        try:
            seleccionar = int(input("Si quieres pausar escribe 1\n"))
            if seleccionar == 1:pausa()
            else: print("-->Esa respuesta es erronea, porfavor intenta de nuevo\n")
        except ValueError: 
            print("-->Tines que ingrsar un numero\n")  

    while d_largo!=0:
        print("Restan: "+str(d_largo)+" segundos de descanso")
        d_largo-=1
        time.sleep(1)
        try:
            seleccionar = int(input("Si quieres pausar escribe 1\n"))
            if seleccionar == 1:pausa()
            else: print("-->Esa respuesta es erronea, porfavor intenta de nuevo\n")
        except ValueError: 
            print("-->Tines que ingrsar un numero\n")  
    print("Felciades, has completado un pomodoro")
    return 


def pausa (): #tengo que hacer que regrese el conteo que llevaba 

    print("\n")
    print("Estas en pausa")
    print("Para reaundar selecciona un 1")
    try:
        reanudar = int (input("Quieres reanudar?"))
        if reanudar == 1: ciclo()
        else: print("-->Esa respuesta es erronea, porfavor intenta de nuevo\n")
    except: print("-->Tines que teclar un numero ")
    return

def reininio():
    ciclo()
    return

def seleccion(): 
   
    while True:
        try:
            print("\n")
            print("1-Pausar 2-Reiniciar 3-Inciar")
            seleccionar = int(input("Que es lo que queires hacer?\n"))
            if seleccionar == 1:pausa()
            elif seleccionar == 2:reininio()
            elif seleccionar == 3:ciclo()
            else: print("-->Esa respuesta es erronea, porfavor intenta de nuevo\n")
        except ValueError: 
            print("-->Tines que ingrsar un numero\n")


seleccion()
