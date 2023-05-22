import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import webbrowser
import requests



class MainWindow(Screen):
    pass

class AboutMe(Screen):
    pass

class GCC(Screen):
    pass

class LG(Screen):
    pass

class LB(Screen):
    pass

class LR(Screen):
    pass

class WindowManager(ScreenManager):
    pass





kv = Builder.load_file('my.kv')

class ApgeneApp (App):
    def build(self):
        return kv

    
    
if __name__ == "__main__":
    ApgeneApp().run()