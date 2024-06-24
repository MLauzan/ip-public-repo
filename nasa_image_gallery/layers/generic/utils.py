import math

def pagesQuantity(imagesQuantity):
    pages = imagesQuantity/ 5
    if pages > 2000:
        pages = 2000
        
    return math.ceil(pages)

def getPreviousPages(number):
    previousNumbers = []
    for i in range(number - 1, 1, -1):
        if i > 1 and len(previousNumbers) < 5:
            previousNumbers.append(i)
    if not previousNumbers:
        return None
    return previousNumbers[::-1]

def getNextPages(number, limit):
    nextNumbers = []
    for i in range(number + 1, limit):
        nextNumbers.append(i)
        if len(nextNumbers) >= 5:
            break
    
    return nextNumbers















