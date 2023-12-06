from mask import *
from tensorflow.tsl.python.lib.core import pywrap_ml_dtypes

inputs = {}

def test_get_mask_token_index():
    inputs["input_ids"] = tf.constant([101, 2059, 1045, 3856, 2039, 1037, 103, 2013, 1996, 2795, 1012, 102], dtype=pywrap_ml_dtypes)
    assert get_mask_token_index(103, inputs) == 6
