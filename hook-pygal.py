# From https://github.com/Kozea/pygal/issues/182 to make pygal work with PyInstaller

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('pygal')
