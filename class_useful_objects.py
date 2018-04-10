#-*-coding:Utf-8 -*

import random
import string

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
            string=str(self.liste[0])
            for i in range(1,len(self.liste)):
                string+=" " + str(self.liste[i])
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
        size=len(self.instruction)
        comp_acc=0
        L=[]
        replacement=[]
        maillon_tab=[]
        for i in range(size):
            if self.instruction[i]=="{":
                L.append(i)
                for j in range(i+1,size):
                    if self.instruction[j]=="{":
                        comp_acc+=1
                    elif self.instruction[j]=="}":
                        comp_acc=comp_acc-1
                        if comp_acc==-1:
                            L.append(j)
                            maillon=self.instruction[L[0]:L[1]+1]
                            maillon_tab.append(maillon)
                            rand=''.join([random.choice(string.ascii_letters + string.digits) for n in range(L[1]+1-L[0])])
                            """verifier que rand n'est pas dans le dico des fonctions ou un nom dans le reste de la chaine, sinon change"""
                            self.instruction=self.instruction.replace(maillon,rand)
                            replacement.append(rand)
                            L=[]
                            comp_acc=0
        string_split_no_proc=self.instruction.split()
        for i in range(len(replacement)):
            for j in range(len(string_split_no_proc)):
                if string_split_no_proc[j]==replacement[i]:
                    string_split_no_proc[j]=maillon_tab[i]
        return string_split_no_proc
