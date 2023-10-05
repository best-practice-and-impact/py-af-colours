import pytest
from py_af_colours import af_colours

unit_test_config_path = "./py_af_colours/config/config.yaml"

def test_invalid_palette_value():
    with pytest.raises(ValueError):
        af_colours("wrong_palette", "hex", config_path = unit_test_config_path)

def test_invalid_colour_format_value():
    with pytest.raises(ValueError):
        af_colours("duo", "wrong_format", config_path = unit_test_config_path)

def test_invalid_low_number_of_colours_value():
    with pytest.raises(ValueError):
        af_colours("categorical", "hex", 0, config_path = unit_test_config_path)

def test_invalid_high_number_of_colours_value():
    with pytest.raises(ValueError):
        af_colours("categorical", "hex", 7, config_path = unit_test_config_path)