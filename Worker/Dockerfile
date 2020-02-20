FROM python:alpine3.7
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY worker.py /app
ENTRYPOINT [ "python3" ]
CMD  [ "worker.py" ]
