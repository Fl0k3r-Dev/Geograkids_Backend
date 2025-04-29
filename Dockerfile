# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . /app

# Ativa ambiente virtual
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Instala dependências
RUN python -m venv $VIRTUAL_ENV && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta correta (8080)
EXPOSE 8080

# Comando de inicialização corrigido
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
