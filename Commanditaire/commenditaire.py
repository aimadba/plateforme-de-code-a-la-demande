#!/usr/bin/python3

from flask import Flask
import requests
import json


# CREATION DES FILES "TODO" ET "DONE"
list_queue = {"TODO", "DONE"}
for i in list_queue:
        que = {}
        que["file"] = i
        d = {"queue" : json.dumps(que)}
        r = requests.post("http://localhost:5000/rabbit", data=d)
        print("statut : {}".format(r.status_code))
        print(r.text)

#----------------------------------------------------------------------

#Generation de la tache a resoudre
	tache = {}
	tache{"id_projet"} = 100
	tache["id_tache"] = 10
	tache["address_git"] = "https://github.com/aimadba/DockerFile_tache.git"
	tache["command"] = "python3 tache.py"
#Conversion du python en JSON
task = {"ta" : json.dumps(tache)}

#Envoi de la tache au file TO DO
r = requests.post("http://localhost:5000/rabbit/TODO", data=task)
print("statut : {}".format(r.status_code))
print(r.text)

# connection au rabbitmq et ecoute pour lire les messages dans la file DONE et  
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
def callback(ch, method, properties, body):
    print("reception de %r" % body)

channel.basic_consume(queue="DONE", on_message_callback=callback, auto_ack=True)
print("en attent s'un message")
rss = channel.start_consuming()

print (rss)