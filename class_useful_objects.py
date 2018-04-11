#-*-coding:Utf-8 -*

import random
import string
import re

class Stack():
    """Classe des objets de type pile"""

    def __init__(self, liste):
        self.liste=liste

    def print_stack(self):
        """Methode d'affichage de la pile, ce qui sera affiché à l'utilisateur"""
        if self.liste==[]:
            """Si mon stack est vide, on affiche une chaine de caractère vide"""
            string=""
        else:
            """ On affiche chaque élément de la pile sous forme d'une chaine de caractère (attribut associé à chaque objet à afficher)"""
            string=str(self.liste[0].string)
            for i in range(1,len(self.liste)):
                string+=" " + str(self.liste[i].string)
        return string

    def append(self, element):
        """Méthode permettant d'ajouter un objet en fin de pile"""
        self.liste.append(element)
        return self
            
    def pop(self, nb_of_elements):
        """Méthode permettant de supprimer un nombre d'objet "nb_of_element" de la pile et 
        d'obtenir la liste de ces éléments supprimés, dans l'ordre dans lequel ils étaient dans la pile"""
        L=[]
        if len(self.liste)>=nb_of_elements:
            for i in range(nb_of_elements):
                L.append(self.liste.pop())
            L.reverse()
            return L
        else:
            print("Syntax error: used operator lacks a term")

    def pop_element(self):
        """Méthode permettant de supprimer le dernier élément de la pile et de renvoyer la pile sans cet élément"""
        L=[]
        if len(self.liste)>=1:
            L=self.pop(1)
            return self
        else:
            print("Syntax error: no term to remove")

    def exch(self):
        """Méthode qui permet d'échanger les deux derniers éléments de la pile"""
        L=[]
        if len(self.liste)>=2:
            """On vérifie que la pile a bien deux éléments à échanger"""
            L=self.pop(2)
            self.append(L[1])
            self.append(L[0])
            return self
        else:
            print("Syntax error: no elements to exchange")

    def dup(self):
        """Méthode permettant de dupliquer le dernier élément de la pile"""
        if len(self.liste)>=1:
            """On vérifie que la pile a bien un élément à dupliquer"""
            self.append(self.liste[-1])
        else:
            print("Syntax error: no element to duplicate")


class Instruction():

    def __init__(self, instruction):
        self.instruction=instruction

    def split_instruction(self):
        """Méthode permettant de séparer la chaîne de carcatère instruction en tokens. 
        Elle commence par rajouter un espace après une accolade ouvrante "{" puis rajoute un espace, si besoin avant une accolade fermante "}".
        On utilise en suite la méthode sur les chaines de caractères permettant de construire une liste de tokens. 
        Les accolades sont donc égalemenet des tokens."""
        nb=self.instruction.count("{")
        for i in range(len(self.instruction)+nb):
            if self.instruction[i]=="{":
                self.instruction=self.instruction[0:i+1]+" "+self.instruction[i+1:len(self.instruction)+1]
        nb2=self.instruction.count("(\S)?}")
        for i in range(len(self.instruction)+nb2):
            if self.instruction[i]=="}" and not re.match(" ",self.instruction[i-1]) and not re.match("{",self.instruction[i-2]):
                self.instruction=self.instruction[0:i]+" "+self.instruction[i:len(self.instruction)+1]
            elif self.instruction[i]=="}" and re.match(" ",self.instruction[i-1]) and re.match("{",self.instruction[i-2]):
                self.instruction=self.instruction[0:i]+" "+self.instruction[i:len(self.instruction)+1]
        instruction_split=self.instruction.split()
        return instruction_split



def traitement_procedure(liste):
    """L'objet de cette fonction est de transformée une liste de tokens, dans laquelle il ya des accolades, en une liste sans ces accolades. 
    Tout ce qu'il y a entre ces accolades est mis dans une liste, inséré au bon endroit dans la liste originale. 
    Il est donc nécessaire pour commencer, avec un compteur de repérer une accolade ouvrante et son accolade fermante associée."""
    while liste.count("{")!=0:
        n=len(liste)
        K=[]
        """Initialisation du compteur"""
        comp_acc=0
        for i in range(n):
            if liste[i]=="{":
                K.append(i)
                for j in range(i+1,n):
                    if liste[j]=="{":
                        comp_acc+=1
                    elif liste[j]=="}":
                        comp_acc=comp_acc-1
                        if comp_acc==-1:
                            K.append(j)
        """On récupére tout ce qu'il y a entre les accolades et le met dans une liste"""
        liste_procedure=liste[K[0]+1:K[1]]
        """Cette fonction est récursive afin de traiter la possibilité d'avoir des accolades dans des accolades"""
        liste_procedure=traitement_procedure(liste_procedure)
        """La suite des instructions permet de supprimer de notre liste originale les éléments entre accolades 
        et d'insérer la liste construite à partir de ces élements dans notre nouvelle liste"""
        for l in range(K[0], K[1]+1):
            liste.pop(K[0])
        liste.insert(K[0], liste_procedure)
    return liste    


