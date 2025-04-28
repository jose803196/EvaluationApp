<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="EVAP - Sistema de Evaluación Estudiantil para la gestión y evaluación eficiente de estudiantes con Python y KivyMD.">
    <title>EVAP - Sistema de Evaluación Estudiantil</title>
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <style>
        body{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        header{
            text-align: center;
            padding: 30px 0;
            background: linear-gradient(135deg, #00bcd4,rgba(24, 186, 215, 0.89));
            color: white;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(179, 0, 255, 0.2);
        }
        h1{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }
        h2{
            color: #008ba3;
            border-bottom: 2px solid #00bcd4;
            padding-bottom: 5px;
            margin-top: 30px;
        }
        .badge{
            display: inline-block;
            padding: 3px 8px;
            background-color: #00bcd4;
            color: white;
            border-radius: 4px;
            font-size: 0.8em;
            margin-right: 5px;
        }
        .tech-item {
            display: inline-block;
            margin-right: 15px;
            margin-bottom: 10px;
        }
        .features {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin: 20px 0;
        }
        .feature-card {
            flex: 1 1 250px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-left: 4px solid #00bcd4;
        }
        .screenshots {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
            margin: 25px 0;
        }
        .screenshot {
            border: 1px solid #ddd;
            border-radius: 6px;
            overflow: hidden;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .screenshot:hover {
            transform: translateY(-5px);
        }
        .screenshot img {
            max-width: 200px;
            display: block;
        }
        .screenshot-caption {
            text-align: center;
            padding: 8px;
            background: #f5f5f5;
            font-size: 0.9em;
        }
        code {
            background-color: #f0f0f0;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
        }
        pre code {
            display: block;
            padding: 10px;
            background: #f0f0f0;
            border-radius: 5px;
        }
        .tech-stack {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
    </style>
</head>

<body>
    <header role="banner" aria-label="Encabezado de EVAP">
        <h1>EVAP</h1>
        <p>Sistema de Evaluación Estudiantil</p>
    </header>
    <main>
        <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=green" alt="Python version">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License MIT">
        <img src="https://img.shield.io/kivy/kivy/master/kivy/data/logo/kivy-icon-256.png">
        <span style="display: flex; align-items: center;">
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