FROM --platform=linux/amd64 python:3.9.20-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "urco/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

