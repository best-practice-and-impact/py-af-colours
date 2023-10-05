import pytest
from py_af_colours import af_colours

unit_test_config_path = "./py_af_colours/config/config.yaml"

@pytest.mark.parametrize("palette, colour_format, number_of_colours, config_path",
    [("categorical", "hex", 1, unit_test_config_path),
     ("categorical", "hex", 2, unit_test_config_path),
     ("categorical", "hex", 3, unit_test_config_path),    
     ("categorical", "hex", 4, unit_test_config_path),
     ("categorical", "hex", 5, unit_test_config_path),
     ("categorical", "hex", 6, unit_test_config_path),],)

def test_categorical_list_length(palette, colour_format, number_of_colours, config_path):
    assert len(af_colours(palette, colour_format, number_of_colours, config_path)) == number_of_colours