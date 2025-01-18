FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

ENV SECRET_KEY="django-insecure-k93jv&5xx1(c0sj_iv_d6v7rmol9eif3p50e9mt%@*732mj0kj"
ENV CELERY_BROKER_URL="redis://localhost:6379/0"
ENV CELERY_BACKEND="redis://localhost:6379/0"

RUN mkdir -p /app/media

EXPOSE 8000

CMD EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]