import os
import cv2
import datetime


def byteconversion(bytes: int, to: str, default=1024) -> int:
    """Converts bytes to other storage formats.

    Args:
        bytes (int): bytes to be converted.
        to (str): convert to options['bit', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb']
        default (int, optional): 1024 bytes equals 1 kb. Defaults to 1024.

    Returns:
        int: converted bytes
    """
    result = float(bytes)
    if to == 'bit':
        return bytes * 8
    conversion = {'kb': 1, 'mb': 2, 'gb': 3, 'tb': 4, 'pb': 5, 'eb': 6}
    for _ in range(conversion[to]):
        result = result / default
    return int(result)


def get_length_seconds(file: str) -> int:
    """get the video length in secondss

    Args:
        file (str): file path

    Returns:
        int: video length in seconds
    """
    print(file.temporary_file_path())
    video = cv2.VideoCapture(file.temporary_file_path())
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    print(fps, frames)
    # print(file)
    return round(frames / fps)


def filesize(file: str, to: str) -> int:
    """Gets the video size in mb

    Args:
        file (str): file path.
        to (str): storage format.

    Returns:
        int : conversion of the bytes to provided storage format.
    """
    file_bytes = os.path.getsize(file.temporary_file_path())
    print(file_bytes)
    print(byteconversion(file_bytes, to))
    return byteconversion(file_bytes, to)


def rate(video_size: int, duration: int) -> int | float:
    """Charges the user according to the video size and duration specified

    Args:
        video_size (int): size of the video to be charged
        duration (int): duration of the video to be charged

    Returns:
        int: rate of the video
    """
    video_charge = 5 if video_size <= 500 else 12.5
    video_charge += 12.5 if duration <= 378 else 20
    return video_charge


# min rate = 17.5 (5+12.5) less size | less duration
# max rate = 32.5 (12.5+20) more size | more duration
# mid rate1 = 25 (5+20) less size | more duration
# mid rate2= 25 (12.5+12.5) more size | less duration
