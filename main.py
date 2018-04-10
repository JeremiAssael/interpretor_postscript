from class_token import *
from class_useful_objects import *



"""def inter(instruction, dico_function):
    instr=Instruction(instruction)
    tab_instruction=instr.split_instruction()
    n=len(tab_instruction)
    pile=Stack([])
    L=[]
    for i in range(n):
        tab_instruction[i]=get_type(tab_instruction[i])
        pile, dico_function=tab_instruction[i].operation(pile, i, dico_function)
    L.append(pile)
    L.append(dico_function)
    return L



dico_function={}
instruction=input(">>>")
liste=[]
pile=[]
while instruction!="exit":
    liste=inter(instruction, dico_function)
    print(liste[0].print_stack())
    dico_function=liste[1]
    print(dico_function)
    instruction=input(">>>")"""


def inter(instruction, pile, dico_function):
    instr=Instruction(instruction)
    tab_instruction=instr.split_instruction()
    n=len(tab_instruction)
    L=[]
    for i in range(n):
        tab_instruction[i]=get_type(tab_instruction[i])
        pile, dico_function=tab_instruction[i].operation(pile, i, dico_function)
    L.append(pile)
    L.append(dico_function)
    return L



dico_function={}
instruction=input(">>>")
liste=[]
pile=Stack([])
while instruction!="exit":
    liste=inter(instruction, pile, dico_function)
    print(liste[0].print_stack())
    pile=liste[0]
    dico_function=liste[1]
    print(dico_function)
    instruction=input(">>>")



"""dico_function={}
instruction=input(">>>")
liste=[]
pile=[]
while instruction!="exit":
    try:
        liste=inter(instruction, dico_function)
        print(liste[0].print_stack())
        dico_function=liste[1]
        print(dico_function)
        instruction=input(">>>")
    except:
        instruction=input(">>>")"""

