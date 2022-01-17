nro00   = int(input("ingresar número entero 1  : "))
nro01   = int(input("ingresar número entero 2  : "))
nro02   = int(input("ingresar número entero 3  : "))
nro03   = int(input("ingresar número entero 4  : "))
nro04   = int(input("ingresar número entero 5  : "))
nro05   = int(input("ingresar número entero 6  : "))
nro06   = int(input("ingresar número entero 7  : "))
nro07   = int(input("ingresar número entero 8  : "))
nro08   = int(input("ingresar número entero 9  : "))
nro09   = int(input("ingresar número entero 10 : "))
contador    = 0
for i in range(0,10,1):
    if i == 0:
        if nro00 > 23:
            contador = contador + 1
    elif i == 1:
        if nro01 > 23:
            contador = contador + 1        
    elif i == 2:
        if nro02 > 23:
            contador = contador + 1        
    elif i == 3:
        if nro03 > 23:
            contador = contador + 1        
    elif i == 4:
        if nro04 > 23:
            contador = contador + 1        
    elif i == 5:
        if nro05 > 23:
            contador = contador + 1        
    elif i == 6:
        if nro06 > 23:
            contador = contador + 1        
    elif i == 7:
        if nro07 > 23:
            contador = contador + 1        
    elif i == 8:
        if nro08 > 23:
            contador = contador + 1        
    else:
        if nro09 > 23:
            contador = contador + 1        
print(f"Cantidad total de números ingresados mayores a 23: {contador}")