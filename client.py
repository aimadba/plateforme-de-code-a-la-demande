#!/usr/bin/python3

from flask import Flask
import requests
import json



dat = {}
dat["name"] = "bb"
dat["message"] = "this is the Msg"


d = {"na" : json.dumps(dat)}

r = requests.post("http://localhost:5000/rabbit", data=d)
print("statut : {}".format(r.status_code))
print(r.text)

r = requests.post("http://localhost:5000/rabbit/bbFG/", data=d)
print("statut : {}".format(r.status_code))
print(r.text)

r = requests.get("http://localhost:5000/rabbit/bbFG/", data=d)
print("statut : {}".format(r.status_code))
data = json.loads(r)
print(data)

