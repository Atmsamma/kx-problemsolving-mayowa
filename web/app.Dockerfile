FROM python:latest

USER root

WORKDIR /var/www/

ADD . /var/www/
RUN pip install -r ./requirements.txt
RUN pip install gunicorn


EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]

