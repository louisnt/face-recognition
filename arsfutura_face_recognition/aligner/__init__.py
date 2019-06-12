from abc import ABC, abstractmethod


class Aligner(ABC):
    @abstractmethod
    def align(self, img):
        pass

    def __call__(self, *args, **kwargs):
        self.align(*args, **kwargs)
