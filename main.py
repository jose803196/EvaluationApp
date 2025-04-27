from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import sqlite3
from sqlite3 import OperationalError
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

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
    estudiante_actual = None
    
    def on_pre_enter(self):
        self.cargar_estudiantes()

    def cargar_estudiantes(self):
        self.ids.lista_estudiantes.clear_widgets()
        try:
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            cursor.execute("SELECT ID, Nombre, Apellido, Cedula FROM Estudiantes")
            for estudiante in cursor.fetchall():
                item = OneLineListItem(
                    text=f"{estudiante[1]} {estudiante[2]} - Cédula: {estudiante[3]}",
                    height=50
                )
                item.bind(on_release=lambda x, est_id=estudiante[0]: self.mostrar_notas(est_id))
                self.ids.lista_estudiantes.add_widget(item)
        except Exception as e:
            print(f"Error cargando estudiantes: {e}")
        finally:
            conn.close()

    def mostrar_notas(self, estudiante_id):
        self.estudiante_actual = estudiante_id
        try:
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            
            # Obtener datos del estudiante
            cursor.execute("SELECT Nombre, Apellido FROM Estudiantes WHERE ID=?", (estudiante_id,))
            nombre, apellido = cursor.fetchone()
            
            # Obtener notas
            cursor.execute("SELECT Practica, Nota FROM Notas WHERE EstudianteID=?", (estudiante_id,))
            notas = cursor.fetchall()
            
            # Calcular acumulados
            total = sum(nota[1] for nota in notas)
            promedio = total / len(notas) if notas else 0
            
            # Crear contenido principal con ScrollView
            main_content = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
            main_content.bind(minimum_height=main_content.setter('height'))
            
            # Información del estudiante
            estudiante_box = BoxLayout(size_hint_y=None, height=60)
            estudiante_box.add_widget(TextInput(
                text=f"Estudiante: {nombre} {apellido}",
                readonly=True,
                font_size='18sp',
                size_hint_x=0.8
            ))
            main_content.add_widget(estudiante_box)
            
            # Encabezado de notas
            encabezado = BoxLayout(size_hint_y=None, height=40)
            encabezado.add_widget(TextInput(
                text="Práctica",
                readonly=True,
                background_color=(0.7, 0.7, 0.7, 1),
                size_hint_x=0.6
            ))
            encabezado.add_widget(TextInput(
                text="Nota",
                readonly=True,
                background_color=(0.7, 0.7, 0.7, 1),
                size_hint_x=0.4
            ))
            main_content.add_widget(encabezado)
            
            # Lista de notas con ScrollView
            notas_scroll = ScrollView(size_hint=(1, None), size_hint_y=None, height=min(400, len(notas)*50))
            notas_container = BoxLayout(orientation='vertical', size_hint_y=None)
            notas_container.bind(minimum_height=notas_container.setter('height'))
            
            for practica, nota in notas:
                nota_box = BoxLayout(size_hint_y=None, height=40)
                nota_box.add_widget(TextInput(
                    text=practica,
                    readonly=True,
                    size_hint_x=0.6
                ))
                nota_box.add_widget(TextInput(
                    text=str(nota),
                    readonly=True,
                    size_hint_x=0.4
                ))
                notas_container.add_widget(nota_box)
            
            notas_scroll.add_widget(notas_container)
            main_content.add_widget(notas_scroll)
            
            # Totales
            totales_box = BoxLayout(size_hint_y=None, height=60)
            totales_box.add_widget(TextInput(
                text=f"Nota Acumulada: {total:.2f}",
                readonly=True,
                background_color=(0.2, 0.7, 0.3, 1),
                size_hint_x=0.5
            ))
            totales_box.add_widget(TextInput(
                text=f"Promedio: {promedio:.2f}",
                readonly=True,
                background_color=(0.2, 0.5, 0.8, 1),
                size_hint_x=0.5
            ))
            main_content.add_widget(totales_box)
            
            self.dialog = MDDialog(
                title=f"Notas de {nombre} {apellido}",
                type="custom",
                content_cls=main_content,
                buttons=[
                    MDFlatButton(
                        text="Agregar Práctica",
                        on_release=lambda x: self.agregar_nota(),
                        size_hint=(0.4, None),
                        height=40
                    ),
                    MDFlatButton(
                        text="Cerrar",
                        on_release=lambda x: self.dialog.dismiss(),
                        size_hint=(0.4, None),
                        height=40
                    )
                ],
                size_hint=(0.9, 0.9)
            )
            self.dialog.open()
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def agregar_nota(self):
        self.dialog.dismiss()
        content = BoxLayout(orientation='vertical', spacing=15, size_hint_y=None, height=200)
        
        # Campo para el nombre de la práctica
        practica_box = BoxLayout(size_hint_y=None, height=60)
        practica_box.add_widget(MDLabel(
            text="Nombre de la práctica:",
            size_hint_x=0.4,
            halign="right"
        ))
        self.nueva_practica = MDTextField(
            hint_text='Ej: Práctica 1',
            size_hint_x=0.6
        )
        practica_box.add_widget(self.nueva_practica)
        content.add_widget(practica_box)
        
        # Campo para la nota
        nota_box = BoxLayout(size_hint_y=None, height=60)
        nota_box.add_widget(MDLabel(
            text="Nota (0-20):",
            size_hint_x=0.4,
            halign="right"
        ))
        self.nueva_nota = MDTextField(
            hint_text='0.00 - 20.00',
            input_filter='float',
            size_hint_x=0.6
        )
        nota_box.add_widget(self.nueva_nota)
        content.add_widget(nota_box)
        
        self.dialog = MDDialog(
            title="Agregar Nueva Calificación",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda x: self.dialog.dismiss(),
                    size_hint=(0.4, None),
                    height=40
                ),
                MDRaisedButton(
                    text="Guardar",
                    on_release=self.guardar_nota,
                    size_hint=(0.4, None),
                    height=40
                )
            ],
            size_hint=(0.8, None)
        )
        self.dialog.open()

    def guardar_nota(self, *args):
        try:
            practica = self.nueva_practica.text.strip()
            nota_text = self.nueva_nota.text.strip()
            
            if not practica:
                raise ValueError("Debe ingresar un nombre para la práctica")
                
            if not nota_text:
                raise ValueError("Debe ingresar una nota")
                
            nota = float(nota_text)
            
            if not (0 <= nota <= 20):
                raise ValueError("La nota debe estar entre 0 y 20")
            
            conn = sqlite3.connect('Base.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Notas (EstudianteID, Practica, Nota) VALUES (?, ?, ?)",
                (self.estudiante_actual, practica, nota)
            )
            conn.commit()
            self.dialog.dismiss()
            self.mostrar_notas(self.estudiante_actual)
            
        except ValueError as e:
            self.dialog.title = f"Error: {str(e)}"
        except Exception as e:
            self.dialog.title = f"Error inesperado: {str(e)}"
        finally:
            if 'conn' in locals():
                conn.close()


class PrinScreen(Screen):
    pass


class MyApp(MDApp):
    def ir_a_start(self,*args):
        self.root.current = 'start'
        self.root.transition.direction = 'right'

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        self.title = 'Aplicacion de Evaluación'
        
        sm = ScreenManager()
        sm.add_widget(PrinScreen(name='start'))
        sm.add_widget(CrearScreen(name="crear"))
        sm.add_widget(VerScreen(name="ver"))
        sm.add_widget(EditarScreen(name="editar"))
        sm.add_widget(FillScreen(name='fill'))
        
        return sm


if __name__ == "__main__":
    MyApp().run()