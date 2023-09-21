
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
    


    def split2(self, equ: list):
        for i in range(len(equ)):
            equ[i] = re.findall('[A-Z][^A-Z]*', equ[i])
            #print(equ[i*2])
        return(equ)
    
    def quant(self, halfEqu) -> dict:
        quantDict = {}
        for i in range (len(halfEqu)):
            for count in range (len(halfEqu[i])):
                element = halfEqu[i][count]
                try:
                    elementQuant = int(element[-1])
                    element = element[0 : -1]
                except:
                    elementQuant = 1
                if element in quantDict.keys():
                    quantDict[element] = quantDict[element] + elementQuant
                else:
                    quantDict[element] = elementQuant
        return quantDict



#useless function below  v
    def balance(self, reactant, product):
        
        start = reactant[0][0]
        try:
            startNum = int(start[-1])
            start = start[0 : -1]
        except:
            startNum = 1
        print(start)
        print(startNum)

        

             

            



solve = Chemistry("O2 + NHO3 -> HNO3 + H2O")
equ = solve.splitStep1(solve.equation)
reactant = solve.split2(equ[0])
product = solve.split2(equ[1])


print(reactant, " -> ", product)


reactantQuantities = solve.quant(reactant)
prodQuantities = solve.quant(product)
print(reactantQuantities)