FROM python:3.9-alpine

# Copiar requirements primero para cachear dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorio de trabajo
WORKDIR /app

# Copiar aplicación
COPY app.py .

# Exponer puerto
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]
