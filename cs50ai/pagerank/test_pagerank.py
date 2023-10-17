import pytest
from pagerank import *


def test_transition_model():
    corpus = crawl("pagerank/corpus0")
    assert transition_model(corpus, "1.html", DAMPING) == 5