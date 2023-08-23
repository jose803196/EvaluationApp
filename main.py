from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class CrearScreen(Screen):
    pass

class VerScreen(Screen):
    pass

class EditarScreen(Screen):
    pass

class PrinScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PrinScreen(name ='start'))
        sm.add_widget(CrearScreen(name="crear"))
        sm.add_widget(VerScreen(name="ver"))
        sm.add_widget(EditarScreen(name="editar"))
        return sm

if __name__ == "__main__":
    MyApp().run()