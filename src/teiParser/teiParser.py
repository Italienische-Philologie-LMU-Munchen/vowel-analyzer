
from lxml import etree


class TeiParser:
    def __init__(self, inputfile):
        # Define variables to be used for tei parsing
        # Use parameter values
        self.inputFile = inputfile

    # Method to extract text lines from TEI XML document
    def parse(self):
        # Get all lines from TEI XML document (<l>-Tag as line-tag for texts in verse)
        etreeText = etree.parse(self.inputFile)
        lines = etreeText.xpath("//l")
        textslines = []
        for x in lines:
            textslines.append(x.text)

        return textslines
