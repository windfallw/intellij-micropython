from typing import Tuple, Optional


def set(cpu: Optional[int] = None, pll1: Optional[int] = None, kpu_div: Optional[int] = None) -> None:
    ...


def get() -> Tuple[int, int]:
    ...


def get_cpu() -> int:
    ...


def get_kpu() -> int:
    ...
