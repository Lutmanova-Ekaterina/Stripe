FROM python:3.11

WORKDIR / code

RUN pip install django
RUN pip install psycopg2-binary
RUN pip install djangorestframework
RUN pip install Pillow
RUN pip install djangorestframework-simplejwt
RUN pip install drf-yasg
RUN pip install requests

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
