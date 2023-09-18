import pytest
from py_af_colours import af_colours

def check_value_errors():
    with pytest.raises(ValueError):
        af_colours("wrong_palette", "hex")
        af_colours("duo", "wrong_format")
        af_colours("categorical", "hex", 0)

# tests to write:
# check palette option if not in list gives error
# check colour format option if not in list gives error
# n <= 6 for categorical palette gives error
# n = 0 gives value error
# palette types just give u list of hex codes
# test that with focus u get the right list if it's hex or rgb
# test that categorical gives u list of length asked for
# categorical switches to duo