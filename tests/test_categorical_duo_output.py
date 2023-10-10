import pytest
from py_af_colours import af_colours

unit_test_config_path = "./py_af_colours/config/config.yaml"

@pytest.mark.parametrize("palette, colour_format, number_of_colours, config_path, expected",
    [("duo", "hex", 2, unit_test_config_path,
      af_colours("duo", "hex", 2, unit_test_config_path)),  
     ("categorical", "hex", 2, unit_test_config_path,
      af_colours("duo", "hex", 2, unit_test_config_path))])

def test_categorical_two_equals_duo_hex(palette, colour_format,
                                        number_of_colours, config_path, expected):
    assert af_colours(palette, colour_format,
                      number_of_colours, config_path) == expected


@pytest.mark.parametrize("palette, colour_format, number_of_colours, config_path, expected",
    [("duo", "rgb", 2, unit_test_config_path,
      af_colours("duo", "rgb", 2, unit_test_config_path)),
     ("categorical", "rgb", 2, unit_test_config_path,
      af_colours("duo", "rgb", 2, unit_test_config_path))])

def test_categorical_two_equals_duo_rgb(palette, colour_format,
                                        number_of_colours, config_path, expected):
    assert af_colours(palette, colour_format,
                      number_of_colours, config_path) == expected