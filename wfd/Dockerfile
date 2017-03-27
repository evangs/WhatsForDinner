FROM python:2.7-alpine
LABEL maintainer "esailer@asu.edu"
RUN apk add --update \
    nginx
RUN mkdir -p /run/nginx
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN rm -v /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python manage.py collectstatic --noinput
EXPOSE 80
CMD [ "/bin/ash", "startapp"]