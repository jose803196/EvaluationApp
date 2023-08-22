from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class FirstScreen(BoxLayout):
    pass

class MyApp(App):
    pass

if __name__ == "__main__":
    MyApp().run()