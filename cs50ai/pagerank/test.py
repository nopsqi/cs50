import pytest
from pagerank import *


def test_transition_model():
    corpus = crawl("corpus0")
    assert transition_model(corpus, )