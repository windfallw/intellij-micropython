from typing import Tuple, Union, List, Any, Optional


class Fpioa_Manager:

    def register(self, pin: int, function: int, force: bool) -> Any:
        ...

    def unregister(self, pin: int, function: int) -> Any:
        ...


fm = Fpioa_Manager()
