import pygal
from pygal import Config
from pygal.style import Style


class ChartExporter:
    def __init__(self, labelData, data, title, outputFile):
        # Define variables to be used for chart creation
        # Use parameter values
        self.labelData = labelData
        self.data = data
        self.title = title
        self.outputFile = outputFile

        # Manage fix values
        self.style = Style(
            font_family="Sans-serif",
            label_font_size=20,
            major_label_font_size=20,
            title_font_size=20,
            tooltip_font_size=20
        )
        self.config = Config()
        self.config.show_legend = False
        self.config.human_readable = True
        self.config.fill = True
        self.config.height = self.config.width

    # Method to export chart (absolute numbers)
    def export(self):
        chart = pygal.Radar(config=self.config, style=self.style)
        chart.title = self.title
        chart.x_labels = self.labelData
        chart.add(self.title, self.data)
        chart.render_to_file(self.outputFile)
        # For testing purposes only
        # return "ChartExporter.export() works"

    # Method to export chart (percentages)
    def exportPercentage(self):
        self.config.show_legend = True
        chart = pygal.Pie(config=self.config, style=self.style)
        chart.title = self.title
        chart.x_labels = self.labelData
        barChartData = list(zip(self.labelData, self.data))
        for x in barChartData:
            chart.add(x[0], [x[1]])
        chart.render_to_file(self.outputFile)
        # For testing purposes only
        # return "ChartExporter.exportPercentage() works"
