from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QCheckBox, QSizePolicy
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
        # Percentage toggle
        self.cbPercentage = QCheckBox("Calculate\r\npercentages", self)

        # Geometry of buttons
        self.btFileSelect.setGeometry(10, 10, 100, 40)
        self.btAnalysis.setGeometry(10, 55, 100, 40)
        self.btOutputDir.setGeometry(10, 100, 100, 40)
        self.cbPercentage.setGeometry(10, 145, 100, 40)

        # Webview to display result SVG
        self.wvResult = QWebEngineView(self)
        self.wvResult.setGeometry(
            120, 10, self.width() - 150, self.height() - 50)

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
            if (self.cbPercentage.isChecked()):
                vowelResult = vowelCalcObject.calcpercentage()
            else:
                vowelResult = vowelCalcObject.calc()

            chartExporterObject = ChartExporter(
                vowelResult[0], vowelResult[1], self.filename, self.output)
            if (self.cbPercentage.isChecked()):
                chartExporterObject.exportPercentage()
            else:
                chartExporterObject.export()

            self.wvResult.load(QUrl("file:"+self.output))

    def resizeEvent(self, event):
        self.wvResult.setGeometry(
            120, 10, self.width() - 150, self.height() - 50)
        QMainWindow.resizeEvent(self, event)


def main():
    app = QApplication([])
    window = VowelAnalyzerGui()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
