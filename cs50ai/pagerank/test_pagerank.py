import pytest
from pagerank import *


def test_transition_model():
    corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
    assert transition_model(corpus, "1.html", DAMPING) == {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}