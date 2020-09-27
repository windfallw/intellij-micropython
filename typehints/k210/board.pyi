from typing import Union, List


class Board_Info:
    pin_num: int = 48
    JTAG_TCK: int = 0
    JTAG_TDI: int = 1
    JTAG_TMS: int = 2
    JTAG_TDO: int = 3
    ISP_RX: int = 4
    ISP_TX: int = 5
    WIFI_TX: int = 6
    WIFI_RX: int = 7
    WIFI_EN: int = 8
    PIN9: int = 9
    PIN10: int = 10
    PIN11: int = 11
    LED_B: int = 12
    LED_G: int = 13
    LED_R: int = 14
    PIN15: int = 15
    BOOT_KEY: int = 16
    PIN17: int = 17
    MIC_ARRAY_BCK: int = 18
    MIC_ARRAY_WS: int = 19
    MIC_ARRAY_DATA3: int = 20
    MIC_ARRAY_DATA2: int = 21
    MIC_ARRAY_DATA1: int = 22
    MIC_ARRAY_DATA0: int = 23
    MIC_ARRAY_LED: int = 24
    SPI0_CS1: int = 25
    SPI0_MISO: int = 26
    SPI0_CLK: int = 27
    SPI0_MOSI: int = 28
    SPI0_CS0: int = 29
    MIC0_WS: int = 30
    MIC0_DATA: int = 31
    MIC0_BCK: int = 32
    I2S_WS: int = 33
    I2S_DA: int = 34
    I2S_BCK: int = 35
    LCD_CS: int = 36
    LCD_RST: int = 37
    LCD_DC: int = 38
    LCD_WR: int = 39
    DVP_SDA: int = 40
    DVP_SCL: int = 41
    DVP_RST: int = 42
    DVP_VSYNC: int = 43
    DVP_PWDN: int = 44
    DVP_HSYNC: int = 45
    DVP_XCLK: int = 46
    DVP_PCLK: int = 47

    pin_name: List = ['JTAG_TCK', 'JTAG_TDI', 'JTAG_TMS', 'JTAG_TDO', 'ISP_RX', 'ISP_TX', 'WIFI_TX ', 'WIFI_RX ',
                      'WIFI_EN ', 'PIN9', 'PIN10', 'PIN11', 'LED_B', 'LED_G', 'LED_R', 'PIN15', 'BOOT_KEY', 'PIN17',
                      'MIC_ARRAY_BCK', 'MIC_ARRAY_WS ', 'MIC_ARRAY_DATA3', 'MIC_ARRAY_DATA2', 'MIC_ARRAY_DATA1',
                      'MIC_ARRAY_DATA0', 'MIC_ARRAY_LED', 'SPI0_CS1', 'SPI0_MISO', 'SPI0_CLK ', 'SPI0_MOSI', 'SPI0_CS0',
                      'MIC0_WS', 'MIC0_DATA', 'MIC0_BCK', 'I2S_WS', 'I2S_DA', 'I2S_BCK', 'LCD_CS', 'LCD_RST', 'LCD_DC',
                      'LCD_WR ', 'DVP_SDA', 'DVP_SCL', 'DVP_RST', 'DVP_VSYNC', 'DVP_PWDN', 'DVP_HSYNC', 'DVP_XCLK',
                      'DVP_PCLK']

    D: List = [4, 5, 21, 22, 23, 24, 32, 15, 14, 13, 12, 11, 10, 3]

    def pin_map(self, Pin: int) -> Union[bool, str]:
        ...


board_info = Board_Info()
