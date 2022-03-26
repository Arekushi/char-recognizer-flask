import tensorflow as tf
import numpy as np
import pandas as pd
from operator import itemgetter

from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from keras.optimizer_v2.adam import Adam
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
from src.tensorflow.tf import TF, IMG_WIDTH, IMG_HEIGHT
from src.utils.letters import alphabet


class LetterHandwrittenTF(TF):
    def __init__(self):
        TF.__init__(self, 'letter-handwritten')

    @staticmethod
    def reshape(x):
        return np.reshape(x.values, (x.shape[0], 28, 28))

    @staticmethod
    def reshape_to_model(x):
        return x.reshape(x.shape[0], x.shape[1], x.shape[2], 1)

    def load_data(self):
        data = pd.read_csv('src/datasets/A_Z Handwritten_Data.csv').astype('float32')
        x = data.drop('0', axis=1)
        y = data['0']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        x_train = self.reshape(x_train)
        x_test = self.reshape(x_test)

        self.add('train', x_train, y_train)
        self.add('test', x_test, y_test)

    def evaluate(self):
        model = self.get_model()

        (x_train, y_train) = itemgetter('x', 'y')(self.get_data('train'))
        (x_test, y_test) = itemgetter('x', 'y')(self.get_data('test'))

        x_test = self.reshape_to_model(x_test)
        y_test_categorical = to_categorical(y_test, num_classes=26, dtype='int')

        loss, accuracy = model.evaluate(x_test, y_test_categorical)

        return loss, accuracy

    def create_model(self):
        (x_train, y_train) = itemgetter('x', 'y')(self.get_data('train'))
        (x_test, y_test) = itemgetter('x', 'y')(self.get_data('test'))

        x_train = self.reshape_to_model(x_train)
        x_test = self.reshape_to_model(x_test)

        y_train_categorical = to_categorical(y_train, num_classes=26, dtype='int')
        y_test_categorical = to_categorical(y_test, num_classes=26, dtype='int')

        model = tf.keras.models.Sequential()
        model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(MaxPool2D(pool_size=(2, 2), strides=2))
        model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'))
        model.add(MaxPool2D(pool_size=(2, 2), strides=2))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='valid'))
        model.add(MaxPool2D(pool_size=(2, 2), strides=2))
        model.add(Flatten())
        model.add(Dense(64, activation="relu"))
        model.add(Dense(128, activation="relu"))
        model.add(Dense(26, activation="softmax"))

        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy'],
        )

        model.fit(
            x_train,
            y_train_categorical,
            epochs=5,
            validation_data=(x_test, y_test_categorical)
        )

        model.save(f'src/models/{self.name}.model')

        self.model = model

        return True

    def predict(self, image_file):
        result = TF.predict(self, image_file)
        return alphabet[result].upper()
