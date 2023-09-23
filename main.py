from kivy.app import App
#from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen, ScreenManager
import sqlite3
from sqlite3 import OperationalError


class CrearScreen(Screen):
    def create_table(self,nombreinput):
        try:
            conn = sqlite3.connect(self.ids.nombreinput.text+'.db')
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE Programacion 
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Apellido TEXT NOT NULL, Cedula INTEGER NOT NULL, Correo TEXT NOT NULL)""")
            conn.commit()
            conn.close()
        except OperationalError as e:
            pass

class FillScreen(Screen):
    def fill(self):
        fname = self.ids['firstname'].text
        lname = self.ids['lastname'].text
        cedula = int(self.ids['cedula'].text)
        nail = self.ids['email'].text

        conn = sqlite3.connect('Base2.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Programacion (Name, Apellido, Cedula, Correo) VALUES (?,?,?,?)",(fname,lname,cedula,nail))
        conn.commit()
        conn.close()

class VerScreen(Screen):
    pass

class EditarScreen(Screen):
    pass

class PrinScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        self.title = 'Eva App'
        #Window.clearcolor = (1,1,1,1)
        sm = ScreenManager()
        sm.add_widget(PrinScreen(name ='start'))
        sm.add_widget(CrearScreen(name="crear"))
        sm.add_widget(VerScreen(name="ver"))
        sm.add_widget(EditarScreen(name="editar"))
        sm.add_widget(FillScreen(name='fill'))
        return sm

if __name__ == "__main__":
    MyApp().run()