#!/usr/bin/env python

import re

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import ActionBar, ActionView, ActionButton
from kivy.properties import NumericProperty, BooleanProperty, ObjectProperty
from kivy.graphics import Color
from kivy.lang import Builder

from utils import FloatInput, dilute, convert_from_percent
from customwidgets import ClearButton

base = Builder.load_file('baseingredient.kv')


class NicInput(BoxLayout):
    _undil_nic_str = NumericProperty(0)
    _undil_nic_vg = NumericProperty(0)
    _undil_nic_pg = NumericProperty(0)


class BaseInput(BoxLayout):
    _targ_vol = NumericProperty(0)
    _tar_nic = NumericProperty(0)
    _tar_vg = NumericProperty(0)
    _tar_pg = NumericProperty(0)


class BaseIngredient(BoxLayout):

    def build(self):
        return base


