<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="EVAP - Sistema de Evaluación Estudiantil para la gestión y evaluación eficiente de estudiantes con Python y KivyMD.">
    <style>  
        body {  
            font-family: Arial, sans-serif;  
            line-height: 1.6;  
            background-color: #f9f9f9;  
            margin: 0;  
            padding: 20px;  
        }  
        
        header {  
            text-align: center;  
            background: #4CAF50;  
            color: white;  
            padding: 10px 0;  
            border-radius: 5px;  
        }  

        h1 {  
            margin: 0;  
            font-size: 2.5em;  
        }  

        h2 {  
            color: #333;  
            border-bottom: 2px solid #4CAF50;  
            padding-bottom: 5px;  
        }  

        main {  
            margin: 20px auto;  
            max-width: 800px;  
            background: white;  
            padding: 20px;  
            border-radius: 5px;  
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);  
        }  

        ul {  
            list-style-type: none;  
            padding: 0;  
        }  

        li {  
            background: #f2f2f2;  
            margin: 5px 0;  
            padding: 10px;  
            border-radius: 5px;  
        }  

        .features {  
            display: flex;  
            flex-wrap: wrap;  
            gap: 20px;  
        }  

        .feature-card {  
            flex: 1 1 calc(50% - 20px);  
            min-width: 300px;  
            background: #e9ffe9;  
            padding: 15px;  
            border-radius: 5px;  
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);  
        }  

        .screenshots {  
            display: flex;  
            flex-wrap: wrap;  
            gap: 15px;  
        }  

        .screenshot {  
            flex: 1 1 calc(33% - 15px);  
            min-width: 200px;  
        }  

        .screenshot img {  
            width: 100%;  
            border-radius: 5px;  
        }  

        .screenshot-caption {  
            text-align: center;  
            font-weight: bold;  
            margin-top: 5px;  
        }  

        .tech-stack {  
            display: flex;  
            flex-direction: column;  
            margin-top: 10px;  
        }  

        .tech-item {  
            padding: 10px;  
            background-color: #e7f3fe; /* Color claro para los badges */  
            border-left: 5px solid #2196F3; /* Línea a la izquierda */  
            margin: 5px 0;  
            border-radius: 5px;  
        }  

        /* Responsividad */  
        @media (max-width: 600px) {  
            .feature-card {  
                flex: 1 1 100%;  
            }  

            .screenshot {  
                flex: 1 1 100%;  
            }  
        }  
    </style>
</head>

