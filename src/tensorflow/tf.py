from abc import ABC, abstractmethod
import tensorflow as tf
import numpy as np

from PIL import Image
# from PIL import ImageOps

from operator import itemgetter
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout

IMG_HEIGHT = 28
IMG_WIDTH = 28


class TF(ABC):
    def __init__(self, name):
        self.model = None
        self.data = dict()
        self.name = name

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

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def create_model(self):
        pass

    def get_model(self):
        if not self.model:
            self.model = tf.keras.models.load_model(f'src/models/{self.name}.model')

        return self.model

    def evaluate(self):
        model = self.get_model()
        (x_test, y_test) = itemgetter('x', 'y')(self.get_data('test'))
        x_test = self.normalize(x_test)

        loss, accuracy = model.evaluate(x_test, y_test)

        return loss, accuracy

    def predict(self, image_file):
        model = self.get_model()

        img = Image.open(image_file).convert('RGB')
        # img = ImageOps.invert(img)

        img = np.array(img)
        img = img[:, :, 0].copy()
        img = np.invert(np.array([img]))

        prediction = model.predict(img)
        return np.argmax(prediction)
