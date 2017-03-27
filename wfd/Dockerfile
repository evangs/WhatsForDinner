FROM python:3.5-alpine
LABEL maintainer "esailer@asu.edu"
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python manage.py collectstatic --noinput
EXPOSE 80
CMD [ "python", "server.py"]