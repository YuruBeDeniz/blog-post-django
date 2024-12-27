FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY wait-for-it.sh /app/wait-for-it.sh

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash", "/app/wait-for-it.sh", "database:5432", "--timeout=30", "--", "bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
