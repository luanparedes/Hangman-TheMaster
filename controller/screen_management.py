from controller.initial_menu import InitialMenu
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

        Builder.load_file('view/InitialMenu.kv')

        self.transition = FadeTransition()
        self.transition.duration = 0.7

        #Screens instances
        initial_menu = InitialMenu()
        self.add_widget(initial_menu)

        self.current = 'starting'


