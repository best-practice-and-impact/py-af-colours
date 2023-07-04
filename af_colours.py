import warnings

def af_colours(palette: str,
               colour_format = "hex",
               number_of_colours = 6):
    """ 
    Return the chosen Analysis Function colour palette in hex or rgb
    format. For the categorical palette, this can be a chosen number of
    colours up to 6.

    Parameters
    ----------
    palette : string
        Type of palette required, with accepted values of "duo",
        "focus", "categorical", and "sequential".

    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    number_of_colours : int
        Number of colours required (categorical palette only). Takes
        values between 2 and 6. Returns 2 colours by default. If a
        palette other than categorical is chosen, any value passed
        is ignored.

    Raises
    ------
    ValueError
        If palette is not "categorical", "duo", "sequential", or "focus".
        Or if colour_format is not "hex" or "rgb".

    Returns
    -------
    list
        chosen_colours_list

    """
    if palette not in ["categorical", "duo", "sequential", "focus"]:
        raise ValueError(
             "palette value of " + palette +
             " is incorrect, must be categorical, duo, sequential, or focus as a string.")
    if colour_format.lower() not in ["hex", "rgb"]:
        raise ValueError(
             "colour_format value of " + colour_format +
             " is incorrect, must be hex or rgb as a string.")
    
    elif palette == "sequential":
        number_of_colours = 3
        chosen_colours_list =sequential_colours(colour_format)
    elif palette == "focus":
        chosen_colours_list = focus_colours(colour_format)
    elif palette == "duo":
        chosen_colours_list = duo_colours(colour_format)
    elif palette == "categorical":
        chosen_colours_list = categorical_colours(colour_format,
                                                  number_of_colours)
    if number_of_colours > 2:
        warnings.warn("Line charts using more than two colours " +
                      "may not meet accessibility standards.",
                      stacklevel = 2)
    return chosen_colours_list


def categorical_colours(colour_format = "hex", number_of_colours = 2):
    """ 
    Return the Analysis Function categorical colour palette as a list
    in hex or rgb format for up to 6 colours. If number_of_colours is 
    2, the function returns the duo palette.

    Parameters
    ----------
    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    number_of_colours : int
        Number of colours required, with accepted values between 2 and 6 inclusive.
        Returns 2 colours if no value given.

    Raises
    ------
    ValueError
        If number_of_colours is greater than 6.

    Returns
    -------
    list
        categorical_colours_list

    """
    categorical_hex_list = ["#12436D","#28A197","#801650",
                            "#F46A25","#3D3D3D","#A285D1"]

    if number_of_colours > 6:
        raise ValueError(
             "number_of_colours must not be more than 6 for the categorical palette.")
    if number_of_colours == 2:
        categorical_colours_list = duo_colours(colour_format)
        return categorical_colours_list

    elif colour_format == "hex":
        full_categorical_colours_list = categorical_hex_list
    elif colour_format == "rgb":
        full_categorical_colours_list = hex_to_rgb(categorical_hex_list)
    
    categorical_colours_list = full_categorical_colours_list[0:number_of_colours]

    return categorical_colours_list


def duo_colours(colour_format = "hex"):
    """ 
    Return the Analysis Function duo colour palette as a list of 2 
    colours in hex or rgb format. This function is also called by 
    sequential_colours() if number_of_colours is equal to 2.

    Parameters
    ----------
    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    Returns
    -------
    list
        duo_colours_list

    """
    duo_hex_list = ["#12436D","#F46A25"]
    
    if colour_format == "hex":
        duo_colours_list = duo_hex_list
    elif colour_format == "rgb":
        duo_colours_list = hex_to_rgb(duo_hex_list)

    return duo_colours_list


def sequential_colours(colour_format = "hex"):
    """ 
    Return the Analysis Function sequential colour palette as a list 
    of 3 colours in hex or rgb format.

    Parameters
    ----------
    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    Returns
    -------
    list
        sequential_colours_list

    """
    sequential_hex_list = ["#12436D", "#2073BC", "#6BACE6"]
    
    if colour_format == "hex":
            sequential_colours_list = sequential_hex_list
    elif colour_format == "rgb":
            sequential_colours_list = hex_to_rgb(sequential_hex_list)
    
    return(sequential_colours_list)


def focus_colours(colour_format = "hex"):
    """ 
    Return the Analysis Function focus colour palette as a list of 2 
    colours in hex or rgb format.

    Parameters
    ----------
    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    Returns
    -------
    list
        focus_colours_list

    """
    focus_hex_list = ["#12436D","#BFBFBF"]
    
    if colour_format == "hex":
            focus_colours_list = focus_hex_list
    elif colour_format == "rgb":
            focus_colours_list = hex_to_rgb(focus_hex_list)
    
    return focus_colours_list


def hex_to_rgb(hex_colours):
    """    
    Convert a list of hex codes to a list of rgb colours.

    Parameters
    ----------
    hex_colours : list
        The hex colours to be converted as a list of strings, with or 
        without # at the beginning.

    Raises
    ------
    TypeError
        If hex_colours is not a list.

    Returns
    -------
    list
        converted_list

    """
    if type(hex_colours) != list:
        raise TypeError(
             "hex_colours must be a list.")
        
    hex_colours_new = [i.lstrip('#') for i in hex_colours]
    
    converted_list = [(tuple(int(value[i:i+2], 16) for i in (0, 2, 4))) 
                      for value in hex_colours_new]
    return converted_list
