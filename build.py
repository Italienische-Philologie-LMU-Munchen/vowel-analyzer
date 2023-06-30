import os
import sys
import venv
import subprocess
import PyInstaller.__main__

# Source: https://stackoverflow.com/questions/12332975/how-can-i-install-a-python-module-within-code
# Source: https://stackoverflow.com/questions/46056557/python-script-to-activate-and-keep-open-a-virtualenv


def isvirtualenv():
    return sys.prefix != sys.base_prefix


def findfile(startdir, pattern):
    for root, dirs, files in os.walk(startdir):
        for name in files:
            if name.find(pattern) >= 0:
                return root + os.sep + name

    return None


def install(reqPath):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", reqPath])


venv_path = 'venv_vowelanalyzer'
requirements_path = os.path.join(os.getcwd(), "requirements.txt")

if isvirtualenv():
    print('Already in virtual environment.')
else:
    if findfile(os.getcwd(), 'activate') is None:
        print('No virtual environment found. Creating one.')
        env = venv.EnvBuilder(with_pip=True)
        env.create(venv_path)
    else:
        print('Not in virtual environment. Virtual environment directory found.')

    # This is the heart of this script that puts you inside the virtual environment.
    # There is no need to undo this. When this script ends, your original path will
    # be restored.
    os.environ['PATH'] = os.path.dirname(
        findfile(os.getcwd(), 'activate')) + os.pathsep + os.environ['PATH']
    sys.path.insert(1, os.path.dirname(findfile(venv_path, 'easy_install.py')))

# Run your script inside the virtual environment from here
install(requirements_path)

PyInstaller.__main__.run([
    'src/vowelAnalyzer.py',
    '--onefile',
    '--console'
])
