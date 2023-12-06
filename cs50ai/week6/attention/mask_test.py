from mask import *

inputs = {}
mask_token_id = 103

def test_get_mask_token_index():
    inputs["input_ids"] = tf.constant([[101, 2059, 1045, 3856, 2039, 1037, 103, 2013, 1996, 2795, 1012, 102]])
    assert get_mask_token_index(mask_token_id, inputs) == 6

def test_get_mask_token_index_1():
    inputs["input_ids"] = tf.constant([[101, 2059, 1045, 103, 2039, 1037, 2338, 2013, 1996, 2795, 1012, 102]])
    assert get_mask_token_index(mask_token_id, inputs) == 3

def test_get_mask_token_index_none():
    inputs["input_ids"] = tf.constant([[101, 2059, 1045, 3856, 2039, 1037, 2338, 2013, 1996, 2795, 1012, 102]])
    assert get_mask_token_index(mask_token_id, inputs) == None

def test_get_color_for_attention_score_0():
    assert get_color_for_attention_score(tf.constant(0)) == (0, 0, 0)

def test_get_color_for_attention_score_100():
    assert get_color_for_attention_score(tf.constant(1)) == (255, 255, 255)

def test_get_color_for_attention_score_25():
    assert get_color_for_attention_score(tf.constant(0.25)) == (64, 64, 64)

def test_get_color_for_attention_score_50():
    assert get_color_for_attention_score(tf.constant(0.5)) == (128, 128, 128)
