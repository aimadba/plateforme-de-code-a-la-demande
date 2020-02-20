FROM python:alpine3.7
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY flask.py /app
ENTRYPOINT [ "python3" ]
CMD  [ "flask.py" ]
