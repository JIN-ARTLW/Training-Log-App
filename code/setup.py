from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5', 'openpyxl'],
    'includes': [
        'sip',
        'PyQt5.sip',
        'PyQt5.QtCore',
        'PyQt5.QtWidgets'
    ],
    'iconfile': 'icon.icns',
    'frameworks': [
        '/usr/local/opt/libffi/lib/libffi.8.dylib',
        '/usr/local/Cellar/sqlite/3.49.1/lib/libsqlite3.dylib'
    ],
    'plist': {
        'CFBundleName': 'Training Log App',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'CFBundleIdentifier': 'com.example.traininglog',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
