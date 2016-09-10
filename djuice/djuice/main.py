#!/usr/bin/env python

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.properties import ObjectProperty, NumericProperty
from baseingredient import BaseIngredient


class BaseScreen(Screen):
    pass

class TestScreen2(Screen):
    pass

class TestScreen3(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('djuice.kv')

class DJuiceApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    DJuiceApp().run()