import os,sys,shutil
from youtube_dl import YoutubeDL

vods_dir = "vods"

if not os.path.exists(vods_dir):
    os.makedirs(vods_dir)

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Facebook VOD URL: ")

youtube_dl_opts = {}
video = url

with YoutubeDL(youtube_dl_opts) as ydl:
      info_dict = ydl.extract_info(video, download=False)
      video_url = info_dict.get("url", None)
      video_id = info_dict.get("id", None)
      upload_date = info_dict.get("upload_date", None)
      timestamp = info_dict.get("timestamp", None)

while upload_date is None:
    try:
        youtube_dl_opts = {}
        video = "https://www.facebook.com/arigameplays/videos/334728620980663/"
        with YoutubeDL(youtube_dl_opts) as ydl:
            info_dict = ydl.extract_info(video, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            upload_date = info_dict.get("upload_date", None)
            timestamp = info_dict.get("timestamp", None)
    except:
        pass

while timestamp is None:
    try:
        youtube_dl_opts = {}
        video = "https://www.facebook.com/arigameplays/videos/334728620980663/"
        with YoutubeDL(youtube_dl_opts) as ydl:
            info_dict = ydl.extract_info(video, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            upload_date = info_dict.get("upload_date", None)
            timestamp = info_dict.get("timestamp", None)
    except:
        pass

filename = f'{upload_date}_{timestamp}_%(resolution)s.%(ext)s'
os.system("title Scraping: "+url)

command = f"youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio --merge-output-format mp4 {url} -o {vods_dir}/{filename}"
os.system(command)

history_file = f"history.txt"
f = open(history_file, "a+") 
f.write(f"{upload_date} - {timestamp} - {url}\n")
f.close()
