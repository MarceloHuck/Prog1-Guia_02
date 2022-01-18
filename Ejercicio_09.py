ingresar    = input("Desea ingresar datos? ('S'/'N'): ")
maximo      = 0.0
while ingresar == "S" or ingresar == "s":
    valor  = float(input("Ingresar numero real positivo: "))
    if maximo < valor:
        maximo = valor
    valor       = 0.0
    ingresar    = input("Desea ingresar más números reales? ('S'/'N'): ")
print(f"Valor Máximo: {maximo}")