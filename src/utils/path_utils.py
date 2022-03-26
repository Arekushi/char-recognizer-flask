import os
import pathlib
import sys


def get_path(path):
    return os.path.join(pathlib.Path().parent.resolve(), path)
