from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('main.kv')


class RootWidget(BoxLayout):
    pass


class PandaStock(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    PandaStock().run()
