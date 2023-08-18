from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text = "Evaluación")

if __name__ == "__main__":
    MyApp().run()