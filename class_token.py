#-*-coding:Utf-8 -*

from class_useful_objects import *
import re

class Token:
    pass

class OperateurUnitaire(Token):
    """Classe des opérateurs unitaires (nombre entier, booléen)"""

    def __init__(self, string):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur unitaire: il est directement empilé"""
        stack.append(self)
        return stack, dico_function


class OperateurBinaire(Token):
    """Classe des opérateurs binaires (tous ceux qui nécessitent l'utilisation des deux derniers élémenst de la pile)"""

    def __init__(self, string):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur binaire: dépile les deux derniers éléments 
        et effectue l'opération associée en fonction de cet opérateur, puis rempile le résultat"""
        terms=stack.pop(2)
        if self.string=="add":
            stack.append(get_type(int(terms[0].string)+int(terms[1].string)))
        elif self.string=="sub":
            stack.append(get_type(int(terms[0].string)-int(terms[1].string)))
        elif self.string=="mul":
            stack.append(get_type(int(terms[0].string)*int(terms[1].string)))
        elif self.string=="idiv":
            stack.append(get_type(int(terms[0].string)//int(terms[1].string)))
        elif self.string=="eq":
            if int(terms[0].string)==int(terms[1].string):
                stack.append(get_type("true"))
            else:
                stack.append(get_type("false"))
        elif self.string=="ne":
            if int(terms[0].string)!=int(terms[1].string):
                stack.append(get_type("true"))
            else:
                stack.append(get_type("false"))
        elif self.string=="lt":
            if int(terms[0].string)<int(terms[1].string):
                stack.append(get_type("true"))
            else:
                stack.append(get_type("false"))
        elif self.string=="le":
            if int(terms[0].string)<=int(terms[1].string):
                stack.append(get_type("true"))
            else:
                stack.append(get_type("false"))
        elif self.string=="gt":
            if int(terms[0].string)>int(terms[1].string):
                stack.append(get_type("true"))
            else:
                stack.append(get_type("false"))
        elif self.string=="ge":
            if int(terms[0].string)>=int(terms[1].string):
                stack.append(get_type("true"))
            else:
                stack.append(get_type("false"))
        elif self.string=="def":
            """Opérateur binaire qui récupère le nom et la procédure définis et crée une nouvelle entrée dans le dictionnaire des fonctions"""
            dico_function[terms[0].lstrip("/")]=terms[1]
        elif self.string=="if": 
            if terms[0].string=="true": 
                """On regarde si la procédure indiquée est vide"""
                if len(terms[1].liste)==0:
                    """Si elle est vide on ne fait rien"""
                    pass
                else:
                    """Si elle n'est pas vide, on ajoute les éléments de la liste procédure dans notre pile et effectue les opérations asscociées, 
                    grâce à la fonction intermédiaire inter_list_partielle, en considérant cette nouvelle pile comme une liste d'instruction"""
                    for i in range(len(terms[1].liste)):
                        stack.append(terms[1].liste[i])
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
            elif terms[0].string=="false":
                pass
            else:
                print("Syntax error: if lacks a term")
        else:
            print("Ce n'est pas un opérateur binaire")
        return stack, dico_function


class OperateurTernaire(Token):
    """Classe des opérateurs ternaires (tous ceux qui nécessitent l'utilisation des trois derniers élémenst de la pile)"""

    def __init__(self, string):
        self.string=string 

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur ternaire: dépile les trois derniers éléments 
        et effectue l'opération associée en fonction de cet opérateur, puis rempile le résultat"""
        terms=stack.pop(3)
        if self.string=="ifelse":
            if terms[0].string=="true": 
                if len(terms[1].liste)==0:
                    """La procédure est-elle vide ?"""
                    pass
                else:
                    """Si elle n'est pas vide, on ajoute les éléments de la liste procédure dans notre pile et effectue les opérations asscociées, 
                    grâce à la fonction intermédiaire inter_list_partielle, en considérant cette nouvelle pile comme une liste d'instruction"""
                    for i in range(len(terms[1].liste)):
                        stack.append(terms[1].liste[i])
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
            elif terms[0].string=="false":
                if len(terms[2].liste)==0:
                    """La procédure est-elle vide ?"""
                    pass
                else:
                    """Si elle n'est pas vide, on ajoute les éléments de la liste procédure dans notre pile et effectue les opérations asscociées, 
                    grâce à la fonction intermédiaire inter_list_partielle, en considérant cette nouvelle pile comme une liste d'instruction"""
                    for i in range(len(terms[2].liste)):
                        stack.append(terms[2].liste[i])
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
            else:
                print("Syntax error: ifelse lacks a term")
        return stack, dico_function


class OperateurQuaternaire(Token):
    """Classe des opérateurs quaternaires (tous ceux qui nécessitent l'utilisation des deux derniers élémenst de la pile)"""

    def __init__(self, string):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur quaternaire: dépile les quatre derniers éléments 
        et effectue l'opération associée en fonction de cet opérateur, puis rempile le résultat"""
        terms=stack.pop(4)
        if self.string=="for":
            if len(terms[3].liste)==0:
                """La procédure est-elle vide ?"""
                for i in range(int(terms[0].string),int(terms[2].string)+1,int(terms[1].string)):
                    """Dans le cas d'une procédure vide, on ajoute un à un les éléments compris entre les bornes de notre boucle, en fonction du pas"""
                    stack.append(get_type(i))
            else:
                for i in range(int(terms[0].string),int(terms[2].string)+1,int(terms[1].string)):
                    """Si la procédure n'est pas vide, on ajoute le premier élément de la boucle for, 
                    on ajoute la procédure, on effectue l'opération associée.
                    On recommence pour chaque élémént de la boucle, jusqu'à atteindre la borne de fin, en tenant compte du pas"""
                    stack.append(get_type(i))
                    for i in range(len(terms[3].liste)):
                        stack.append(terms[3].liste[i])
                    """Utilisation de la fonction intermédiaire inter_list_partielle qui permet de gérer les procédures"""
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
        else:
            print("Syntax error: for lacks a term")
        return stack, dico_function


class Name(Token):
    """Classe des noms, utilisés dans la définition de foncton ou dans l'appel à une fonction"""

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        if self.string[0]=="/":
            """Si le nom est précédé du caractère "/" c'est qu'il sert à définir une foction, auquel cas on l'empile simplement"""
            stack.append(self.string)
        else:
            if dico_function.get(self.string)!=None:
                """Si le nom est bien présnet dans le dictionnaire des fonctions, 
                on appelle la fonction associée et exécute la procédure associée avec la fonction intermédiaire inter_list_partielle"""
                procedure=dico_function[self.string]
                for i in range(len(procedure.liste)):
                    stack.append(procedure.liste[i])
                liste=inter_list_partielle(stack, dico_function)
                stack=Stack(liste[0])
            else:
                print("Syntax error: terms not recognized")        
        return stack, dico_function


class Procedure(Token):
    """Classe des procédures: objet composite dont l'attribut est une liste d'objets de type d'une classe fille de la classe Token"""

    def __init__(self, liste):
        self.liste=liste

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'une procédure: on l'empile"""
        stack.append(self)
        return stack, dico_function


class Dup(Token):
    """Classe de l'objet permettant l'appel à la méthode de la classe Stack pour dupliquer le dernier objet de la pile."""

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        stack.dup()
        return stack, dico_function


class Exch(Token):
    """Classe de l'objet permettant l'appel à la méthode de la classe Stack pour échanger les deux derniers objets de la pile."""

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        stack.exch()
        return stack, dico_function


class Pop(Token):
    """Classe de l'objet permettant l'appel à la méthode de la classe Stack pour supprimer le dernier objet de la pile."""

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        stack.pop_element()
        return stack, dico_function


def get_type(token):
    """Fonction permettant de reconnaitre pour un token (sous forme de chaine de caractère) sa classe associée et de le transtyper"""
    if token in ["true","false"]:
        token=OperateurUnitaire(token)
        return token
    elif re.search("^[-]?\d*$",str(token))!=None:
        try:
            b=int(token)
            token=OperateurUnitaire(token)
            return token
        except:
            pass
    elif token in ["add","sub", "mul", "idiv", "eq", "ne", "lt", "le", "gt", "ge", "def", "if"]:
        token=OperateurBinaire(token)
        return token
    elif token in ["ifelse"]:
        token=OperateurTernaire(token)
        return token
    elif token in ["for"]:
        token=OperateurQuaternaire(token)
        return token
    elif token in ["def"]:
        token=Def(token)
        return token
    elif token in ["dup"]:
        token=Dup(token)
        return token
    elif token in ["exch"]:
        token=Exch(token)
        return token
    elif token in ["pop"]:
        token=Pop(token)
        return token
    elif token[0]=="/" and re.search("^\w*$",token[1:])!=None:
        token=Name(token)
        return token
    elif re.search("^\w*$",token)!=None:
        token=Name(token)
        return token
    else:
        print("Syntax error: terms not recognized")

    

def inter_list_partielle(stack, dico_function):
    """Fonction intermédiaire indispensable dans la gestion des procédures.
    La pile actuelle devient une liste d'instruction qui va être lue comme si elle était issue d'une instruction entrée par l'utilisateur"""
    tab_instruction=stack.liste
    n=len(tab_instruction)
    pile=Stack([])
    L=[]
    for i in range(n):
        pile, dico_function=tab_instruction[i].operation(pile, i, dico_function)
    L.append(pile.liste)
    L.append(dico_function)
    return L
