#!/usr/bin/env python

# utils.py

import re
from kivy.uix.textinput import TextInput

def dilute(undiluted_parts_per_unit, target_parts_per_unit, target_volume):
    """
    Finds the amount to dilute
    :param undiluted_parts_per_unit: int type or float type
    :param target_parts_per_unit: int type or float type
    :param target_volume: int type or float type
    :return: float type
    """
    return float((target_parts_per_unit * target_volume) / undiluted_parts_per_unit)


def convert_from_percent(whole_number):
    """
    Converts percentage to float
    :param whole_number: type string or type int
    :return: type float
    """
    return float(whole_number / 100)


class FloatInput(TextInput):
    """
    Custom widget to accept only float as input.
    """

    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)