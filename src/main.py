from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from .database import check_database_exists, create_connection, close_connection

Builder.load_file('main.kv')


class RootWidget(BoxLayout):
    pass


class PandaStock(App):
    def build(self):
        if check_database_exists("panda_stocks.db"):
            print("Database file exists.")
        else:
            print("Database file does not exist.")
        
        return RootWidget()


if __name__ == '__main__':        
    PandaStock().run()
