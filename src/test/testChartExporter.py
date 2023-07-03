from chartExporter import ChartExporter


def testChartExporter():
    chartExporterObject = ChartExporter(["A", "E", "I", "O", "U"], [20, 12, 45, 18, 7], "Test")
    print(chartExporterObject.export())
