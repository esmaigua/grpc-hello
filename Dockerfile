# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . /app

# Instala las dependencias
RUN pip install grpcio grpcio-tools

# Expone el puerto donde corre el servidor
EXPOSE 50051

# Comando por defecto para correr el servidor gRPC
CMD ["python", "server.py"]
