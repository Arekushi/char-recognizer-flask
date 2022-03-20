import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from PIL import Image
from PIL import ImageOps


Flatten = tf.keras.layers.Flatten
Dense = tf.keras.layers.Dense
Conv2D = tf.keras.layers.Conv2D
MaxPooling2D = tf.keras.layers.MaxPooling2D


IMG_HEIGHT = 28
IMG_WIDTH = 28


def get_model():
    return tf.keras.models.load_model('src/models/digit-handwritten.model')


def normalize(data):
    return tf.keras.utils.normalize(data, axis=1)


def get_data():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    return (x_train, y_train), (x_test, y_test)


# def resize(data):
#     return np.array(data).reshape(-1, IMG_HEIGHT, IMG_WIDTH, 1)


def create_model():
    (x_train, y_train), _ = get_data()
    x_train = normalize(x_train)

    model = tf.keras.models.Sequential()
    model.add(Flatten(input_shape=(IMG_HEIGHT, IMG_WIDTH)))
    model.add(Dense(units=128, activation='relu'))
    model.add(Dense(units=128, activation='relu'))
    model.add(Dense(units=10, activation='softmax'))

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(x_train, y_train, epochs=3)
    model.save('src/models/digit-handwritten.model')


def evaluate():
    model = get_model()
    _, (x_test, y_test) = get_data()
    x_test = normalize(x_test)

    loss, accuracy = model.evaluate(x_test, y_test)

    return loss, accuracy


def predict(image_file):
    model = get_model()

    img = Image.open(image_file).convert('RGB')
    # img = ImageOps.invert(img)

    img = np.array(img)
    img = img[:, :, 0].copy()
    img = np.invert(np.array([img]))

    prediction = model.predict(img)
    return np.argmax(prediction)
