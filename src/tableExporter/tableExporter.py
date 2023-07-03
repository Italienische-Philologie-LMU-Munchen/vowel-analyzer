import csv

class TableExporter:
    def __init__(self, lableData, data, outputFile):
        self.data = data
        self.lableData = lableData
        self.outputFile = outputFile

    def export(self):
        with open(self.outputFile, 'w', newline='') as file:
            # Manage CSV writer settings
            csv.register_dialect("custom", delimiter=";", skipinitialspace=True)
            writer = csv.writer(file, dialect="custom")

             # Write headline
            writer.writerow(self.lableData)

            for x in self.data:
                writer.writerow(x)

        return "TableExporter.export() works"
