FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# RUN echo "export STREAMLIT_SERVER_HEADLESS=true" >> ~/.bashrc
# RUN echo "export STREAMLIT_SERVER_PORT=8501" >> ~/.bashrc
# RUN echo "export STREAMLIT_SERVER_ENABLE_CORS=false" >> ~/.bashrc
# RUN echo "export STREAMLIT_SERVER_RUN_ON_SAVE=false" >> ~/.bashrc
# RUN echo "export STREAMLIT_SERVER_ENABLE_XSRF=false" >> ~/.bashrc
# RUN echo "export STREAMLIT_DISABLE_BROWSER=true" >> ~/.bashrc

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.enableCORS", false, "--server.enableXsrfProtection", false]
