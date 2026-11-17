FROM python:3.12-slim
WORKDIR /srv
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
COPY wsgi.py .
EXPOSE 8000
# A Render a PORT környezeti változót adja, lokálisan 8000
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT:-8000} wsgi:app"]
