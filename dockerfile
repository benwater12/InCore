FROM python:3.6.8

USER 0

RUN mkdir -p /usr/src/app
ADD . /usr/src/app

WORKDIR /usr/src/app
RUN pip install --upgrade pip  &&\
    pip install -r requirements.txt


CMD ["python", "./src/apps.py"]