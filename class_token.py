#-*-coding:Utf-8 -*

from class_useful_objects import *
import re

class Token:
    pass

class OperateurUnitaire(Token):
    """Classe des opérateurs unitaires, comportement: empile"""

    def __init__(self, string):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur unitaire"""
        b=0
        try:
            b=int(self.string)
            stack.append(b)
        except:
            if self.string=="true":
                b="true"
            else:
                b="false"
            stack.append(b)
        return stack, dico_function


class OperateurBinaire(Token):
    """Classe des opérateurs binaires, comportement: dépile, dépile, appel à la méthode opération, empile"""

    def __init__(self, string):
        self._associated_number=2
        self.string=string

    def _get_associated_number(self):
        """Méthode permettant d'accéder au nombre caractéristique de cette classe. L'utilisation de propriétés permet de ne pas modifier cette attribut"""
        return self._associated_number

    associated_number=property(_get_associated_number)

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur binaire"""
        terms=stack.pop(self.associated_number)
        if self.string=="add":
            stack.append(terms[0]+terms[1])
        elif self.string=="sub":
            stack.append(terms[0]-terms[1])
        elif self.string=="mul":
            stack.append(terms[0]*terms[1])
        elif self.string=="idiv":
            stack.append(terms[0]//terms[1])
        elif self.string=="eq":
            if terms[0]==terms[1]:
                stack.append("true")
            else:
                stack.append("false")
        elif self.string=="ne":
            if terms[0]!=terms[1]:
                stack.append("true")
            else:
                stack.append("false")
        elif self.string=="lt":
            if terms[0]<terms[1]:
                stack.append("true")
            else:
                stack.append("false")
        elif self.string=="le":
            if terms[0]<=terms[1]:
                stack.append("true")
            else:
                stack.append("false")
        elif self.string=="gt":
            if terms[0]>terms[1]:
                stack.append("true")
            else:
                stack.append("false")
        elif self.string=="ge":
            if terms[0]>=terms[1]:
                stack.append("true")
            else:
                stack.append("false")
        elif self.string=="if": 
            if terms[0]=="true": 
                """On regarde si la procédure indiquée est vide"""
                if re.match("({)\s*?(})",terms[1]):
                    """La procédure est-elle vide ?"""
                    pass
                else:
                    procedure=terms[1].lstrip("{")
                    procedure=procedure.rstrip("}")
                    procedure=Instruction(procedure)
                    procedure=procedure.split_instruction()
                    for i in range(len(procedure)):
                        stack.append(procedure[i])
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
            elif terms[0]=="false":
                pass
            else:
                print("Syntax error: if lacks a term")
        else:
            print("Ce n'est pas un opérateur binaire")
        return stack, dico_function


class OperateurTernaire(Token):
    """Classe des opérateurs ternaires, comportement: dépile, dépile, dépile, appel à la méthode opération, empile"""

    def __init__(self, string):
        self._associated_number=3
        self.string=string

    def _get_associated_number(self):
        """Méthode permettant d'accéder au nombre caractéristique de cette classe. L'utilisation de propriétés permet de ne pas modifier cette attribut"""
        return self._associated_number

    associated_number=property(_get_associated_number)

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur ternaire"""
        terms=stack.pop(self.associated_number)
        if self.string=="ifelse":
            if terms[0]=="true": 
                if re.match("({)\s*?(})",terms[1]):
                    """La procédure est-elle vide ?"""
                    pass
                else:
                    procedure=terms[1].lstrip("{")
                    procedure=procedure.rstrip("}")
                    procedure=Instruction(procedure)
                    procedure=procedure.split_instruction()
                    for i in range(len(procedure)):
                        stack.append(procedure[i])
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
            elif terms[0]=="false":
                if re.match("({)\s*?(})",terms[2]):
                    """La procédure est-elle vide ?"""
                    pass
                else:
                    procedure=terms[2].lstrip("{")
                    procedure=procedure.rstrip("}")
                    procedure=Instruction(procedure)
                    procedure=procedure.split_instruction()
                    for i in range(len(procedure)):
                        stack.append(procedure[i])
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
            else:
                print("Syntax error: ifelse lacks a term")
        return stack, dico_function


class OperateurQuaternaire(Token):
    """Classe des opérateurs quaternaires, comportement: dépile, dépile, dépile, dépile, appel à la méthode opération, empile"""

    def __init__(self, string):
        self._associated_number=4
        self.string=string

    def _get_associated_number(self):
        """Méthode permettant d'accéder au nombre caractéristique de cette classe. L'utilisation de propriétés permet de ne pas modifier cette attribut"""
        return self._associated_number

    associated_number=property(_get_associated_number)

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'un operateur quaternaire"""
        terms=stack.pop(self.associated_number)
        if self.string=="for":
            if re.match("({)\s*?(})",terms[3]):
                """La procédure est-elle vide ?"""
                for i in range(terms[0],terms[2]+1,terms[1]):
                    stack.append(i)
            else:
                for i in range(terms[0],terms[2]+1,terms[1]):
                    stack.append(i)
                    procedure=terms[3].lstrip("{")
                    procedure=procedure.rstrip("}")
                    procedure=Instruction(procedure)
                    procedure=procedure.split_instruction()
                    for i in range(len(procedure)):
                        stack.append(procedure[i])
                    liste=inter_list_partielle(stack, dico_function)
                    stack=Stack(liste[0])
        else:
            print("Syntax error: for lacks a term")
        return stack, dico_function


class Name(Token):

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        if self.string[0]=="/":
            stack.append(self.string)
        else:
            if dico_function.get(self.string)!=None:
                procedure=dico_function[self.string]
                procedure=procedure.lstrip("{")
                procedure=procedure.rstrip("}")
                procedure=Instruction(procedure)
                procedure=procedure.split_instruction()
                for i in range(len(procedure)):
                    stack.append(procedure[i])
                liste=inter_list_partielle(stack, dico_function)
                stack=Stack(liste[0])
            else:
                print("Syntax error: terms not recognized")        
        return stack, dico_function


class Procedure(Token):

    def __init__(self, string):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'une procédure"""
        stack.append(self.string)
        return stack, dico_function


class Def(Token):

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        """Réalise le comportement d'une procédure"""
        if re.search("^(/)\w*$",get_previous_token(stack,i-1))!=None and get_previous_token(stack,i)[0]=="{":
            dico_function[get_previous_token(stack,i-1).lstrip("/")]=get_previous_token(stack,i)
            stack.pop(2)
        else:
            pass
        return stack, dico_function


class Dup(Token):

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        stack.dup()
        return stack, dico_function


class Exch(Token):

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        stack.exch()
        return stack, dico_function


class Pop(Token):

    def __init__(self, string, i=0, dico_function={}):
        self.string=string

    def operation(self, stack, i=0, dico_function={}):
        stack.pop_element()
        return stack, dico_function

def get_previous_token(instruc_stack, old_token_index=-1):
    try:
        previous_one=instruc_stack.liste[old_token_index-1]
        return previous_one
    except:
        print("Syntax error: no function to define")


def get_type(token):
    if token in ["true","false"]:
        token=OperateurUnitaire(token)
        return token
    elif re.search("^\d*[.,]?\d*$",str(token))!=None:
        try:
            b=int(token)
            token=OperateurUnitaire(token)
            return token
        except:
            pass
    elif token in ["add","sub", "mul", "idiv", "eq", "ne", "lt", "le", "gt", "ge", "if"]:
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
    elif token[0]=="{":
        token=Procedure(token)
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
    tab_instruction=stack.liste
    n=len(tab_instruction)
    pile=Stack([])
    L=[]
    for i in range(n):
        tab_instruction[i]=get_type(tab_instruction[i])
        pile, dico_function=tab_instruction[i].operation(pile, i, dico_function)
    L.append(pile.liste)
    L.append(dico_function)
    return L
