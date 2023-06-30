from chartExporter import ChartExporter


def testChartExporter():
    chartExporterObject = ChartExporter([])
    print(chartExporterObject.export())
