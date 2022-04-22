from controller.screen_management import ScreenManagement
from kivymd.app import MDApp
from kivy.core.window import Window


# App size
Window.minimum_width, Window.minimum_height = (300, 640)


class MainApp(MDApp):
    def build(self):
        self.title = 'Hangman - The Master'
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '300'
        self.theme_cls.theme_style = 'Dark'

        return ScreenManagement()


if __name__ == '__main__':
    MainApp().run()
