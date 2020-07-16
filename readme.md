# FB VOD Ripper

This script will download VODs (up to 1080p) from Facebook.

## Dependencies


```python
requests==2.22.0
beautifulsoup4==4.9.1
```

python 3.8.1, ffmpeg

## Usage

Just run start.bat and go from there.



## Current state of this
This was all poorly made in about 5-10 minutes.

There's no validation for anything, we have useless temp files to determine the biggest file to get the highest quality video file, and we don't even handle incomplete downloads!

We even rely on a 3rd party to parse Facebook for the links to download. 

(since it was the quickest way to go about it, I made this for someone who needed it quickly and said all other CLI methods didn't save HQ)

Feel free to submit a pull request if you'd like to clean this up and maybe help take away the 3rd party reliance.

I have no further plans to do any more for this other then accepting pull requests.
