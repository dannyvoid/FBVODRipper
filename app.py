import os,sys,shutil

vods_dir = "vods"

if not os.path.exists(vods_dir):
    os.makedirs(vods_dir)

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Facebook VOD URL: ")

videoid = url.split("/")[-2]

filename = f'%(resolution)s_{videoid}.%(ext)s'
os.system("title Scraping: "+url)

command = f"youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio --merge-output-format mp4 {url} -o {vods_dir}/{filename}"
os.system(command)

history_file = f"history.txt"
f = open(history_file, "a+") 
f.write(f"{videoid} - {url}\n")
f.close()
