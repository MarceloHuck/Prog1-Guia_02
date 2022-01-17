ingresar    = input("Desea ingresar datos? ('S'/'N'): ")
while ingresar == "S" or ingresar == "s":
    entero = int(input("Ingresar número entero: "))
    if entero < 0:
        print(f"Número ingresado ({entero}) es negativo")
    ingresar    = input("Desea ingresar datos? ('S'/'N'): ")