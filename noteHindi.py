import datetime
import os
import subprocess

def note(data):
    if data == "none":
        return
    date = datetime.datetime.now()
    filename = str(date).replace(':','-')+'-note.txt'
    folder_path = os.path.join(os.getcwd(), 'Notes')
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)
    subprocess.Popen(['notepad.exe', file_path])