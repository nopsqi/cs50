from mask import *
from tensorflow import dtypes

inputs = {}

def test_get_mask_token_index():
    inputs["input_ids"] = tf.constant([101, 2059, 1045, 3856, 2039, 1037, 103, 2013, 1996, 2795, 1012, 102], dtype=dtypes.ml_dtypes.float8_e4m3b11fnuz)
    assert get_mask_token_index(103, inputs) == 6


def test_get_mask_token_index():
    inputs["input_ids"] = tf.constant([101, 2059, 1045, 3856, 2039, 1037, 103, 2013, 1996, 2795, 1012, 102])
    assert get_mask_token_index(103, inputs) == 6
