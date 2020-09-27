"""
Sensor module for camera configuration and image capture, etc., used to control the development board camera to complete the camera task.
"""

from typing import Any, Optional

INVLAID: int

BAYER: int  #1BPP/RAW
RGB565: int  #2BPP/RGB565
YUV422: int  #2BPP/YUV422
GRAYSCALE: int  #1BPP/GRAYSCALE
JPEG: int  #JPEG/COMPRESSED

"C/SIF Resolutions"
QQCIF: int  #88x72
QCIF: int  #176x144
CIF: int  #352x288
QQSIF: int  #88x60
QSIF: int  #176x120
SIF: int  #352x240

"VGA Resolutions"
QQQQVG: int  #40x30
QQQVGA: int  #80x60
QQVGA: int  #160x120
QVGA: int  #320x240
VGA: int  #640x480
HQQQVG: int  #60x40
HQQVGA: int  #120x80
HQVGA: int  #240x160

"FFT Resolutions"
B64X32: int  #64x32
B64X64: int  #64x64
B128X64: int  #128x64
B128X12: int  #128x128
B240X24: int  #240x240

"Other"
LCD: int  #128x160
QQVGA2: int  #128x160
WVGA: int  #720x480
WVGA2: int  #752x480
SVGA: int  #800x600
SXGA: int  #1280x1024
UXGA: int  #1600x1200


def reset(freq: int = 24000000, set_regs: bool = True, dual_buff: bool = False) -> None:
    """
    Reset and initialize the camera.

    :param freq: Set the clock frequency of sensor. The higher the frequency, the higher the frame rate, but the picture quality may be worse. The default is 24MHz. If the camera has colored spots (ov7740), you can lower it appropriately, such as 20MHz.
    :param set_regs:  Allows the program to write camera registers. The default isTrue. If you need a custom reset sequence, you can set it to False, and then use the sensor.__ write_reg(addr, value) function to customize the write register sequence.
    :param dual_buff: The default isFalse.Allowing double buffering will increase the frame rate, but the memory footprint will also increase (about 384KiB).
    """


def binocular_reset() -> None:
    """
    Reset and initialize the binocular camera.

    """


def run(enable: int) -> bool:
    """
    Turn on image capture.

    :param enable: 1 means start grabbing image, 0 means stop grabbing image.
    :return: True : set successfully, False : setting error.
    """


def set_framesize(framesize: int, set_regs: bool = True) -> bool:
    """
    It is used to set the camera output frame size. The k210 supports VGA format at most. If it is larger than VGA, it will not be able to acquire images. The screen of the MaixPy development board is 320*240 resolution, and the recommended setting is QVGA format.

    :param framesize: frame size.
    :param set_regs: Allows the program to write camera registers. The default isTrue. If you need a custom sequence, you can set it to False, and then use the sensor.__ write_reg(addr, value) function to customize the write register sequence.
    :return: True : set successfully, False: setting error.
    """


def set_pixformat(format: int, set_regs: bool = True) -> bool:
    """
    Used to set the camera output format, k210 supports rgb565 and yuv422 formats. The screen of the MaixPy development board configuration is set using rgb565, and the recommended setting is RGB565 format.

    :param format: frame format.
    :param set_regs: Allows the program to write camera registers. The default isTrue. If you need a custom sequence, you can set it to False, and then use the sensor.__ write_reg(addr, value) function to customize the write register sequence.
    :return: True : set successfully, False: setting error.
    """


def snapshot() -> Any:
    """
    Control camera capture image.

    :return: image object.
    """


def shutdown(param: bool) -> None:
    """
    关闭摄像头/切换摄像头

    单目摄像头
    enable: True 表示开启摄像头 False 表示关闭摄像头
    双目摄像头
    select: 通过写入 0 或 1 来切换摄像头
    """


def skip_frames(n: Optional[int] = None, time: Optional[int] = 300) -> None:
    """
    Skip the specified number of frames or skip the image for the specified time.

    若 n 和 time 皆未指定，该方法跳过300毫秒的帧；若二者皆指定，该方法会跳过 n 数量的帧，但将在 time 毫秒后返回

    :param n: skip n frame image.
    :param time: Skip the specified time in ms.
    """


def width() -> int:
    """
    Get camera resolution width.

    :return: camera resolution width of int type.
    """


def height() -> int:
    """
    Get camera resolution height.

    :return: int type camera resolution height.
    """


def get_fb() -> int:
    """
    Get the current camera ID.

    :return: int type ID.
    """


def set_colorbar(enable: bool) -> None:
    """
    Set the camera to color bar mode.

    :param enable: 1 means to turn on the color bar mode 0 means to turn off the color bar mode.
    """


def set_contrast(contrast: int) -> bool:
    """
    Set camera contrast.

    :param contrast: camera contrast, range [-2, +2].
    :return: set successfully or error.
    """


def set_brightness(brightness: int) -> bool:
    """
    Set camera brightness.

    :param brightness: camera saturation, range [-2, +2].
    :return: True : set successfully or error.
    """


def set_auto_gain(enable: bool, gain_db: Optional[int] = None) -> None:
    """
    Set the camera automatic gain mode.

    如果需要追踪颜色，需要关闭自动增益

    :param enable: 1 means to turn on automatic gain 0 means to turn off automatic gain.
    :param gain_db:  Set the camera fixed gain value when the auto gain is turned off, the unit is db.
    """


def get_gain_db() -> float:
    """
    Get camera gain value.

    :return: Gain value of float type.
    """


def set_hmirror(enable: bool) -> None:
    """
    Set the camera horizontal mirror.

    :param enable: 1 means to turn on horizontal mirroring 0 to turn off horizontal mirroring.
    """


def __write_reg(address: Any, value: Any) -> None:
    """
    Write the specified value to the camera register.

    :param address: register address.
    :param value: write value.
    """


def __read_reg(address: Any) -> int:
    """
    Read camera register value.

    :param address: register address.
    :return: Register value of type int.
    """
