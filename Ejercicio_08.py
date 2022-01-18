precio      = 1
cantidad    = 0
ingresar    = 'S'
while precio != 0:
    auto    = input("Ingresar auto  : ")
    precio  = int(input("Ingresar precio ('0' para terminar): $ "))
    if precio >= 1460000 and precio <= 2850000:
        cantidad += 1
print(f"Cantidad de autos con precio entre 1460000 y 2850000: {cantidad}")