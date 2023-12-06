from mask import *
from transformers import AutoTokenizer, TFBertForMaskedLM

tokenizer = AutoTokenizer.from_pretrained(MODEL)

def test_get_mask_token_index():
    inputs = tokenizer("then i picked up a [MASK] from the table.", return_tensors="tf")
    assert get_mask_token_index(tokenizer.mask_token_id, inputs) == 6

def test_get_mask_token_index_1():
    inputs = tokenizer("then i [MASK] up a book from the table.", return_tensors="tf")
    assert get_mask_token_index(tokenizer.mask_token_id, inputs) == 2

def test_get_mask_token_index_none():
    inputs = tokenizer("then i picked up a book from the table.", return_tensors="tf")
    assert get_mask_token_index(tokenizer.mask_token_id, inputs) == None

def test_get_color_for_attention_score_0():
    assert get_color_for_attention_score(tf.constant(0)) == (0, 0, 0)

def test_get_color_for_attention_score_100():
    assert get_color_for_attention_score(tf.constant(1)) == (255, 255, 255)

def test_get_color_for_attention_score_25():
    assert get_color_for_attention_score(tf.constant(0.25)) == (64, 64, 64)

def test_get_color_for_attention_score_50():
    assert get_color_for_attention_score(tf.constant(0.5)) == (128, 128, 128)
