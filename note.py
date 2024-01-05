import datetime
import os
import subprocess

def Note(data):
    date=datetime.datetime.now()
    filename=str(date).replace(':','-')+'-note.txt'
    a=os.getcwd()
    if not os.path.exists('Notes'):
        os.mkdir('Notes')
    os.chdir(a+r'\Notes')
    with open(filename,'w') as f:
        f.write(data)
    subprocess.Popen(['notepad.exe',filename])
    os.chdir(a)


