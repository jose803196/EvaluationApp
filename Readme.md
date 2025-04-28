<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EVAP - Sistema de Evaluación Estudiantil</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
            margin-top: 30px;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .screenshots {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            margin: 20px 0;
        }
        .screenshot {
            flex: 0 0 32%;
            margin-bottom: 15px;
            text-align: center;
        }
        .screenshot img {
            max-height: 300px;
        }
        .feature-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .feature-card {
            background: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }
        code {
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .tech-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 20px 0;
        }
        .badge {
            background: #3498db;
            color: white;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        .file-structure {
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            font-family: monospace;
            line-height: 1.8;
        }
    </style>
</head>
<body>
    <h1>EVAP - Sistema de Evaluación Estudiantil</h1>
    
    <p><img src="images/MainScreen.PNG" alt="EVAP Logo" width="200"></p>
    
    <p>EVAP es una aplicación profesional diseñada para gestionar la evaluación de estudiantes de manera eficiente y organizada. Desarrollada con Python y KivyMD, ofrece una interfaz intuitiva para administrar bases de datos estudiantiles, registrar calificaciones y visualizar información académica.</p>
    
    <h2>Características Principales</h2>
    
    <div class="feature-list">
        <div class="feature-card">
            <h3>🗃️ Gestión de bases de datos</h3>
            <p>Completo sistema para administrar información estudiantil con validación de datos y prevención de duplicados.</p>
        </div>
        
        <div class="feature-card">
            <h3>📝 Registro detallado</h3>
            <p>Formularios intuitivos para capturar información personal y académica de los estudiantes.</p>
        </div>
        
        <div class="feature-card">
            <h3>📊 Sistema de calificaciones</h3>
            <p>Registro flexible por prácticas/actividades con cálculo automático de promedios y acumulados.</p>
        </div>
        
        <div class="feature-card">
            <h3>📧 Integración con correo</h3>
            <p>Vinculación con correos electrónicos estudiantiles para futuras funcionalidades de comunicación.</p>
        </div>
        
        <div class="feature-card">
            <h3>📱 Interfaz moderna</h3>
            <p>Diseño responsive y atractivo desarrollado con KivyMD para una experiencia de usuario óptima.</p>
        </div>
    </div>
    
    <h2>Capturas de Pantalla</h2>
    
    <div class="screenshots">
        <div class="screenshot">
            <img src="images/MainScreen.PNG" alt="Main Screen">
            <p>Vista Principal</p>
        </div>
        <div class="screenshot">
            <img src="images/CreateScreen.PNG" alt="Create Screen">
            <p>Crear Base de Datos</p>
        </div>
        <div class="screenshot">
            <img src="images/FillScreen.PNG" alt="Fill Screen">
            <p>Formulario de Estudiante</p>
        </div>
    </div>
    
    <h2>Instalación y Uso</h2>
    
    <h3>1. Requisitos del sistema:</h3>
    <ul>
        <li>Python 3.7 o superior</li>
        <li>Pip (gestor de paquetes de Python)</li>
    </ul>
    
    <h3>2. Instalación de dependencias:</h3>
    <pre><code>pip install kivy kivymd sqlite3</code></pre>
    
    <h3>3. Ejecución de la aplicación:</h3>
    <pre><code>python main.py</code></pre>
    
    <h2>Funcionalidades Detalladas</h2>
    
    <h3>1. Gestión de Base de Datos</h3>
    <ul>
        <li>Creación automática de tablas relacionales (Estudiantes y Notas)</li>
        <li>Validación de campos obligatorios</li>
        <li>Prevención de duplicados por cédula de identidad</li>
        <li>Almacenamiento seguro en SQLite</li>
    </ul>
    
    <h3>2. Registro de Estudiantes</h3>
    <ul>
        <li>Formulario intuitivo con validaciones</li>
        <li>Almacenamiento de información completa:
            <ul>
                <li>Nombres y apellidos</li>
                <li>Cédula de identidad</li>
                <li>Correo electrónico</li>
            </ul>
        </li>
        <li>Mensajes de confirmación y errores</li>
    </ul>
    
    <h3>3. Sistema de Calificaciones</h3>
    <ul>
        <li>Registro detallado por prácticas/actividades</li>
        <li>Cálculo automático de:
            <ul>
                <li>Nota acumulada</li>
                <li>Promedio general</li>
            </ul>
        </li>
        <li>Visualización clara de historial académico</li>
        <li>Validación de rangos (0-20)</li>
    </ul>
    
    <h3>4. Consulta de Información</h3>
    <ul>
        <li>Listado completo de estudiantes</li>
        <li>Visualización detallada por estudiante</li>
        <li>Actualización en tiempo real</li>
    </ul>
    
    <h2>Estructura del Código</h2>
    
    <p>La aplicación sigue una arquitectura modular basada en pantallas (screens):</p>
    
    <div class="file-structure">
        EVAP/<br>
        ├── main.py                # Punto de entrada principal<br>
        ├── screens/<br>
        │   ├── principal.py       # Pantalla de inicio<br>
        │   ├── crear.py          # Creación de base de datos<br>
        │   ├── llenar.py         # Formulario de estudiantes<br>
        │   ├── ver.py            # Visualización de datos<br>
        │   └── editar.py         # Gestión de calificaciones<br>
        └── Base.db               # Base de datos SQLite
    </div>
    
    <h2>Tecnologías Utilizadas</h2>
    
    <div class="tech-badges">
        <span class="badge">Python</span>
        <span class="badge">KivyMD</span>
        <span class="badge">SQLite3</span>
        <span class="badge">MVC</span>
        <span class="badge">OOP</span>
    </div>
    
    <h2>Contribución</h2>
    
    <p>¡Las contribuciones son bienvenidas! Por favor sigue estos pasos:</p>
    
    <ol>
        <li>Haz un fork del proyecto</li>
        <li>Crea una rama para tu feature (<code>git checkout -b feature/AmazingFeature</code>)</li>
        <li>Haz commit de tus cambios (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
        <li>Haz push a la rama (<code>git push origin feature/AmazingFeature</code>)</li>
        <li>Abre un Pull Request</li>
    </ol>
    
    <h2>Licencia</h2>
    
    <p>Distribuido bajo la licencia MIT. Consulta el archivo <code>LICENSE</code> para más información.</p>
    
    <h2>Contacto</h2>
    
    <p>Para preguntas o sugerencias, por favor contacta al desarrollador:</p>
    
    <ul>
        <li>Email: <a href="mailto:tu-email@example.com">tu-email@example.com</a></li>
        <li>GitHub: <a href="https://github.com/tu-usuario" target="_blank">@tu-usuario</a></li>
    </ul>
    
    <hr>
    
    <p><strong>EVAP</strong> - Simplificando la evaluación académica desde 2023</p>
</body>
</html>