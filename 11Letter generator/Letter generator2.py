from time import sleep
import os


def lista_canciones():
    print('\n')
    print("""Generador de letras de canciónes de Linkin Park
            A continuación escoja una canción.
            1. Faint
            2. In the end
            3. New divide
            4. One more light
            5. Crawling
            6. Castle of glass
            7. Leave out all the rest
            8. Burn it down
            9. Papercut
            10.Breaking the habit
            *El orden no implica que una sea mejor que otra""")
    print('\n')

canciones = ['faint'
    ,'in the end'
    ,'new divide'
    ,'one more light'
    ,'crawling'
    ,'castle of glass'
    ,'leave out all the rest'
    ,'burn it down'
    ,'papercut',
    'breaking the habit']

lista_canciones()

def cancion(song):
    contador = 0
    while contador < 2:
        if song in canciones:
            eleccion = song + ".txt"
            archivo = open(eleccion)
            print(archivo.read())
            volver =  input('Quieres volver al menú, (si/no): ').lower()
            if volver == 'si':
                os.system('cls')
                lista_canciones()
                song = input('>>> ').lower()
            elif volver == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                contador += 1
                print('Respuesta equivocada, tienes  ', 2 - contador, 'opción(es) más')
                sleep(1)
                continue
        else:
            print('Revisa lo que escribes')
            sleep(1)
            os.system('cls')
            lista_canciones()
            song = input('>>> ').lower()


song = input('>>> ').lower()
cancion(song)
