# Imagen base Python
FROM python:3.11

# Directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Puerto para web
EXPOSE 5000

# Ejecutar app
CMD ["python", "app.py"]