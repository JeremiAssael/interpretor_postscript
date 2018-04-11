#-*-coding:Utf-8 -*

import random
import string
import re

class Stack():
    """Classe des piles: utilisées lors de l'interrétation de l'instruction entrée par l'utilisateur, utilisée pour renvoyer le résultat"""

    def __init__(self, liste):
        self.liste=liste

    def print_stack(self):
        """Methode d'affichage de la pile, ce qui sera affiché à l'utilisateur"""
        if self.liste==[]:
            """Si mon stack est vide, on affiche une chaine de caractère vide"""
            string=""
        else:
            string=str(self.liste[0].string)
            for i in range(1,len(self.liste)):
                string+=" " + str(self.liste[i].string)
        return string

    def append(self, element):
        self.liste.append(element)
        return self
            
    def pop(self, nb_of_elements):
        L=[]
        if len(self.liste)>=nb_of_elements:
            for i in range(nb_of_elements):
                L.append(self.liste.pop())
            L.reverse()
            return L
        else:
            print("Syntax error: used operator lacks a term")

    def pop_element(self):
        L=[]
        if len(self.liste)>=1:
            L=self.pop(1)
            return self
        else:
            print("Syntax error: no term to remove")

    def exch(self):
        L=[]
        if len(self.liste)>=2:
            L=self.pop(2)
            self.append(L[1])
            self.append(L[0])
            return self
        else:
            print("Syntax error: no elements to exchange")

    def dup(self):
        if len(self.liste)>=1:
            self.append(self.liste[-1])
        else:
            print("Syntax error: no element to duplicate")


class Instruction():

    def __init__(self, instruction):
        self.instruction=instruction


    def split_instruction(self):
        """Méthode permettant de séparer ma chaîne de carcatère instruction en tokens (qui sont aussi des chaînes de caractères)"""
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

def split_tot(liste):
    while liste.count("{")!=0:
        n=len(liste)
        K=[]
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
        liste_procedure=liste[K[0]+1:K[1]]
        liste_procedure=split_tot(liste_procedure)
        for l in range(K[0], K[1]+1):
            liste.pop(K[0])
        liste.insert(K[0], liste_procedure)
    return liste    

