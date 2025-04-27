from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import sqlite3
from sqlite3 import OperationalError
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from functools import partial 

class CrearScreen(Screen):  
    def create_table(self):  
        try:  
            # Conexión a la base de datos  
            conn = sqlite3.connect('Base.db')  
            cursor = conn.cursor()  
            
            # Crear tabla de estudiantes  
            cursor.execute("""CREATE TABLE IF NOT EXISTS Estudiantes   
                              (ID INTEGER PRIMARY KEY AUTOINCREMENT,   
                              Nombre TEXT NOT NULL,   
                              Apellido TEXT NOT NULL,   
                              Cedula TEXT NOT NULL UNIQUE,   
                              Correo TEXT NOT NULL)""")  
            
            # Crear tabla de notas  
            cursor.execute("""CREATE TABLE IF NOT EXISTS Notas   
                              (ID INTEGER PRIMARY KEY AUTOINCREMENT,  
                              EstudianteID INTEGER NOT NULL,  
                              Practica TEXT NOT NULL,  
                              Nota REAL NOT NULL,
                              FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(ID))""")  
            
            # Guardar cambios y cerrar conexión  
            conn.commit()  
            conn.close()  
            
            # Cambiar a la siguiente pantalla  
            self.manager.current = 'fill'  
            self.manager.transition.direction = 'left'  
        except OperationalError as e:  
            print(f"Error creando tablas: {e}")

class FillScreen(Screen):
    def fill(self):
        nombre = self.ids.firstname.text
        apellido = self.ids.lastname.text
        cedula = self.ids.cedula.text
        email = self.ids.email.text

        if not all([nombre, apellido, cedula, email]):
            self.mostrar_error("Todos los campos son obligatorios")
            return

        try:
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO Estudiantes (Nombre, Apellido, Cedula, Correo) VALUES (?,?,?,?)",
                          (nombre, apellido, cedula, email))
            
            conn.commit()
            conn.close()
            
            # Limpiar campos
            self.ids.firstname.text = ""
            self.ids.lastname.text = ""
            self.ids.cedula.text = ""
            self.ids.email.text = ""
            
            self.mostrar_exito("Estudiante registrado exitosamente")
            
        except sqlite3.IntegrityError:
            self.mostrar_error("La cédula ya está registrada")
        except Exception as e:
            self.mostrar_error(f"Error: {str(e)}")

    def mostrar_error(self, mensaje):
        self.dialog = MDDialog(
            title="Error",
            text=mensaje,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: self.dialog.dismiss())]
        )
        self.dialog.open()

    def mostrar_exito(self, mensaje):
        self.dialog = MDDialog(
            title="Éxito",
            text=mensaje,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: self.dialog.dismiss())]
        )
        self.dialog.open()


class VerScreen(Screen):
    def on_pre_enter(self):
        self.cargar_estudiantes()
    
    def cargar_estudiantes(self):
        lista = self.ids.lista_estudiantes
        lista.clear_widgets()
        
        try:
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Estudiantes")
            estudiantes = cursor.fetchall()
            
            for estudiante in estudiantes:
                item = TwoLineListItem(
                    text=f"{estudiante[1]} {estudiante[2]}",
                    secondary_text=f"Cédula: {estudiante[3]} | Correo: {estudiante[4]}"
                )
                item.bind(on_release=partial(self.mostrar_detalle, estudiante[0]))
                lista.add_widget(item)
                
        except Exception as e:
            print(f"Error cargando estudiantes: {e}")
        finally:
            conn.close()
    
    def mostrar_detalle(self, estudiante_id, *args):
        try:
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Estudiantes WHERE ID=?", (estudiante_id,))
            estudiante = cursor.fetchone()
            
            cursor.execute("SELECT Practica, Nota FROM Notas WHERE EstudianteID=?", (estudiante_id,))
            notas = cursor.fetchall()
            
            contenido = f"Nombre: {estudiante[1]}\nApellido: {estudiante[2]}\nCédula: {estudiante[3]}\nCorreo: {estudiante[4]}"
            
            if notas:
                contenido += "\n\nNotas:"
                for nota in notas:
                    contenido += f"\n- {nota[0]}: {nota[1]}"
            
            self.dialog = MDDialog(
                title="Detalle del Estudiante",
                text=contenido,
                buttons=[
                    MDFlatButton(text="Cerrar", on_release=lambda x: self.dialog.dismiss()),
                    MDFlatButton(text="Agregar Nota", on_release=lambda x: self.agregar_nota(estudiante_id))
                ],
                size_hint=(0.8, None)
            )
            self.dialog.open()
            
        except Exception as e:
            print(f"Error mostrando detalle: {e}")
        finally:
            conn.close()


class EditarScreen(Screen):
    pass


class PrinScreen(Screen):
    pass


class MyApp(MDApp):
    def ir_a_start(self):
        self.root.current = 'start'
        self.root.transition.direction = 'right'

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
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