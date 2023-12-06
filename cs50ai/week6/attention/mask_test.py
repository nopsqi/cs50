from mask import *
from transformers import AutoTokenizer, TFBertForMaskedLM

inputs = {}
tokenizer = AutoTokenizer.from_pretrained(MODEL)

def test_get_mask_token_index():
    assert get_mask_token_index(103, tokenizer("then i picked up a [MASK] from the table.", return_tensors="tf")) == 6

def test_get_mask_token_index_1():
    assert get_mask_token_index(103, tokenizer("then i [MASK] up a book from the table.", return_tensors="tf")) == 2

def test_get_mask_token_index_none():
    assert get_mask_token_index(104, tokenizer("then i picked up a book from the table.", return_tensors="tf")) == None

def test_get_color_for_attention_score_0():
    assert get_color_for_attention_score(tf.constant(0)) == (0, 0, 0)

def test_get_color_for_attention_score_100():
    assert get_color_for_attention_score(tf.constant(1)) == (255, 255, 255)

def test_get_color_for_attention_score_25():
    assert get_color_for_attention_score(tf.constant(0.25)) == (64, 64, 64)

def test_get_color_for_attention_score_50():
    assert get_color_for_attention_score(tf.constant(0.5)) == (128, 128, 128)
