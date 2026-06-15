# --- ETAPA 1: Builder ---
# Aquí solo preparamos, no importa si pesa un poco más
FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# --- ETAPA 2: Final (Aquí es donde ocurre la magia de la ligereza) ---
FROM python:3.12-slim

# Instalamos SOLAMENTE el runtime de Tkinter. 
# Esto no instala todo el paquete de desarrollo, solo lo que la app necesita para correr.
RUN apt-get update && apt-get install -y --no-install-recommends \
    libtk8.6 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario para seguridad
RUN useradd --create-home --shell /bin/bash calculatoruser

WORKDIR /app

# Copiamos solo lo necesario del builder
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/lib/python3/dist-packages /usr/lib/python3/dist-packages

# Copiamos tu código
COPY Python-Calculator/src/ ./src/
RUN chown -R calculatoruser:calculatoruser /app/src

USER calculatoruser
WORKDIR /app/src

# ¡Listo! Imagen ligera y con soporte gráfico
CMD ["python", "main.py"]