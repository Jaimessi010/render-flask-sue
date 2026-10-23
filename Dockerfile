
# Imagen base de Python
FROM python:3.13-slim

# Directorio de trabajo
WORKDIR /app

# Evitar archivos temporales y buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copiar dependencias
COPY requirements.txt .

# Instalar Flask y Gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el codigo del proyecto
COPY . .

# Puerto de la aplicacion
EXPOSE 5001

# Ejecutar Flask con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
