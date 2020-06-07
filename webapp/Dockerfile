FROM python:3.8-buster

RUN mkdir /django

ADD requirements.txt.frozen /django

WORKDIR /django

RUN pip install -r requirements.txt.frozen

ADD . /django

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
