@echo off
echo Starting Text Summarizer App...
call .venv\Scripts\activate.bat
uvicorn app:app --reload
