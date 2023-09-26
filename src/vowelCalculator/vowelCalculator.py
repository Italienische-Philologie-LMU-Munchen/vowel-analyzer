import re


class VowelCalculator:
    def __init__(self, text):
        # Define variables to be used for table creation
        # Use parameter values
        self.text = text

    # Method to calculate absolute numbers of vowels in given text
    def calc(self):
        # Define counter variables
        aCounter = 0
        eCounter = 0
        iCounter = 0
        oCounter = 0
        uCounter = 0
        # Go through all lines of text and count vowels if we have a string (avoid undefined error)
        # Use regex to count vowels with diacritics as we consider vowels with diacritics as 'normal' vowels
        for x in self.text:
            if isinstance(x, str):
                x = x.lower()
                aCounter += len(re.findall("[aàáäâ]", x))
                eCounter += len(re.findall("[eéèêë]", x))
                iCounter += len(re.findall("[iìíîï]", x))
                oCounter += len(re.findall("[oòóôö]", x))
                uCounter += len(re.findall("[uùúûü]", x))

        # For testing purposes only
        # return "VowelCalculator.calc() works"

        # Return result matrix
        return [["A", "E", "I", "O", "U"], [aCounter, eCounter, iCounter, oCounter, uCounter]]

    # Method to calculate percentages of vowels in given text

    def calcpercentage(self):
        # Define counter variables
        aCounter = 0
        eCounter = 0
        iCounter = 0
        oCounter = 0
        uCounter = 0
        # Go through all lines of text and count vowels if we have a string (avoid undefined error)
        # Use regex to count vowels with diacritics as we consider vowels with diacritics as 'normal' vowels
        for x in self.text:
            if isinstance(x, str):
                x = x.lower()
                aCounter += len(re.findall("[aàáäâ]", x))
                eCounter += len(re.findall("[eéèêë]", x))
                iCounter += len(re.findall("[iìíîï]", x))
                oCounter += len(re.findall("[oòóôö]", x))
                uCounter += len(re.findall("[uùúûü]", x))

        # Calculate percentages using overall number of vowels as reference
        overallcounter = aCounter + eCounter + iCounter + oCounter + uCounter
        aPercentage = aCounter * 100 / overallcounter
        ePercentage = eCounter * 100 / overallcounter
        iPercentage = iCounter * 100 / overallcounter
        oPercentage = oCounter * 100 / overallcounter
        uPercentage = uCounter * 100 / overallcounter

        # For testing purposes only
        # return "VowelCalculator.calc() works"

        # Return result matrix
        return [["A", "E", "I", "O", "U"], [aPercentage, ePercentage, iPercentage, oPercentage, uPercentage]]
