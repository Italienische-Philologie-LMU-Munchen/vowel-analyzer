from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from teiParser import TeiParser
from vowelCalculator import VowelCalculator
from chartExporter import ChartExporter


class VowelAnalyzerGui(QMainWindow):
    def __init__(self):
        super().__init__()

        # Title of application window
        self.setWindowTitle("Vowel Analyzer")

        # Fixed geometry for startup of application
        self.setGeometry(0, 0, 600, 600)

        # Select file button
        self.btFileSelect = QPushButton("Select file", self)
        self.btFileSelect.clicked.connect(self.selectFile)
        # Analysis button
        self.btAnalysis = QPushButton("Run analysis", self)
        self.btAnalysis.clicked.connect(self.runAnalysis)
        # Output button
        self.btOutputDir = QPushButton("Select output", self)
        self.btOutputDir.clicked.connect(self.selectOutput)

        # Geometry of buttons
        self.btFileSelect.setGeometry(10, 10, 100, 40)
        self.btAnalysis.setGeometry(10, 55, 100, 40)
        self.btOutputDir.setGeometry(10, 100, 100, 40)

        # Webview to display result SVG
        self.wvResult = QWebEngineView(self)
        self.wvResult.setGeometry(120, 10, 500, 500)

        # Storage attributes for file handling
        self.filename = ''
        self.output = ''

    def selectFile(self):
        self.filename, filter = QFileDialog.getOpenFileName(self, 'Open file',
                                                            'c:\\', "XML files (*.xml)")

    def selectOutput(self):
        self.output = str(QFileDialog.getExistingDirectory(
            self, "Select Directory")) + '/output.svg'
        self.output = self.output

    def runAnalysis(self):
        if self.filename != '' and self.output != '':
            teiParserObject = TeiParser(self.filename)
            vowelCalcObject = VowelCalculator(teiParserObject.parse())
            vowelResult = vowelCalcObject.calc()
            chartExporterObject = ChartExporter(
                vowelResult[0], vowelResult[1], self.filename, self.output)
            chartExporterObject.export()

            self.wvResult.load(QUrl(self.output))


def main():
    app = QApplication([])
    window = VowelAnalyzerGui()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
