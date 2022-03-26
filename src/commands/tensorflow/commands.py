import click

from src.commands.tensorflow import tf_cli
from src.tensorflow.tf import TF
from src.tensorflow.digit_handwritten_tf import DigitHandwrittenTF
from src.tensorflow.letter_handwritten_tf import LetterHandwrittenTF


models = dict(
    digit=DigitHandwrittenTF(),
    letter=LetterHandwrittenTF()
)


@tf_cli.command('create-model')
@click.argument('name')
def create_model(name: str):
    tf: TF = models.get(name)
    tf.create_model()


@tf_cli.command('evaluate')
@click.argument('name')
def evaluate(name: str):
    tf: TF = models.get(name)
    tf.evaluate()
