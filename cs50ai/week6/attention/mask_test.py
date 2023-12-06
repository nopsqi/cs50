from mask import *

inputs = {}

def test_get_mask_token_index():
    inputs["input_ids"] = tf.constant([101, 2059, 1045, 3856, 2039, 1037, 103, 2013, 1996, 2795, 1012, 102])
    assert get_mask_token_index(103, inputs) == 6

def test_get_mask_token_index_1():
    inputs["input_ids"] = tf.constant([101, 2059, 1045, 3856, 2039, 1037, 1996, 2013, 103, 2795, 1012, 102])
    assert get_mask_token_index(103, inputs) == 8

def test_get_mask_token_index_none():
    inputs["input_ids"] = tf.constant([101, 2059, 1045, 3856, 2039, 1037, 103, 2013, 1996, 2795, 1012, 102])
    assert get_mask_token_index(104, inputs) == None

def test_get_color_for_attention_score_0():
    assert get_color_for_attention_score(0) == (0, 0, 0)

def test_get_color_for_attention_score_100():
    assert get_color_for_attention_score(1) == (255, 255, 255)

def test_get_color_for_attention_score_25():
    assert get_color_for_attention_score(0.25) == (64, 64, 64)

def test_get_color_for_attention_score_50():
    assert get_color_for_attention_score(0.5) == (128, 128, 128)
