from typing import Any, List, Tuple, Union


def load(param: Union[int, str]) -> kpu_net:
    ...


def init_yolo2(kpu_net: kpu_net, threshold: float, nms_value: float, anchor_num: int,
               anchor: Union[List, Tuple]) -> None:
    ...


def deinit(stask: kpu_net) -> None:
    ...


def run_yolo2(kpu_net: kpu_net, image_t: Any) -> List:
    ...


def forward(kpu_net: kpu_net, image_t: Any, int: int) -> fmap:
    ...


def fmap(fmap: fmap, int: int) -> Any:
    """
    取特征图的指定通道数据到image对象
    :param fmap:
    :param int:
    :return:
    """
    ...


def fmap_free(fmap: fmap) -> None:
    ...


def netinfo(task: kpu_net) -> List:
    ...


class kpu_net:
    ...


class fmap:
    ...
