FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y \\\\
    gcc \\\\
    libpq-dev \\\\
    && apt-get clean \\\\
    && rm -rf /var/lib/apt/lists/* \

COPY requirements.txt/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]