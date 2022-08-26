'''Example number 1 
Enfoque 1:

Se requieren los siguientes pasos:

Tome la entrada como una cadena.
Agregue la primera letra de la cadena a la salida.
Repita la cadena completa y agregue cada letra siguiente al espacio para generar la salida.
Cambie la salida a mayúsculas(acrónimo obligatorio).
'''
def acronym(stng): 
    oupt = stng[0] 

    for i in range(1, len(stng)): 
        if stng[i-1] == ' ': 
            
            oupt += stng[i] 
            
    oupt = oupt.upper() 
    return oupt 

inpt1 = "Company Of Python"
print('Example: ',acronym(inpt1)) 

inpt2 = "genius for years"
print('Example: ',acronym(inpt2)) 

'''Example number 2
Se requieren los siguientes pasos:

Tome la entrada como una cadena.
Divide las palabras.
Repita las palabras y agregue la primera letra a la salida.
Cambie la salida a mayúsculas(acrónimo obligatorio).'''

def acronym2(stng): 
    lst = stng.split() 
    oupt = "" 
    
    for word in lst: 
        oupt += word[0] 
        
    oupt = oupt.upper() 
    return oupt 

inpt1 = "Arida Fish Company"
print('Example2: ',acronym2(inpt1)) 

inpt1 = "eye for an eye"
print('Example2: ',acronym2(inpt1)) 