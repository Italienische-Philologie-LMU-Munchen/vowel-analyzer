import pygal
from pygal import Config
from pygal.style import Style

class ChartExporter:
    def __init__(self, labelData, data, title):
        self.labelData = labelData
        self.data = data
        self.title = title

        self.style = Style(
            font_family = "Sans-serif",
            label_font_size = 20,
            major_label_font_size = 20,
            title_font_size = 20,
            tooltip_font_size = 20
        )

        self.config = Config()
        self.config.show_legend = False
        self.config.human_readable = True
        self.config.fill = True
        self.config.height = self.config.width

    def export(self):
        chart = pygal.Radar(config=self.config, style=self.style)
        chart.title = self.title
        chart.x_labels = self.labelData
        chart.add(self.title, self.data)
        chart.render_to_file("export/test.svg")
        return "ChartExporter.export() works"
