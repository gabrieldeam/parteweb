@echo off
REM Ativar o ambiente virtual
call venv\Scripts\activate.bat

REM Executar o aplicativo Flet
python app.py

REM Manter a janela aberta após a execução
pause
