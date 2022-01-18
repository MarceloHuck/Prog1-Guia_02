from xml.dom import minicompat
from pkg_resources import PkgResourcesDeprecationWarning


ingresar    = input("Desea ingresar datos? ('S'/'N'): ")
persona     = ""
minimo      = 0.0
while ingresar == "S" or ingresar == "s":
    nombre    = input("Ingresar persona   : ")
    salario   = float(input("Ingresar salario: $ "))
    if minimo == 0.0:
        minimo  = salario
        persona = nombre
    else:
        if salario < minimo:
            minimo = salario
            persona = nombre
    ingresar    = input("Desea ingresar más personas y sus salarios? ('S'/'N'): ")
print(f"Menor salario: {persona}")