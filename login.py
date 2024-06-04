from kivymd.tools.hotreload.app import MDApp

from kivy.factory import Factory
from kivy.core.window import Window

Window.size = (450, 550)


class LoginApp(MDApp):
    # config your settings
    
    DEBUG = True
    # KV_FILES = []
    # Path of your kv file directory
    KV_DIRS = ["kv_files"]

    CLASSES = {"MainApp": "main"}

    def build_app(self, first=False):
        # Configuer your app setting here

        # called your entry-point class.
        return Factory.MainApp()


if __name__ == "__main__":
    LoginApp().run()