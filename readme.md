
# FBVODRipper

This script will download VODs (up to 1080p) from Facebook.

This is JUST a wrapper for Youtube-DL, use that if you're comfortable with it.

-f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio

## Dependencies


```python
python 3.8.*
youtube-dl
facebook cookie
```

## Usage

**You will need to generate a cookies.txt file for Facebook and place it in this same directory.**
**You can use either of these plugins depending on if you're using [chrome](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg?hl=en) or [firefox](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/).**

Fill "list.txt" with links to Facebook VODs and then run "batch-videos.bat" to batch rip.

Run "single-video.bat" if you'd like to rip a single video.

It will download in the highest quality (1080p if the broadcaster streamed in that quality!)

Prior to the rewrite I was told Youtube-DL didn't support Facebook but that person was using an extremely outdated version of youtube-dl.
