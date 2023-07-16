from teiParser import TeiParser


def testTeiParser():
    teiParserObject = TeiParser(
        r"C:\Users\Resch\Documents\GitHub\vowel-analyzer\src\test\testData\DivinaCommedia.xml")
    print(teiParserObject.parse())
