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
            aCounter = aCounter + x.count("a")
            aCounter = aCounter + x.count("à")
            aCounter = aCounter + x.count("á")
            aCounter = aCounter + x.count("â")
            aCounter = aCounter + x.count("ä")
            eCounter = eCounter + x.count("e")
            eCounter = eCounter + x.count("è")
            eCounter = eCounter + x.count("é")
            eCounter = eCounter + x.count("ë")
            eCounter = eCounter + x.count("ê")
            iCounter = iCounter + x.count("i")
            iCounter = iCounter + x.count("ì")
            iCounter = iCounter + x.count("í")
            iCounter = iCounter + x.count("ï")
            iCounter = iCounter + x.count("î")
            oCounter = oCounter + x.count("o")
            oCounter = oCounter + x.count("ò")
            oCounter = oCounter + x.count("ó")
            oCounter = oCounter + x.count("ô")
            oCounter = oCounter + x.count("ö")
            uCounter = uCounter + x.count("u")
            uCounter = uCounter + x.count("ù")
            uCounter = uCounter + x.count("ú")
            uCounter = uCounter + x.count("û")
            uCounter = uCounter + x.count("ü")
           
            
            
        
