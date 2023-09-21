import pytest
import yaml
from py_af_colours import af_colours

with open("../py_af_colours/config/config.yaml") as file:
     config = yaml.load(file, Loader = yaml.BaseLoader)

def check_value_errors():
    with pytest.raises(ValueError):
        af_colours("wrong_palette", "hex")
        af_colours("duo", "wrong_format")
        af_colours("categorical", "hex", 0)
        af_colours("categorical", "hex", 7)


# TODO: Try pytest parametrize:
# Example use of af_colours:
# af_colours("duo", "hex")
# or introduce n, only used for categorical:
# af_colours("categorical", "hex", n = 4)

value_errors_test_cases = [("wrong_palette", "hex"),
                           ("duo", "wrong_format"),
                           ("categorical", "hex", 0),
                           ("categorical", "hex", 7)]

@pytest.mark.parametrize("af_colours_input", value_errors_test_cases)
def test_mean_errors(af_colours_input):
    with pytest.raises(ValueError):
        af_colours(af_colours_input)