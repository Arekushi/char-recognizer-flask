from werkzeug.datastructures import FileStorage
from src.tensorflow.digit import create_model, evaluate, predict


def create_model_tf():
    create_model()

    return {
        'success': True
    }


def evaluate_tf():
    loss, accuracy = evaluate()

    return {
        'loss': loss,
        'accuracy': accuracy
    }


def predict_tf(image_file: FileStorage):
    prediction = predict(image_file)

    return {
        'prediction': int(prediction)
    }
