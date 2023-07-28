import re
class VowelCalculator:
    def __init__(self, text):
        self.text = text

    def calc(self):
        #return "VowelCalculator.calc() works"
        aCounter = 0
        eCounter = 0
        iCounter = 0
        oCounter = 0
        uCounter = 0
        for x in self.text:
            if isinstance(x, str):
                x = x.lower()
                aCounter += len(re.findall("[aàáäâ]", x))
                eCounter += len(re.findall("[eéèêë]", x))
                iCounter += len(re.findall("[iìíîï]", x))
                oCounter += len(re.findall("[oòóôö]", x))
                uCounter += len(re.findall("[uùúûü]", x))
               
               

        return [["A", "E", "I", "O", "U"], [aCounter, eCounter, iCounter, oCounter, uCounter]]
           
            
    def calcpercentage(self):
        #return "VowelCalculator.calc() works"
        aCounter = 0
        eCounter = 0
        iCounter = 0
        oCounter = 0
        uCounter = 0
        for x in self.text:
            if isinstance(x, str):
                x = x.lower()
                aCounter += len(re.findall("[aàáäâ]", x))
                eCounter += len(re.findall("[eéèêë]", x))
                iCounter += len(re.findall("[iìíîï]", x))
                oCounter += len(re.findall("[oòóôö]", x))
                uCounter += len(re.findall("[uùúûü]", x))
               
        overallcounter = aCounter + eCounter + iCounter + oCounter + uCounter
        aPercentage = aCounter * 100 / overallcounter 
        ePercentage = eCounter * 100 / overallcounter
        iPercentage = iCounter * 100 / overallcounter
        oPercentage = oCounter * 100 / overallcounter
        uPercentage = uCounter * 100 / overallcounter


        return [["A", "E", "I", "O", "U"], [aPercentage, ePercentage, iPercentage, oPercentage, uPercentage]]           
        
