
# input equation like this: O2 + NH3 -> HNO3 + H2O

import re

def splitStep1(equation: str) -> str:

    reactant = equation.split(" -> ")[0]
    product = equation.split(" -> ")[1]
    listR = reactant.split()
    listP = product.split()

    return [listR, listP]
    


def split2(equ: list):
    for i in range(int((len(equ) + 1)/2)):
        equ[i*2] = re.findall('[A-Z][^A-Z]*', equ[i*2])
        #print(equ[i*2])
    return(equ)

            




equ = splitStep1("O2 + NH3 -> HNO3 + H2O")
reactant = split2(equ[0])
product = split2(equ[1])

print(reactant, " -> ", product)

