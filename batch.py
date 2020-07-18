import os,os.path
from os import path

list = "list.txt"

with open(list) as links:
    for line in links:
        line = line.strip('\n')
        line = line.strip('\t')

        filename = line.split("/")[-2]

        if path.exists(f"complete/{filename}.mp4"):
            os.system('cls')
            continue
        else:
            command = f"python app.py {line}"
            os.system(command)
            os.system('cls')
