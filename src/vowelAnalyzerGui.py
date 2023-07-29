import os
import tempfile
from shutil import copyfile
from pathlib import Path
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QCheckBox
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
        self.btOutputDir = QPushButton("Export SVG", self)
        self.btOutputDir.clicked.connect(self.export)
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
        self.filepath = ''
        self.filename = ''
        self.output = ''

        # Create temp folder if not existing
        self.temppath = Path(tempfile.gettempdir()) / "VowelAnalyzer"
        self.temppath.mkdir(parents=True, exist_ok=True)

    def selectFile(self):
        baseDirectory = str(Path.home() / 'Desktop')
        self.filepath, filter = QFileDialog.getOpenFileName(self, 'Open file',
                                                            baseDirectory, "XML files (*.xml)")
        self.filename = os.path.splitext(os.path.basename(self.filepath))[0]

    def export(self):
        self.output = Path(str(QFileDialog.getExistingDirectory(
            self, "Select Directory")))
        copyfile(str(self.temppath / (self.filename + '.svg')),
                 str(self.output / (self.filename + '.svg')))

    def runAnalysis(self):
        if self.filepath != '':
            teiParserObject = TeiParser(self.filepath)

            vowelCalcObject = VowelCalculator(teiParserObject.parse())
            if (self.cbPercentage.isChecked()):
                vowelResult = vowelCalcObject.calcpercentage()
            else:
                vowelResult = vowelCalcObject.calc()

            chartExporterObject = ChartExporter(
                vowelResult[0], vowelResult[1], self.filename, str(self.temppath / (self.filename + '.svg')))
            if (self.cbPercentage.isChecked()):
                chartExporterObject.exportPercentage()
            else:
                chartExporterObject.export()

            self.wvResult.load(
                QUrl("file:"+(self.temppath / (self.filename + '.svg')).as_posix()))

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