<body>
    <header role="banner" aria-label="Encabezado de EVAP">
        <h1>EVAP</h1>
        <p>Sistema de Evaluación Estudiantil</p>
    </header>
    <main>
        <span style="display: flex; align-items: center;gap:15px">
            <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=green" alt="Python version">
            <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License MIT">
            <img src="https://img.shield.io/kivy/kivy/master/kivy/data/logo/kivy-icon-256.png">
            <img src="https://kivymd.readthedocs.io/en/latest/_static/logo-kivymd.png" alt="Logo" style="margin-left: 8px; width:25px; margin-right:8px;"/> 
            <img src="https://img.shields.io/badge/KivyMD-1.1.1-blue" alt="KivyMD Badge"/>  
        </span>
        <section aria-labelledby="descripcion">
            <h2 id="descripcion">Descripción</h2>
            <p>EVAP es una aplicación profesional diseñada para facilitar la gestión y evaluación de estudiantes. Desarrollada con Python y KivyMD, ofrece una interfaz moderna e intuitiva para administrar información académica de manera eficiente.</p>
        </section>
        <section aria-labelledby="caracteristicas" class="features">
            <h2 id="caracteristicas">Características</h2>
            <ul role="list" class="features">
                <li class="feature-card">
                    <h3>Gestión de Estudiantes</h3>
                    <p>Registro completo de estudiantes con nombres, apellidos, cédula de identidad y correo electrónico.</p>
                </li>
                <li class="feature-card">
                    <h3>Sistema de Calificaciones</h3>
                    <p>Asignación y edición de notas por práctica, con cálculo automático de promedio y acumulados.</p>
                </li>
                <li class="feature-card">
                    <h3>Base de Datos Segura</h3>
                    <p>Almacenamiento local con SQLite, garantizando integridad y disponibilidad de los datos.</p>
                </li>
                <li class="feature-card">
                    <h3>Interfaz Intuitiva</h3>
                    <p>Diseño responsive y accesible, con transiciones fluidas entre pantallas.</p>
                </li>
            </ul>
        </section>
        <section aria-labelledby="caracteristicas-principales">
            <h2 id="caracteristicas-principales">Características Principales</h2>
            <ul>
                <li><strong>Creación de base de datos</strong> con información completa de estudiantes.</li>
                <li><strong>Visualización detallada</strong> de registros estudiantiles.</li>
                <li><strong>Edición avanzada</strong> de calificaciones con validación de datos.</li>
                <li><strong>Sistema de promedios</strong> automático.</li>
                <li><strong>Validación de campos</strong> para garantizar datos correctos.</li>
                <li><strong>Mensajes de feedback</strong> para operaciones exitosas o errores.</li>
            </ul>
        </section>
        <section aria-labelledby="capturas-pantalla">
            <h2 id="capturas-pantalla">Capturas de Pantalla</h2>
            <div class="screenshots" role="list">
                <div class="screenshot" role="listitem">
                    <img src="images/MainScreen.PNG" alt="Pantalla Principal de EVAP">
                    <div class="screenshot-caption">Pantalla Principal</div>
                </div>
                <div class="screenshot" role="listitem">
                    <img src="images/CreateScreen.PNG" alt="Pantalla de Creación de Base de Datos de EVAP">
                    <div class="screenshot-caption">Creación de Base de Datos</div>
                </div>
                <div class="screenshot" role="listitem">
                    <img src="images/FillScreen.PNG" alt="Pantalla de Registro de Estudiantes de EVAP">
                    <div class="screenshot-caption">Registro de Estudiantes</div>
                </div>
            </div>
        </section>
        <section aria-labelledby="tecnologias">
            <h2 id="tecnologias">Tecnologías Utilizadas</h2>
            <ul class="tech-stack" role="list">
                <li class="tech-item"><span class="badge">Python</span> Lenguaje principal</li>
                <li class="tech-item"><span class="badge">KivyMD</span> Interfaz gráfica</li>
                <li class="tech-item"><span class="badge">SQLite</span> Base de datos</li>
                <li class="tech-item"><span class="badge">Material Design</span> Estilo visual</li>
            </ul>
        </section>
        <section aria-labelledby="estructura-bd">
            <h2 id="estructura-bd">Estructura de la Base de Datos</h2>
            <p>La aplicación crea automáticamente una base de datos SQLite llamada <code>Base.db</code> con las siguientes tablas:</p>
            <ul>
                <li><strong>Estudiantes</strong>: Almacena información personal de los estudiantes</li>
                <li><strong>Notas</strong>: Registra las calificaciones asociadas a cada estudiante</li>
            </ul>
        </section>
        <section aria-labelledby="flujo-trabajo">
            <h2 id="flujo-trabajo">Flujo de Trabajo</h2>
            <ol>
                <li>Crear la estructura de la base de datos</li>
                <li>Registrar estudiantes con sus datos personales</li>
                <li>Visualizar y administrar los registros existentes</li>
                <li>Asignar y editar calificaciones por práctica</li>
                <li>Consultar promedios y notas acumuladas</li>
            </ol>
        </section>
        <section aria-labelledby="requisitos">
            <h2 id="requisitos">Requisitos del Sistema</h2>
            <ul>
                <li>Python 3.x</li>
                <li>Bibliotecas: Kivy, KivyMD, SQLite3</li>
                <li>Sistema operativo: Windows, Linux o macOS</li>
            </ul>
        </section>
        <section aria-labelledby="instalacion">
            <h2 id="instalacion">Instalación</h2>
            <p>Para ejecutar EVAP, siga estos pasos:</p>
            <ol>
                <li>Instale Python 3.x desde <a href="https://www.python.org/downloads/" target="_blank" rel="noopener">python.org</a></li>
                <li>Instale las dependencias necesarias:
                    <pre><code lang="bash">pip install kivy kivymd sqlite3</code></pre>
                </li>
                <li>Descargue los archivos de la aplicación</li>
                <li>Ejecute el archivo principal:
                    <pre><code lang="bash">python main.py</code></pre>
                </li>
            </ol>
        </section>
        <section aria-labelledby="licencia">
            <h2 id="licencia">Licencia</h2>
            <p>Este proyecto está bajo licencia MIT. Consulte el archivo LICENSE para más detalles.</p>
        </section>
    </main>
</body>
</html>