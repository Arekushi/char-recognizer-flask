from abc import ABC, abstractmethod
from werkzeug.datastructures import FileStorage


class Handwritten(ABC):
    def __init__(self, tf):
        self.tf = tf

    def create_model(self):
        result = self.tf.create_model()

        return {
            'success': result
        }

    def evaluate(self):
        loss, accuracy = self.tf.evaluate()

        return {
            'loss': loss,
            'accuracy': accuracy
        }

    def predict(self, image_file: FileStorage):
        prediction = self.tf.predict(image_file)

        return {
            'prediction': f'{prediction}'
        }
