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
           
            
            
        
