
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
                return newBal
        print(bal)
        return bal
        
    def addToEqu(self, loc, numToAdd, equ, quant):        
        print("location" , loc)
        if numToAdd != 1:
            loc = list(quant.keys())[loc]
            print("location" , loc)
            for i in range (len(equ)):              
                for n in range (len(equ[i])):
                    print("hello")
                    print(equ[i][n])
                    if loc in equ[i][n]:
                        print("hi")
                        location = i
                        try:                    
                            numToAdd = numToAdd * float(equ[i-1])
                            print("numToAdd", numToAdd)
                            equ[i-1] = numToAdd
                        except TypeError: 
                            print("type error")                     
                            equ.insert(location, numToAdd)
                            return equ
                        except:
                            print("othre error")
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
#"H2O2 -> H2O + O2"

#equation = input()
solve = Chemistry("O2 + NH3 -> HNO3 + H2O")
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
    newEquation = solve.addToEqu(count, bigNum, reactant, reactantQuantities)
    reactantQuantities = solve.quant(newEquation)

    '''
    if int(count/len(reactantQuantities)) % 2 == 0:
        bigNum = solve.balance(reactantQuantities, prodQuantities, count)
        solve.addToEqu(count, bigNum, reactant, reactantQuantities)
        print(reactant)
        reactantQuantities = solve.quant(reactant)
        print(reactantQuantities)
    else:
        bigNum = solve.balance(prodQuantities, reactantQuantities, count)
        solve.addToEqu(count, bigNum, product, prodQuantities)
        print(product)
        reactantQuantities = solve.quant(product)
        print(prodQuantities)
    '''
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