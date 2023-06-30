from tableExporter import TableExporter


def testTableExporter():
    tableExporterObject = TableExporter([])
    print(tableExporterObject.export())
