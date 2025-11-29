FROM alpine:latest

# Instalar herramientas básicas
RUN apk add --no-cache curl python3 py3-pip && \
    pip3 install flask

# Crear directorio de trabajo
WORKDIR /app

# Copiar script de la aplicación
COPY app.py .

# Exponer puerto
EXPOSE 5000

# Comando por defecto
CMD ["python3", "app.py"]
