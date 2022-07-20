import os
import cv2
import datetime

video_path = "D:/Projects/python projects/rpalabs/video storage/video_files/miyukixfuziwararap.mp4"
video = cv2.VideoCapture(video_path)

frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
seconds = round(frames / fps)
video_time = datetime.timedelta(seconds=seconds)
filesize = os.path.getsize(video_path)


def byteconversion(bytes, to, default=1024):
    result = float(bytes)
    if to == 'bit':
        return bytes * 8
    conversion = {'kb': 1, 'mb': 2, 'gb': 3, 'tb': 4, 'pb': 5, 'eb': 6}
    for _ in range(conversion[to]):
        result = result / default
    return(result)


print(f'video in seconds: {seconds}')
print(f'video in minutes: {video_time}')
print(f"video size: {byteconversion(filesize, 'mb')}")
