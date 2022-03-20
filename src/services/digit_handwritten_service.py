from werkzeug.datastructures import FileStorage
from src.tensorflow.digit_handwritten_tf import create_model, evaluate, predict


class DigitHandWrittenService:
    @staticmethod
    def create_model():
        create_model()

        return {
            'success': True
        }

    @staticmethod
    def evaluate():
        loss, accuracy = evaluate()

        return {
            'loss': loss,
            'accuracy': accuracy
        }

    @staticmethod
    def predict(image_file: FileStorage):
        prediction = predict(image_file)

        return {
            'prediction': int(prediction)
        }
