
# FBVODRipper

This script will download VODs (up to 1080p) from Facebook.

This is JUST a wrapper for Youtube-DL, use that if you're comfortable with it.

-f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio

## Dependencies


```python
python 3.8.*
youtube-dl via pip
```

## Usage

***a lot of redundant loops/checks since i discovered facebook is unreliable at giving upload_date and timestamp, but can't be bothered to clean. someone needed a quick fix. feel free to clean and submit a pr***

Fill "list.txt" with links to Facebook VODs and then run "batch-videos.bat" to batch rip.

Run "single-video.bat" if you'd like to rip a single video.

It will download in the highest quality (1080p if the broadcaster streamed in that quality!)

Prior to the rewrite I was told Youtube-DL didn't support Facebook but that person was using an extremely outdated version of youtube-dl.
