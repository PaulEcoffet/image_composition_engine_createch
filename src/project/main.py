from typing import Any

import yaml  ## Need uv add pyyaml
import numpy as np
from pprint import pprint
from abc import ABC, abstractmethod

def main():
    with open("conf.yml") as f:
        config = yaml.load(f, yaml.CFullLoader)
    pprint(config)
    print("*************")
    for layer in config["layers"]:
        print(layer["image"])
        print(layer["filters"])
        print("-----")
        # load image
        # apply filter
        # save img

class Blend(ABC):

    @abstractmethod
    def apply(self, background: np.ndarray, image: np.ndarray, opacity: float):
        raise NotImplementedError

class DifferenceBlend(Blend):
    def apply(self, background, image, opacity) -> np.ndarray:
        return background - opacity * image




main()