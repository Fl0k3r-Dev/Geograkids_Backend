Iniciar projeto com uv (servidor interno da aplicação)

venv\Scripts\activate => CASO O COMANDO ABAIXO NAO RODE
uvicorn app.main:app --reload => EXECUTA PROJETO

Para configurar o ambiente Python:

Instalar python com variável de ambiente definida
Instalar fastapi com o pip: pip install fastapi
Instalar sqlalchemy para gerenciar o banco de dados: pip install sqlalchemy
Instalar o gerenciado do MySQL do PYTHON: pip install pymysql

Endereço local do swagger: http://127.0.0.1:8000/docs
Requisições serão feitas no endereço: http://127.0.0.1:8000