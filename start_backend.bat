@echo off
REM Ativa o ambiente virtual
call venv\Scripts\activate.bat

REM Verifica se a ativação deu certo e uvicorn está disponível
where uvicorn >nul 2>&1
if %errorlevel% neq 0 (
    echo Erro: Uvicorn nao encontrado. Execute este script com o terminal do Git Bash:
    echo.
    echo source venv/Scripts/activate
    echo uvicorn app.main:app --reload
    pause
    exit /b
)

REM Inicia o backend com Uvicorn
uvicorn app.main:app --reload
pause
