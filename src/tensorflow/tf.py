from abc import ABC, abstractmethod
import tensorflow as tf
import numpy as np
import pathlib

from src.utils import get_path
from src.utils.image_utils import get_image
from operator import itemgetter
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout

IMG_HEIGHT = 28
IMG_WIDTH = 28


class TF(ABC):
    def __init__(self, name):
        self.model = None
        self.data = dict()
        self.name = name

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def create_model(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @staticmethod
    def normalize(data):
        return tf.keras.utils.normalize(data, axis=1)

    def add(self, type, x, y):
        self.data[type] = dict(x=x, y=y)

    def get_data(self, type):
        try:
            return self.data[type]
        except KeyError:
            self.load_data()
            return self.data[type]

    def get_model(self):
        if not self.model:
            self.model = tf.keras.models.load_model(
                get_path(f'src/models/{self.name}.model')
            )

        return self.model

    def predict(self, image_file):
        model = self.get_model()

        img = get_image(image_file)
        img = np.array(img)
        img = img[:, :].copy()
        img = np.invert(np.array([img]))

        prediction = model.predict(img)
        return np.argmax(prediction)
