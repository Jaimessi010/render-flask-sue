
import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# ======================================
# CONFIGURACION DEL PROYECTO
# ======================================

APP_NAME = "Flask Deploy"
VERSION = "1.0.0"

# ======================================
# PAGINA PRINCIPAL
# ======================================

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Deploy | Railway</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #0b1020;
            color: #ffffff;
            min-height: 100vh;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 25px 8%;
            border-bottom: 1px solid #263047;
        }

        .logo {
            font-size: 23px;
            font-weight: bold;
        }

        .logo span {
            color: #a78bfa;
        }

        .badge {
            background: #173d35;
            color: #6ee7b7;
            border: 1px solid #276b56;
            padding: 9px 16px;
            border-radius: 30px;
            font-size: 13px;
        }

        main {
            max-width: 1100px;
            margin: auto;
            padding: 75px 25px;
        }

        .hero {
            text-align: center;
            margin-bottom: 65px;
        }

        .tag {
            display: inline-block;
            color: #c4b5fd;
            background: #292142;
            padding: 9px 18px;
            border-radius: 30px;
            margin-bottom: 25px;
            font-size: 14px;
        }

        h1 {
            font-size: clamp(34px, 6vw, 58px);
            margin-bottom: 22px;
        }

        h1 span {
            color: #a78bfa;
        }

        .hero p {
            color: #aab5cb;
            font-size: 18px;
            line-height: 1.8;
            max-width: 700px;
            margin: auto;
        }

        h2 {
            font-size: 25px;
            margin-bottom: 25px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 60px;
        }

        .card {
            background: #151d31;
            border: 1px solid #2b3650;
            border-radius: 15px;
            padding: 28px;
        }

        .card .icon {
            font-size: 32px;
            margin-bottom: 20px;
        }

        .card h3 {
            font-size: 20px;
            margin-bottom: 12px;
        }

        .card p {
            color: #aab5cb;
            line-height: 1.7;
            font-size: 14px;
        }

        .pipeline {
            background: #151d31;
            border: 1px solid #2b3650;
            border-radius: 15px;
            padding: 35px;
            margin-bottom: 40px;
        }

        .steps {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
            margin-top: 25px;
        }

        .step {
            background: #202a43;
            border: 1px solid #374562;
            padding: 24px 15px;
            border-radius: 12px;
            text-align: center;
            flex: 1;
        }

        .step strong {
            display: block;
            margin-bottom: 10px;
            color: #c4b5fd;
        }

        .step small {
            color: #aab5cb;
        }

        .arrow {
            font-size: 25px;
            color: #a78bfa;
        }

        .version {
            background: #151d31;
            border: 1px solid #2b3650;
            padding: 28px;
            border-radius: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
        }

        .version p {
            color: #aab5cb;
            margin-top: 8px;
        }

        .version-number {
            color: #6ee7b7;
            font-size: 26px;
            font-weight: bold;
        }

        footer {
            text-align: center;
            padding: 30px;
            color: #7d8ba5;
            border-top: 1px solid #263047;
            font-size: 14px;
        }

        @media (max-width: 700px) {
            header {
                padding: 22px;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .steps {
                flex-direction: column;
            }

            .step {
                width: 100%;
            }

            .arrow {
                transform: rotate(90deg);
            }

            .version {
                flex-direction: column;
                text-align: center;
            }
        }
    </style>
</head>

<body>

    <header>
        <div class="logo">Flask<span>Deploy.</span></div>
        <div class="badge">● Servicio activo</div>
    </header>

    <main>

        <section class="hero">

            <div class="tag">
                PROYECTO DEVOPS · UNIDAD 2
            </div>

            <h1>
                Despliegue continuo <br>
                con <span>Railway</span>
            </h1>

            <p>
                Aplicación web desarrollada con Python y Flask,
                preparada para demostrar la integración con GitHub
                y la automatización del proceso de despliegue
                continuo (CD).
            </p>

        </section>

        <h2>Tecnologías utilizadas</h2>

        <div class="cards">

            <div class="card">
                <div class="icon">🐍</div>
                <h3>Python + Flask</h3>
                <p>
                    Framework utilizado para desarrollar
                    la aplicación web y sus endpoints.
                </p>
            </div>

            <div class="card">
                <div class="icon">📁</div>
                <h3>GitHub</h3>
                <p>
                    Repositorio encargado del control de
                    versiones y de almacenar el código fuente.
                </p>
            </div>

            <div class="card">
                <div class="icon">🚀</div>
                <h3>Railway</h3>
                <p>
                    Plataforma que construye y publica
                    automáticamente las nuevas versiones.
                </p>
            </div>

        </div>

        <section class="pipeline">

            <h2>Pipeline de despliegue continuo</h2>

            <div class="steps">

                <div class="step">
                    <strong>01 · Desarrollo</strong>
                    <small>Visual Studio Code</small>
                </div>

                <div class="arrow">➜</div>

                <div class="step">
                    <strong>02 · Repositorio</strong>
                    <small>Git Push a GitHub</small>
                </div>

                <div class="arrow">➜</div>

                <div class="step">
                    <strong>03 · Despliegue</strong>
                    <small>Railway CD</small>
                </div>

                <div class="arrow">➜</div>

                <div class="step">
                    <strong>04 · Producción</strong>
                    <small>Aplicación disponible</small>
                </div>

            </div>

        </section>

        <div class="version">

            <div>
                <h2 style="margin-bottom:0;">
                    Versión de la aplicación
                </h2>
                <p>
                    Actualizable mediante nuevos commits.
                </p>
            </div>

            <div class="version-number">
                v{{ version }}
            </div>

        </div>

    </main>

    <footer>
        Proyecto académico DevOps |
        Despliegue continuo con Railway
    </footer>

</body>
</html>
    """, version=VERSION)


# ======================================
# ENDPOINT DE SALUD
# ======================================

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "application": APP_NAME,
        "version": VERSION
    })


# ======================================
# INFORMACION DEL PROYECTO
# ======================================

@app.route("/api/info")
def info():
    return jsonify({
        "project": APP_NAME,
        "version": VERSION,
        "framework": "Flask",
        "deployment": "Railway",
        "repository": "render-flask-sue",
        "pipeline": [
            "Desarrollo",
            "GitHub",
            "Railway",
            "Produccion"
        ]
    })


# ======================================
# EJECUCION LOCAL
# ======================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
