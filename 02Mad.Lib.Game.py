# Mad Libs Generator - Charles Joseph Monaghan 11/10/2017
# Traducido por Anartz Mugika Ledo 23/04/2021

# Loop back to this point once code finishes
loop = 1

while (loop < 10):

    # Todas las preguntas que se le realiza al usuario para que las conteste
    noun = input("Selecciona un sustantivo: ")
    p_noun = input("Selecciona un sustantivo en plural: ")
    noun2 = input("Selecciona un sustantivo: ")
    place = input("Nombra un lugar: ")
    adjective = input("Selecciona un adjetivo (Describe una palabra): ")
    noun3 = input("Selecciona un sustantivo: ")
    noun4 = input("Selecciona el último sustantivo: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("The anger of your",noun," and you", p_noun)
    print ("can be friendly with your", noun2,",")
    print ("Be kind with your",p_noun,"in the ",place)
    print ("but don't let your heart always",adjective,"."),
    print ()
    print ("More may it be than you",noun3,",")
    print ("be a beauty",noun4,".")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1