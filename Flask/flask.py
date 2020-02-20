#!/usr/bin/python3

from flask import Flask , request
import json
import requests
import pika


#Creation d'unr instance du Serveur FLASK avec le nom app
app = Flask(__name__)
#-----------------------------------------------------------------------------------------------------------

# Definir les parametres de connection au Rabbitmq ainsi que initialiser une connexion
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('0.0.0.0',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
#--------------------------------------------------------------------------------------------------------------

#Foction pour cree une file "TO DO /DONE "qui prend en parametre le nom de la file
def creat_queue(queue):
	channel.queue_declare(queue=queue)
	return ("you created a queue ")

#--------------------------------------------------------------------------------------------------------------

#Fonction pour ajouter une tache au file deja cree et prend en parametre le nom de la file et le message= la tache
def write_queue(message,queue):
	channel.basic_publish(exchange='',routing_key=queue, body=message)
	connection.close()
	return ("you sent a message to {}".format(queue))

#--------------------------------------------------------------------------------------------------------------

#Fonction pour lire un message  ou tache depuis la file "TO DO / DONE" 
def read_queue(queue):
	method_frame,header_frame,body=channel.basic_get$
	if method_frame:
		print(method_frame, header_frame, body)
		channel.basic_ack(method_frame.delivery_$
		return (body)
	else:
		print(" Rien à lire ")
#---------------------------------------------------------------------------------------------------------------

# Le code du Service qui permet la creation d'une file "DONE ET TODO" 
@app.route("/rabbit",methods=['POST'])
def crea_Q():
	res = json.loads(request.form.get("queue"))
    name = res["file"]
    creat_queue(queue = name)
    return ("vous avez cree une queue = {} ".format(res["file"]))
#-----------------------------------------------------------------------------------------------------------------

# le code du service qui permet le depot d'un message=tache dans une file
@app.route("/rabbit/<nom_file>",methods=['POST'])
def depo_M(nom_file=None):
   	res = json.loads(request.form.get("ta"))
    r = json.dumps(res)
    f = nom_file
    write_queue(queue=f,message=r)  
    return ("message sent to queue successfully")

#-----------------------------------------------------------------------------------------------------------------

#Le code du service qui permet la lecture d'un message dans une file
@app.route("/rabbit/<nom_file>",methods=['GET'])
def read_M(nom_file=None):
        x = read_queue(nom_file)
        return x
#-----------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
#Pour demarre le serveur Flask et etre pret pour recevoir les requetes
	app.run()
#-----------------------------------------------------------------------------------------------------------------