ingresar    = input("Desea ingresar datos? ('S'/'N'): ")
sueldo      = 0.0
total       = 0.0
while ingresar == "S" or ingresar == "s":
    sueldo  = float(input("Ingresar sueldo: "))
    total   = total + sueldo
    sueldo  = 0.0
    ingresar    = input("Desea ingresar mas sueldos? ('S'/'N'): ")
print(f"Total de sueldos ingresados: {total}")