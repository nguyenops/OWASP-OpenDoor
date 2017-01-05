# -*- coding: utf-8 -*-

"""TplError classes"""

class TplError(Exception):
    """TplError class"""

    def __init__(self, message):
        super(TplError, self).__init__(message)

class ColorError(Exception):
    """ColorError class"""

    def __init__(self, message):
        super(ColorError, self).__init__(message)