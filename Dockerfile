FROM python:3.10-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r /temp/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]