
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
        return equ
    
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
                            bigNum = float(halfEqu[i-1])
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


    def balance(self, firstQuant, secQuant, count):
        
        start = list(firstQuant.keys())[count]
        startQR = firstQuant[start]       
        startQP = secQuant[start]
        bal = startQP/startQR
        rOrP = "r"
        if bal != int(bal):
            newBal = startQR/startQP
            if len(str(bal)) > len(str(newBal)):
                rOrP = "p"
                print(newBal)
                return (newBal, rOrP)
        print(bal)
        return (bal, rOrP)
        
    def addToEqu(self, loc, numToAdd, equ, quant):        
        firstCount = 0
        print("location" , loc)
        if numToAdd != 1:
            loc = list(quant.keys())[loc]
            print("location" , loc)
            while firstCount < (len(equ)): 
                try:
                    int(equ[firstCount])
                    print("yes")
                except:
                    print("string")             
                    for n in range (len(equ[firstCount])):
                        print("hello")
                        print(equ[firstCount][n])
                        if loc in equ[firstCount][n]:
                            location = firstCount
                            try:     
                                numToAdd = numToAdd * float(equ[firstCount-1])
                                print("numToAdd", numToAdd)
                                equ[firstCount-1] = numToAdd
                            except TypeError:
                                print("inserting...")
                                equ.insert(location, numToAdd)
                                firstCount += 1
                            except:
                                print("othre error")
                firstCount += 1
        return equ

    def reconHalfEqu(self, halfEqu):
        for i in range (len(halfEqu)):
            try:
                halfEqu[i] = "".join(map(lambda x:x, halfEqu[i]))
            except:
                pass
        return halfEqu
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

#print("O2 + NH3 -> HNO3 + H2O")
"O2 -> O3"
#"H2O2 -> H2O + O2"

#equation = input()
solve = Chemistry("H2O + O2 -> H2O2")
equ = solve.splitStep1(solve.equation)
reactant = solve.splitStep2(equ[0])
product = solve.splitStep2(equ[1])

print(reactant, " -> ", product)

count = 0
totalCount = 0
reactantQuantities = solve.quant(reactant)
prodQuantities = solve.quant(product)
print(reactantQuantities)
print(prodQuantities)

isBalanced = True
if reactantQuantities != prodQuantities:
    isBalanced = False

while isBalanced == False and totalCount < 10:
    print(count)
    #print(int(count/len(reactantQuantities)) % 2)
    #print(len(reactantQuantities))
    bigNum = solve.balance(reactantQuantities, prodQuantities, count)
    if bigNum[1] == "r":
        print("reactant")
        reactant = solve.addToEqu(count, bigNum[0], reactant, reactantQuantities)
        print(reactant)
        reactantQuantities = solve.quant(reactant)
        print(reactantQuantities)
    elif bigNum[1] == "p":
        print(product)
        product = solve.addToEqu(count, bigNum[0], product, prodQuantities)
        prodQuantities = solve.quant(product)

    count += 1
    totalCount += 1
    
    if count == len(reactantQuantities):
        count = 0

    if reactantQuantities == prodQuantities:
        isBalanced = True
        print("Balanced")

reactant = solve.reconHalfEqu(reactant)
product = solve.reconHalfEqu(product)
print(reactant , "->" , product)