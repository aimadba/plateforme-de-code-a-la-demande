#!/usr/bin/python3

from flask import Flask , render_template , request
import json
import requests
import pika


app = Flask(__name__)


credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('0.0.0.0',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()



@app.route("/rabbit",methods=['POST'])
def creat_file(queue=None):
    r = json.loads(request.form.get("na"))
    channel.queue_declare(queue = r["name"])
    print("-- Queue cree---")
    #return render_template("crea.html", data1=queue)
    return ("vous avez cree une queue = {} ".format(r["name"]))




@app.route("/rabbit/bbFG/",methods=['POST'])
def depo_m(message=None):
    re = json.loads(request.form.get("na"))
    name = re ["name"]
    message = re ["message"]
    channel.basic_publish(exchange='', routing_key=name, body=message)
    print("-- message envoye au queue---")
    connection.close()
    return ("vous avez envoyer le message ""{}"" au queue : {}".format(message, name))



@app.route("/rabbit/bbFG/",methods=['GET'])
def lec_m():
    def callback(ch, method, properties, body):
        print("reception de %r" % body)
    
    re = json.loads(request.form.get("na"))
    name = re ["name"]
    x = channel.basic_consume(queue=name, on_message_callback=callback, auto_ack=True)
    print("en attent s'un message")
    channel.start_consuming()
    return print (json.dumps(x))

if __name__ == "__main__":
    app.run()

