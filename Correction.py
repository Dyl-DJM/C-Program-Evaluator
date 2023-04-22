#! /usr/local/bin/python3.8

from subprocess import *
from csv import *
import sys


"""
Return the comparison between two strings
"""
def same_string(chaine_un, chaine_deux):
    if len(chaine_un) != len(chaine_deux):
        return False
    else:
        for i in range(len(chaine_un)):
            if chaine_un[i] != chaine_deux[i]:
                return False
    return True

"""
Return the amount of documentation blocks
"""
def compte_doc(fichier, folder):

    # Retrieves the documentation lines
    liste = ((run(["grep", "-i", "/*[^a-zA-Z0123456789]*/", folder + fichier], capture_output="True").stdout).decode(encoding="utf8")).split("*/")

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
    return compteur


"""
Returns the amount of tests which gave the expected answer
"""
def test(executable):
    test_valides = 0
    liste = [(0, 0), (1, 0), (0, 1), (1, 1), (12, 12), (12, -43), (-1, -52)] # Program arguments we want to check the output

    for i in range(7):
        (first, second) = liste[i]
        somme = first + second

        attente = "La somme de " + str(first) + " et " + str(second) + " vaut " + str(somme) + "\n"
        resultat = ((run(["./"+executable, str(first), str(second)], capture_output="True")).stdout).decode(encoding="utf8")

        if same_string(attente, resultat) == True:
            test_valides += 1

    return test_valides


"""
Return a list string of the filename without the extension
"""
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



# =========== Main ==========================

number_arguments = len(sys.argv)
result_name_file = "out.csv"


if number_arguments != 3 and number_arguments != 4:
    print("Usage : ./Correction.py [path of the archive] [folder_name] \n ./Correction.py [path of the archive] [folder_name] [result_name_file].csv")
    exit(1)
elif number_arguments == 4:
    result_name_file = sys.argv[3]
    if not result_name_file.endswith(".csv"):
        print("The file name must be a csv extension.")
        exit(1)

archive_name = sys.argv[1]
folder_name = sys.argv[2] + "/"

if not archive_name.endswith(".zip"):
    print("The zip name must be a zip.")
    exit(1)

# unzip the archive
run(["unzip", archive_name])
programmes = ((run(["ls", folder_name], capture_output=True).stdout).decode(encoding="utf8")).split("\n") # C files list

#List of all the lines we want to write in the result file
lignes =[]

exec_name = 'executable'

for i in range(len(programmes) - 1):
    print(programmes[i])  # Display

    # List where we retrieve the current C file information
    chaine_descriptive = []

    # Check compilation by looking for an executable presence
    compilation = run(["gcc", folder_name + programmes[i], "-ansi", "-Wall", "-o", exec_name], capture_output="True")
    existe_ex = (run(["ls", exec_name], capture_output="True").stderr).decode(encoding="utf8")
    nom = enleve_extension(programmes[i].split("_"))
    nombre_warning = len(((compilation.stderr).decode(encoding="utf8").split("warning"))) - 1

    chaine_descriptive.append(nom[0])
    chaine_descriptive.append(nom[1])

    if existe_ex != "": # There is an executable
        chaine_descriptive.append(0)
        chaine_descriptive.append(nombre_warning)
        chaine_descriptive.append(0)
    else:
        print(nom[0]+nom[1]+ str(existe_ex))
        chaine_descriptive.append(1)
        chaine_descriptive.append(nombre_warning)
        chaine_descriptive.append(test(exec_name))
        run(["rm", exec_name])

    chaine_descriptive.append(compte_doc(programmes[i], folder_name))
    lignes.append(chaine_descriptive)
    print(str(chaine_descriptive)+"\n")

print("Nombre de fichiers : " + str(len(programmes)))

# csv writing part
run(["touch", result_name_file]) # create the file

file = open(result_name_file, 'w', newline='') # Open the file in write mode
ecrit = writer(file,delimiter=',', quotechar=',', quoting=QUOTE_MINIMAL)

# We write ach line in the file
for i in range(len(lignes)):
    ecrit.writerow(lignes[i])


