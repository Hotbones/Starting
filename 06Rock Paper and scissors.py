# example numer 1, It´s very easy but effective
import random

opciones = ['piedra', 'papel', 'tijera']
print('-' * 30)
print('Piedra, papel o tijera'.center(30))
print('-' * 30)
print('1. Piedra'.center(30))
print('2. Papel'.center(30))
print('3. Tijera'.center(30))
humano = int(input('\nIngrese una opción: '))
pc = random.randint(1,3)
resultado = 'Vos elegiste ' + opciones[humano - 1] + '.\n'
resultado += 'La computadora eligió ' + opciones[pc - 1] + '.\n'

print((humano - pc) % 3)
if (humano - pc) % 3 == 0:
    resultado += 'Empate'
elif (humano - pc) % 3 == 1:
    resultado += 'Ganaste'
else:
    resultado += 'Perdiste.'
    
print(resultado)

#------------------------------------------------------------------------------------------