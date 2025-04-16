FROM python:3.12-slim

WORKDIR /app

COPY . .

# --no-cache-dir if an issue installing requirements
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "mainapp.py", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false", "--server.fileWatcherType", "none"]
