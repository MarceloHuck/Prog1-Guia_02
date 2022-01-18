cuantos     = int(input("Cuántas personas desea ingresar: "))
ingresados  = 0
total       = 0
while ingresados < cuantos:
    edad    = int(input("Ingresar edad: "))
    total   = total + edad
    edad    = 0
    ingresados += 1
print(f"Promedio de edad: {total//cuantos}")