FROM python:3.8

WORKDIR /olx

COPY . /olx/
COPY requirements.txt .

RUN ["pip", "install", "-r", "requirements.txt"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]