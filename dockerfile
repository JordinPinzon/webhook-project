# Usamos una imagen base de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos del proyecto al contenedor
COPY . /app

# Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto en el que Flask estará ejecutándose
EXPOSE 3000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
