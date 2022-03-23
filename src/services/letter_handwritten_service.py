from src.services.handwritten_abstract_service import Handwritten
from src.tensorflow.letter_handwritten_tf import LetterHandwrittenTF


class LetterHandWrittenService(Handwritten):
    def __init__(self):
        Handwritten.__init__(self, LetterHandwrittenTF())
