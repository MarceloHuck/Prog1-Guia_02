lunes       = int(input("ingresar lluvia lunes    : "))
martes      = int(input("ingresar lluvia martes   : "))
miercoles   = int(input("ingresar lluvia miércoles: "))
jueves      = int(input("ingresar lluvia jueves   : "))
viernes     = int(input("ingresar lluvia viernes  : "))
sabado      = int(input("ingresar lluvia sábado   : "))
domingo     = int(input("ingresar lluvia domingo  : "))

nollovio    = 0
milimetros  = 0.0
for i in range(0,7,1):
    if i == 0:
        if lunes == 0:
            nollovio += 1
        else:
            milimetros += lunes
    elif i == 1:
        if martes == 0:
            nollovio += 1
        else:
            milimetros += martes
    elif i == 2:
        if miercoles == 0:
            nollovio += 1
        else:
            milimetros += miercoles    
    elif i == 3:
        if jueves == 0:
            nollovio += 1
        else:
            milimetros += jueves    
    elif i == 4:
        if viernes == 0:
            nollovio += 1
        else:
            milimetros += viernes    
    elif i == 5:
        if sabado == 0:
            nollovio += 1
        else:
            milimetros += sabado    
    elif i == 6:
        if domingo == 0:
            nollovio += 1
        else:
            milimetros += domingo
print(f"Cantidad de días sin lluvia                     : {nollovio}")  
print(f"Cantidad total de milímetros caídos en la semana: {milimetros}")