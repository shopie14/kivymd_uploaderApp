from kivymd.uix.screen import MDScreen
from View.LoginScreen.login_screen import LoginScreen


class MainApp(MDScreen):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.add_widget(LoginScreen())