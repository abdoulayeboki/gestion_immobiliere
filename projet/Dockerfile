FROM python:3.7.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
CMD python manage.py runserver 0.0.0.0:8000
# RUN python manage.py createsuperuser --username admin --email admin@gmail.com

