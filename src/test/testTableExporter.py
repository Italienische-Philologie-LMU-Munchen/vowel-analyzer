from tableExporter import TableExporter


def testTableExporter():
    tableExporterObject = TableExporter(["A", "E", "I", "O", "U"], [[10, 10, 20, 14, 7]], "export/test.csv")
    print(tableExporterObject.export())
