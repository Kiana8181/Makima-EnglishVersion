FROM python:alpine3.17

WORKDIR /app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

RUN pip install Django

RUN pip install Djangorestframework

RUN pip install django-cors-headers

COPY . .

# Run database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create a superuser (you can customize the username, email, and password)
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('makima', 'admin@example.com', 'makima1381')" | python manage.py shell


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]