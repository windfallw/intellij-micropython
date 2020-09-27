from . import (FFT as FFT, freq as freq, utils as utils)
from typing import Optional, Callable, List, Any


class GPIO:
    GPIO0: int
    GPIO1: int
    GPIO2: int
    GPIO3: int
    GPIO4: int
    GPIO5: int
    GPIO6: int
    GPIO7: int

    GPIOHS0: int
    GPIOHS1: int
    GPIOHS2: int
    GPIOHS3: int
    GPIOHS4: int
    GPIOHS5: int
    GPIOHS6: int
    GPIOHS7: int
    GPIOHS8: int
    GPIOHS9: int
    GPIOHS10: int
    GPIOHS11: int
    GPIOHS12: int
    GPIOHS13: int
    GPIOHS14: int
    GPIOHS15: int
    GPIOHS16: int
    GPIOHS17: int
    GPIOHS18: int
    GPIOHS19: int
    GPIOHS20: int
    GPIOHS21: int
    GPIOHS22: int
    GPIOHS23: int
    GPIOHS24: int
    GPIOHS25: int
    GPIOHS26: int
    GPIOHS27: int
    GPIOHS28: int
    GPIOHS29: int
    GPIOHS30: int
    GPIOHS31: int

    IN: int
    OUT: int

    PULL_UP: int
    PULL_DOWN: int
    PULL_NONE: int

    IRQ_RISING: int
    IRQ_FALLING: int
    IRQ_BOTH: int

    def __init__(self, ID: int, MODE: int, PULL: Optional[int] = None, VALUE: Optional[int] = None) -> None:
        ...

    def value(self, value: Optional[int] = None) -> int:
        ...

    def irq(self, CALLBACK_FUNC: Callable, TRIGGER_CONDITION: int) -> None:
        ...

    def disirq(self) -> None:
        ...

    def mode(self, MODE: int) -> None:
        ...

    def pull(self, PULL: int) -> None:
        ...


class Audio:
    def __init__(self, array: Optional[bytearray] = None, path: Optional[str] = None,
                 points: Optional[int] = 1024) -> None:
        ...

    def to_bytes(self) -> bytearray:
        ...

    def play_process(self, i2s_dev: Any) -> List:
        ...

    def play(self) -> Optional[int]:
        ...

    def finish(self) -> None:
        ...


class FPIOA:
    def __init__(self) -> None:
        ...

    def help(self, func: Optional[int] = None) -> str:
        ...

    def set_function(self, pin: int, func: int) -> None:
        ...

    def get_Pin_num(self, func: int) -> int:
        ...


class I2S:
    def __init__(self, device_num: int) -> None:
        ...

    def channel_config(self, channel: int, mode: int, resolution: int, cycles: int, align_mode: int) -> None:
        ...

    def set_sample_rate(self, sample_rate: int) -> None:
        ...

    def record(self, points: int) -> Audio:
        ...

    def play(self, audio: Audio) -> None:
        ...
