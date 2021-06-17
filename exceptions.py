"""
This file contains (a little bit of OOP) user defined exception classes.
"""

class Error(Exception):
    # Base class for other exception classes
    pass

class ValueTooSmall(Error):
    # Notifies the user when the input value is too small
    pass

class ValueTooBig(Error):
    # Notifies the user when the input value is too big
    pass

