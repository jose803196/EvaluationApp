from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import sqlite3
from sqlite3 import OperationalError


class CrearScreen(Screen):
    def crear_tabla(self):
        try:
            conn = sqlite3.connect('Notas.db')
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE Programacion 
                        (ID integer primary key, name text, apellido text, cedula integer, correo text)""")
            conn.commit()
            conn.close()
        except OperationalError as e:
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