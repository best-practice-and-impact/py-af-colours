import pytest
from py_af_colours import af_colours

unit_test_config_path = "./py_af_colours/config/config.yaml"

def test_value_errors():
    with pytest.raises(ValueError):
        af_colours("wrong_palette", "hex", config_path = unit_test_config_path)
        af_colours("duo", "wrong_format", config_path = unit_test_config_path)
        af_colours("categorical", "hex", 0, config_path = unit_test_config_path)
        af_colours("categorical", "hex", 7, config_path = unit_test_config_path)

# TODO: Try pytest parametrize:
# Example use of af_colours:
# af_colours("duo", "hex")
# or introduce n, only used for categorical:
# af_colours("categorical", "hex", n = 4)

#value_errors_test_cases = [("wrong_palette", "hex"),
#                           ("duo", "wrong_format"),
#                           ("categorical", "hex", 0),
#                           ("categorical", "hex", 7)]

#@pytest.mark.parametrize("af_colours_input", value_errors_test_cases)
#def test_mean_errors(af_colours_input):
#    with pytest.raises(ValueError):
#        af_colours(af_colours_input)