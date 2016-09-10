#!/usr/bin/env python

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.actionbar import ActionBar, ActionView, ActionButton
from kivy.uix.settings import SettingsWithSpinner, SettingsPanel
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.factory import Factory
from kivy.properties import ObjectProperty





class TestWidgetsApp(App):

    def build(self):
        return Builder.load_string()


if __name__ == '__main__':
    TestWidgetsApp().run()