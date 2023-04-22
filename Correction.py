#! /usr/local/bin/python3.8

from subprocess import *
from csv import *


def same_string(chaine_un, chaine_deux):

    if len(chaine_un) != len(chaine_deux):
        return False
    else:
        for i in range(len(chaine_un)):
            if chaine_un[i] != chaine_deux[i]:
                return False
    return True






def compte_doc(fichier):

    liste = ((run(["grep", "-i", "/*[^a-zA-Z0123456789]*/", "eleves_bis/" + fichier], capture_output="True").stdout).decode(encoding="utf8")).split("*/")
    
    chaine = ""
    compteur =  0
    
    print(liste)
    
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] != " " and liste[i][j] != "/" and liste[i][j] != "*" and liste[i][j] != "\n":
                break
            if liste[i][j] == "/" and j < len(liste[i]) - 1 and  liste[i][j+1] == "*":
                compteur = compteur + 1
                while liste[i][j] != "*" and j < len(liste[i]) - 1 and liste[i][j+1] != "/":
                    print(liste[i][j])
                    j = j + 1
                    
                    if liste[i][j] == "\n":
                        compteur = compteur + 1
                    
				
						
						

            
    
	
	#double boucle pour parcourir la chaine savoir si c'est en début de ligne
	
    return compteur

def test(executable):

    test_valides = 0
    liste = [(0, 0), (1, 0), (0, 1), (1, 1), (12, 12), (12, -43), (-1, -52)]

    for i in range(7):
        (first, second) = liste[i]
        somme = first + second

        attente = "La somme de " + str(first) + " et " + str(second) + " vaut " + str(somme) + "\n"
        resultat = ((run(["./"+executable, str(first), str(second)], capture_output="True")).stdout).decode(encoding="utf8")

        if same_string(attente, resultat) == True:
            test_valides += 1

    return test_valides



def enleve_extension(liste):
	
    print(liste)
	

    element = liste[1]

    list_elem = []

    for i in range(len(element)):
        list_elem.append(element[i])


    for i in range(2):
        list_elem.pop()

    element = "".join(list_elem)

    liste[1] = element


    return liste





run(["unzip", "Rendus_eleves"]) # On dézippe l'archive donnée
programmes = ((run(["ls", "eleves_bis/"], capture_output=True).stdout).decode(encoding="utf8")).split("\n") # On dézippe l'archive donnée



lignes =[]

for i in range(len(programmes)-1):
    chaine_descriptive = []

    compilation = run(["gcc", 'eleves_bis/' + programmes[i], "-ansi", "-Wall", "-o", "executable"], capture_output="True")

    existe_ex = (run(["ls", "executable"], capture_output="True").stderr).decode(encoding="utf8")


    print(programmes[i])
    nom = enleve_extension(programmes[i].split("_"))


    nombre_warning = len(((compilation.stderr).decode(encoding="utf8").split("warning"))) - 1
    
 
    

	
    chaine_descriptive.append(nom[0])
    chaine_descriptive.append(nom[1])


    if existe_ex != "":
        chaine_descriptive.append(0)
        chaine_descriptive.append(nombre_warning)
        chaine_descriptive.append(0)
    else:
        print(nom[0]+nom[1]+str(existe_ex))
        chaine_descriptive.append(1)
        chaine_descriptive.append(nombre_warning)
        chaine_descriptive.append(test("executable"))
        run(["rm", "executable"])

    chaine_descriptive.append(compte_doc(programmes[i]))

    lignes.append(chaine_descriptive)

    print(str(chaine_descriptive)+"\n")



print("Nombre de fichiers : "+str(len(programmes)))


run(["touch", "fichier.csv"])




file = open('fichier.csv', 'w', newline='')

ecrit = writer(file,delimiter=',', quotechar=',', quoting=QUOTE_MINIMAL)

for i in range(len(lignes)):

    ecrit.writerow(lignes[i])

