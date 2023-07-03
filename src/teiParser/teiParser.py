
from lxml import etree


class TeiParser:
    def __init__(self, inputfile):
        self.inputFile = inputfile

    def parse(self):
        etreeText = etree.parse(self.inputFile)
        lines = etreeText.xpath("//l")
        textslines = []
        for x in lines: 
            textslines.append(x.text)
        #print(textslines)
        return textslines



