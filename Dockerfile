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
    pip install -r app/requirements.txt

# Expõe porta (ajuste se não for 8000)
EXPOSE 8000

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
