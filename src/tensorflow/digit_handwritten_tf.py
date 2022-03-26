# import os
# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from operator import itemgetter
import tensorflow as tf

from src.tensorflow.tf import TF
from src.utils import get_path


class DigitHandwrittenTF(TF):
    def __init__(self):
        TF.__init__(self, 'digit-handwritten')

    def load_data(self):
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

        self.add('train', x_train, y_train)
        self.add('test', x_test, y_test)

    def evaluate(self):
        model = self.get_model()
        (x_test, y_test) = itemgetter('x', 'y')(self.get_data('test'))
        x_test = self.normalize(x_test)

        loss, accuracy = model.evaluate(x_test, y_test)

        return loss, accuracy

    def create_model(self):
        (x_train, y_train) = itemgetter('x', 'y')(self.get_data('train'))
        x_train = self.normalize(x_train)

        model = tf.keras.models.Sequential()
        model.add(Flatten(input_shape=(28, 28)))
        model.add(Dense(units=128, activation='relu'))
        model.add(Dense(units=128, activation='relu'))
        model.add(Dense(units=10, activation='softmax'))

        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        model.fit(x_train, y_train, epochs=5)

        model.save(
            get_path(f'src/models/{self.name}.model')
        )

        self.model = model

        return True
