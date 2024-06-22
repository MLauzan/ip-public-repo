import math

def pagesQuantity(imagesQuantity):
    pages = imagesQuantity/ 5
    if pages > 2000:
        pages = 2000
        
    return math.ceil(pages)

def getPreviousPages(numero):
    numeros_antecesores = []
    for i in range(numero - 1, 1, -1):
        if i > 1 and len(numeros_antecesores) < 5:
            numeros_antecesores.append(i)
    if not numeros_antecesores:
        return None
    return numeros_antecesores[::-1]

def getNextPages(numero_actual, limite_superior):
    numeros_proximos = []
    for i in range(numero_actual + 1, limite_superior):
        numeros_proximos.append(i)
        if len(numeros_proximos) >= 5:
            break
    
    return numeros_proximos
