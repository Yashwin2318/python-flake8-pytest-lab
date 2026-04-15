import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project_package import base


def test_run():
    assert base.runme() == 1
