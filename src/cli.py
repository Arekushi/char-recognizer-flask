from flask import Flask
from src.commands.tensorflow import tf_cli


clis = [
    tf_cli
]


def config_cli(app: Flask):
    for cli in clis:
        app.cli.add_command(cli)
