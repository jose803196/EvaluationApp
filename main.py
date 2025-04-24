from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import sqlite3
from sqlite3 import OperationalError


class CrearScreen(Screen):
    def create_table(self):
        try:
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE Programacion 
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Apellido TEXT NOT NULL, 
                        Cedula INTEGER NOT NULL, Correo TEXT NOT NULL)""")
            conn.commit()
            conn.close()
            self.manager.current = 'fill'
            self.manager.transition.direction = 'left'
        except OperationalError as e:
            pass


class FillScreen(Screen):
    def fill(self):
        fname = self.ids.firstname.text
        lname = self.ids.lastname.text
        cedula = self.ids.cedula.text
        nail = self.ids.email.text

        if not all([fname, lname, cedula, nail]):
            return  # Validación básica

        try:
            cedula = int(cedula)
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Programacion (Name, Apellido, Cedula, Correo) VALUES (?,?,?,?)",
                          (fname, lname, cedula, nail))
            conn.commit()
            conn.close()
            
            # Limpiar campos después de insertar
            self.ids.firstname.text = ""
            self.ids.lastname.text = ""
            self.ids.cedula.text = ""
            self.ids.email.text = ""
            
        except ValueError:
            print("Cédula debe ser un número")
        except Exception as e:
            print(f"Error: {e}")


class VerScreen(Screen):
    pass


class EditarScreen(Screen):
    pass


class PrinScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        self.title = 'Eva App'
        
        sm = ScreenManager()
        sm.add_widget(PrinScreen(name='start'))
        sm.add_widget(CrearScreen(name="crear"))
        sm.add_widget(VerScreen(name="ver"))
        sm.add_widget(EditarScreen(name="editar"))
        sm.add_widget(FillScreen(name='fill'))
        
        return sm


if __name__ == "__main__":
    MyApp().run()