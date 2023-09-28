
# input equation like this: O2 + NH3 -> HNO3 + H2O

import re

class Chemistry:
    def __init__(self, equation: str) -> None:
        self.equation = equation

    def splitStep1(self, equation: str) -> str:
        reactant = equation.split(" -> ")[0]
        product = equation.split(" -> ")[1]
        listR = reactant.split(" + ")
        listP = product.split(" + ")

        return [listR, listP]
    


    def splitStep2(self, equ: list):
        for i in range(len(equ)):
            equ[i] = re.findall('[A-Z][^A-Z]*', equ[i])
            #print(equ[i*2])
        return(equ)
    
    def quant(self, halfEqu) -> dict:
        quantDict = {}
        for i in range (len(halfEqu)):
            try:
                for count in range (len(halfEqu[i])):             
                    element = halfEqu[i][count] 
                    try:
                        elementQuant = int(element[-1])
                        element = element[0 : -1]
                    except:
                        elementQuant = 1
                    if i > 0:
                        try:
                            bigNum = int(halfEqu[i-1])
                            elementQuant = elementQuant * bigNum
                        except:
                            pass
                    if element in quantDict.keys():    
                        quantDict[element] = quantDict[element] + elementQuant
                    else:        
                        quantDict[element] = elementQuant
                
            except:
                pass
        return quantDict


    def balance(self, reactantQuant, productQuant, count):
        
        start = list(reactantQuant.keys())[count]
        startQR = reactantQuant[start]       
        startQP = productQuant[start]
        bal = startQP/startQR
        return bal
        
    def addToEqu(self, loc, num, equ):
        equ.insert(loc, num)

    def reconHalfEqu(self, halfEqu):
        for i in range (len(halfEqu)):
            try:
                halfEqu[i] = "".join(map(lambda x:x, halfEqu[i]))             
            except:
                pass
        return(halfEqu)
'''
    def reconFullHalf(self, halfEqu):
        for i in range(len(halfEqu)-1):
            try:
                int(halfEqu[i])
                halfEqu[i] = "".join(map(lambda x:x, halfEqu[i]))
            except:
                pass
'''       

          
#splitting equation into computable format

print("O2 + NH3 -> HNO3 + H2O")
solve = Chemistry("O2 + NH3 -> HNO3 + H2O")
equ = solve.splitStep1(solve.equation)
reactant = solve.splitStep2(equ[0])
product = solve.splitStep2(equ[1])

print(reactant, " -> ", product)

count = 0
reactantQuantities = solve.quant(reactant)
prodQuantities = solve.quant(product)
print(reactantQuantities)
print(prodQuantities)

if reactantQuantities != prodQuantities:
    isBalanced = False

while isBalanced == False :
    bigNum = solve.balance(reactantQuantities, prodQuantities, count)
    solve.addToEqu(count, bigNum, reactant)
    print(reactant)
    reactantQuantities = solve.quant(reactant)
    print(reactantQuantities)

    count += 1
    if reactantQuantities == prodQuantities:
        isBalanced = True

reactant = solve.reconHalfEqu(reactant)
product = solve.reconHalfEqu(product)
print(reactant , "->" , product)