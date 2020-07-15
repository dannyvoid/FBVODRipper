# FB VOD Ripper

This script will download VODs from Facebook.

## Dependencies


```python
requests==2.22.0
beautifulsoup4==4.9.1
ffmpeg
```

## Usage

Just run start.bat and go from there.

start.bat requires python 3 at least, I made this using 3.8.1

merge.bat requires ffmpeg be installed somewhere in your environment

## Current state of this
This was all poorly made in about 5-10 minutes.

There's no validation for anything, we have useless temp files to determine the biggest file to get the highest quality video file, and we don't even handle incomplete downloads!

We even rely on a 3rd party to parse Facebook for the links to download. 

(since it was the quickest way to go about it, since I made this for someone who needed it quickly)

Feel free to submit a pull request if you'd like to clean this up and maybe help take away the 3rd party reliance.
