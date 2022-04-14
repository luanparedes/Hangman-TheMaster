from kivy.uix.screenmanager import Screen


class InitialMenu(Screen):
    def __init__(self, **kw):
        super(InitialMenu, self).__init__(**kw)

        self.name = 'starting'
