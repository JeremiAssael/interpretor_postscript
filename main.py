from class_token import *
from class_useful_objects import *


def inter(instruction, pile, dico_function):
    """Fonction intermédiaire qui va permettre la bonne exécution du programme principal. 
    Son fonctionnement est détaillé à chaque étape"""
    instr=Instruction(instruction)
    tab_instruction=instr.split_instruction()
    L=[]
    for i in range(len(tab_instruction)):
        if tab_instruction[i]!="{" and tab_instruction[i]!="}":
            tab_instruction[i]=get_type(tab_instruction[i])
    tab_instruction=traitement_procedure(tab_instruction)   
    tab_instruction=conv_procedure(tab_instruction)
    """Les étapes ci-dessus ont permis de récupérer l'instruction entrée pas l'utilisateur sous forme d'une chaine de caractère, 
    puis de la convertir en une liste d'instruction (méthode split_instruction), et d'associer le bon type à chaque token (boucle for). 
    On a ensuite supprimé toute occurence des accolades, dans l'éventualité où un procédure est présente 
    et remplacé au bonne endroit dans la liste des instructions la procédure comme un objet composite, soit
    une liste d'objets d'une classe fille de la classe Token (fonction traitement_procedure). 
    Enfin, la fonction conv_procedure nous a permit de transtyper chaque liste présente dans l'instruction en une procédure"""
    for i in range(len(tab_instruction)):
        pile, dico_function=tab_instruction[i].operation(pile, i, dico_function)
    """Dans cette boucle, on parcourt simplement chaque objet de notre liste d'instruction, et en fonction du type (classe fille de la classe Token), 
    on execute l'opération associée (appelle à la méthode opération de la bonne classe fill de la classe Token)"""
    L.append(pile)
    L.append(dico_function)
    """On récupére la pile du programme et le dictionnaire des fonctions"""
    return L


def conv_procedure(liste):
    """Fonction permettant de convertir chaque objet de type liste dans une liste quelconque en un objet de type Procedure.
    Fonction récursive afin de traiter les éventuels "procédures dans les procédures" """
    for i in range(len(liste)):
        if type(liste[i]) is list:
            conv_procedure(liste[i])
            liste[i]=Procedure(liste[i])
    return liste



def main():
    """Programme principal: à chaque instruction entrée, l'opération souhaitée s'exécute. La pile reste la même. 
    Il est nécessaire de relancer le programme pour avoir une nouvelle pile. Les ">>>" signifient que c'est à l'utilisateur d'écrire.
    Si l'on veut réinitialiser la pile, il suffit d'entrer l'instruction "clear". Le dictionnaire des fonctions est aussi réinitialisé"""
    dico_function={}
    instruction=input(">>>")
    liste=[]
    pile=Stack([])
    while instruction!="exit" and instruction !="clear":
        liste=inter(instruction, pile, dico_function)
        pile=liste[0]
        print(liste[0].print_stack())
        dico_function=liste[1]
        instruction=input(">>>")
    if instruction=="clear":
        """On utilise la récursion pour relancer le programme avec une pile vide"""
        main()


"""On exécute le programme"""
main()





