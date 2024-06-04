from kivymd.tools.hotreload.app import MDApp
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory
from kivy.core.window import Window

Window.size = (350, 580)


class Slope(MDApp):
    # config your settings
    
    DEBUG = True
    # KV_FILES = []
    # Path of your kv file directory
    KV_DIRS = ["kv_files"]

    CLASSES = {"MainApp": "main"}

    def build_app(self, first=False):
        
        
        # called your entry-point class.
        return Factory.MainApp()


if __name__ == "__main__":
    Slope().run()