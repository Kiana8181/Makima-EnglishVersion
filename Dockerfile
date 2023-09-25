FROM python:alpine3.17

WORKDIR /app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

RUN pip install Django

RUN pip install Djangorestframework

RUN pip install django-cors-headers

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]