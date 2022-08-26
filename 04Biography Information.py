## Pregunte a un usuario su información personal en una sola ronda de preguntas. 
# Luego hay que verificar que la información que se ha ingresado sea válida.
# Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

name = input("ingrese su nombre: ")

while not name:
    try:
        name = input("Ingrese nombre: ")
        _ = float(name)
        print("Introduce algo ")
        name = ""
    except:
        pass
print('Hola',name)


