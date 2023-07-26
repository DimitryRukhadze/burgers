FROM python:3.10

WORKDIR /usr/src/star-burger

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN mkdir bundles
CMD python manage.py runserver 3000
EXPOSE 3000
