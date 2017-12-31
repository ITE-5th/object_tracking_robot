from abc import ABCMeta, abstractmethod


class ObjectDetector(metaclass=ABCMeta):
    @abstractmethod
    def _detect(self, image):
        raise NotImplementedError()

    @abstractmethod
    def _detect_all(self, image):
        raise NotImplementedError()

    def detect(self, image):
        return self._detect(image)

    def detect_all(self, image):
        return self._detect_all(image)
