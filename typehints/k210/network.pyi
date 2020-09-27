from typing import Tuple, Union, List, Any

OPEN: int = 0
WPA_PSK: int = 2
WPA2_PSK: int = 3
WPA_WPA2_PSK: int = 4


class ESP8285:

    def __init__(self, uart: int) -> None:
        """

        :param uart:
        """

    def connect(self, ssid: str, key: str) -> None:
        """

        :param ssid:
        :param key:
        :return:
        """

    def ifconfig(self) -> Union[Tuple[str, str, str, str, str, str, str], int]:
        """

        :return:
        """

    def isconnected(self) -> bool:
        """

        :return:
        """

    def disconnect(self) -> None:
        """

        :return:
        """

    def scan(self) -> List:
        """

        :return:
        """

    def enable_ap(self, ssid: str, key: str, chl: int, ecn: int = WPA2_PSK) -> None:
        """

        :param ssid:
        :param key:
        :param chl:
        :param ecn:
        :return:
        """

    def disable_ap(self) -> None:
        """

        :return:
        """


class ESP32_SPI:

    def __init__(self, cs: int, rst: int, rdy: int, mosi: int, miso: int, sclk: int) -> None:
        """

        :param cs:
        :param rst:
        :param rdy:
        :param mosi:
        :param miso:
        :param sclk:
        """

    def adc(self) -> Tuple[Any, Any, Any, Any, Any]:
        """

        :return:
        """

    def connect(self, ssid: str, key: str) -> None:
        """

        :param ssid:
        :param key:
        :return:
        """

    def ifconfig(self) -> Union[Tuple[str, str, str, str, str, str, str], int]:
        """

        :return:
        """

    def isconnected(self) -> bool:
        """

        :return:
        """

    def disconnect(self) -> None:
        """

        :return:
        """

    def scan(self) -> List:
        """

        :return:
        """
