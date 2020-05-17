from subprocess import Popen, PIPE
from os import getcwd
from platform import system

def exe(path):
    if system() == "Windows":
        command = 'py ' + getcwd() + r'\back.py ' + path
    elif system() == "Darwin" or system() == "Linux":
        command = 'python3 ' + getcwd() + r'/back.py ' + path
    
    stdout = Popen(command, shell=True, stdout=PIPE).stdout
    output = stdout.read()
    return output
