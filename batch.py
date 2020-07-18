import os

list = "list.txt"

with open(list) as links:
    for line in links:
        line = line.strip("\n")
        line = line.strip("\t")

        command = f"python app.py {line}"
        os.system(command)
        os.system("cls")
