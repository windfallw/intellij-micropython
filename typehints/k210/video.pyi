"""
Support play and record video with avi format.
"""


class avi:
    """
    Get from video.open().
    """

    def play(self) -> None:
        """
        Play video, decode one frame data(video or audio) every once called.

        """

    def volume(self, volume: int) -> int:
        """
        Set play volume.

        :param volume: value:[0,100].
        :return: Set value, ranges: [0,100].
        """

    def record(self) -> int:
        """
        Record video frame, it will block until the interval time up.

        :return: The length of current frame( video ).
        """


def open(path, record: bool = False, interval: int = 100000, quality: int = 50, width: int = 320, height: int = 240,
         audio: bool = False, sample_rate: int = 44100, channels: int = 1) -> avi:
    """
    Open a avi file to play or record.

    :param path: file path, e.g. /sd/badapple.avi.
    :param record: record video or not, if False just to play video.
    :param interval: Record interval, unit: micro second, fps = 1000000/interval, default to 100000, that is 10 frames per second.
    :param quality: jpeg compress quality(%), default to 50.
    :param width: record screen width, default to 320.
    :param height: record screen height, default to 240.
    :param audio: record audio or not, default to False.
    :param sample_rate: sample rate of recorded audio, default to 44100 (44.1k).
    :param channels: channels of recorded audio, default to 1.
    :return: Return a object, just support avi format yet, so just return a instance of avi class.
    """
