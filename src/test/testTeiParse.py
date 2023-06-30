from teiParser import TeiParser


def testTeiParser():
    teiParserObject = TeiParser(
        "VowelAnalyzer/test/testData/DivinaCommedia.xml")
    print(teiParserObject.parse())
