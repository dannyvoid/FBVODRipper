@echo off

setlocal
cd /d %~dp0
pushd audio

for %%a in (*.mp4) do (
title converting audio for %%a
ffmpeg -i %%a -vn -acodec copy %%~na.aac
del /f %%a
)

popd
if not exist merged mkdir merged
pushd video

for %%a in (*.mp4) do (
title merging video for %%a
ffmpeg -i ../audio/%%~na.aac -i %%a -c:v copy -vcodec copy ../merged/%%~na.mp4
del /f %%a
popd 
pushd audio
del /f %%~na.aac
popd
pushd video
)