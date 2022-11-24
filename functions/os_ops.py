import os
import subprocess as sp

paths = {
    'microsoftword': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk",
    'vscode': "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_microsoftword():
    os.startfile(paths['microsoftword'])


def open_vscode():
    os.startfile(paths['vscode'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.open(paths['calculator'])
