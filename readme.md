# FB VOD Ripper

This script will download VODs (up to 1080p) from Facebook.

This is JUST a wrapper for Youtube-DL, use that if you're comfortable with that.

The flag to obtain highest quality on facebook is bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio

## Dependencies


```python
python
youtube-dl
```

## Usage

Fill list.txt with links to Facebook VODs and then run "batch-videos.bat" to batch rip

Just run "single-video.bat" if you'd like to rip a single video.

It will download in the highest quality (1080p if the broadcaster streamed in that quality!)

I was told Youtube-DL didn't support this, but I spent 2 seconds finding the flags to grab the highest quality.
