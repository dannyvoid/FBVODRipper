import os,sys,shutil

temp_dir = "temp"
complete_dir = "complete"

if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Facebook VOD URL: ")

filename = url.split("/")[-2]
os.system("title Scraping: "+filename)

command = f"youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio --merge-output-format mp4 {url} -o {temp_dir}/{filename}.mp4"
os.system(command)

if not os.path.exists(complete_dir):
    os.makedirs(complete_dir)

shutil.move(f"{temp_dir}/{filename}.mp4", f"{complete_dir}/{filename}.mp4")
shutil.rmtree(temp_dir)

history_file = f"{complete_dir}/history.txt"
f = open(history_file, "a+") 
f.write(f"{filename} -- {url}\n")
f.close()
