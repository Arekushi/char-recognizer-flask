from src.services.handwritten_abstract_service import Handwritten
from src.tensorflow.digit_handwritten_tf import DigitHandwrittenTF


class DigitHandWrittenService(Handwritten):
    def __init__(self):
        Handwritten.__init__(self, DigitHandwrittenTF())
