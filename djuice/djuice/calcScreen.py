"""
Calculator Screen
"""

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class LabelSliderBox(BoxLayout):
    pass


class VolumeSliderBox(BoxLayout):
    pass


class NicotineSliderBox(BoxLayout):
    pass


class BaseSliderBox(BoxLayout):
    pass

build1 = Builder.load_file('labelsliderbox.kv')


class Calculator(App):
    def build(self):
        return build1


if __name__ == '__main__':
    Calculator().run()
