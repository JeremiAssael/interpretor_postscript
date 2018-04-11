from class_token import *
from class_useful_objects import *


def inter(instruction, dico_function):
    instr=Instruction(instruction)
    tab_instruction=instr.split_instruction()
    pile=Stack([])
    L=[]
    for i in range(len(tab_instruction)):
        if tab_instruction[i]!="{" and tab_instruction[i]!="}":
            tab_instruction[i]=get_type(tab_instruction[i])
    """tous les éléments de notre instruction, quels qu'ils soient ont été transtypés"""
    tab_instruction=split_tot(tab_instruction)   
    tab_instruction=conv_procedure(tab_instruction)
    for i in range(len(tab_instruction)):
        pile, dico_function=tab_instruction[i].operation(pile, i, dico_function)
    L.append(pile)
    L.append(dico_function)
    return L


def conv_procedure(liste):
    for i in range(len(liste)):
        if type(liste[i]) is list:
            conv_procedure(liste[i])
            liste[i]=Procedure(liste[i])
    return liste



dico_function={}
instruction=input(">>>")
liste=[]
pile=[]
while instruction!="exit":
    liste=inter(instruction, dico_function)
    print(liste[0].print_stack())
    dico_function=liste[1]
    print(dico_function)
    instruction=input(">>>")



