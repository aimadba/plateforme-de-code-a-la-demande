#!/usr/bin/python3

from flask import Flask
import requests
import json
import git
import docker

clone_DIR = "./tache"
t="alpine_task"
client = docker.from_env()


# Fonction pour le clonage du depot mocalement

def clone(dep, dire):
        git.Repo.clone_from(dep, dire, branch='master')
#-------------------------------------------------------------

#Fonction pour construire l'image docker a partir du fichier dockerfile pour resoudre la tache 
def build_container(pa,ta):
        client.images.build(path=pa,tag=ta)
#-------------------------------------------------------------------------
#Fonction pour demarrer le conteneur et retourner la resultat de la tache 
def run_container(image):
        res = client.containers.run(image)
        return res
#---------------------------------------------------------------------------

#une requete get pour verifier si il y a des taches si oui en execute le code sinon en affiche que la queue est vide
r = requests.get("http://localhost:5000/rabbit/TODO")   
while r.status_code == 200:

        print("statut : {}".format(r.status_code))
# renvoyer la reponse de la requete au variable et la convertire  
        tache = json.loads(r.text)

# on clone le depot localement depuis l'adresse du git  qui contient un dockerfile et le scripte de la tache
        print("--Clonage du depot------")
        clone(dep=tache["address_git"], dire=clone_DIR)

# on construit l'image alpine qui va executer la tache 
        print("build the docker for the task")
        build_container(pa=clone_DIR,ta=t)

# on demmare le conteneur cree et retourner le reultat dans la variable d
        print("Run the tache docker and return a result")
        d = run_container(image=t)

# on construit le code de la tache resultat qui contient le id projet et id tache precedement retourner
        ta_res = {}
        ta_res["id_projet"] = tache["id_projet"]
        ta_res["id_tache"] = tache["id_tache"]
        #on serialise le resultat pour qu on peut la renvoyer
        ta_res["resultat"] = json.dumps(d.decode("utf-8"))
        tach_res = {"ta" : json.dumps(ta_res)}
# Apres on envoie la tache resultat au queue DONE
        print("envoi tach au queue DONE")
        r1 = requests.post("http://localhost:5000/rabbit/DONE", data$
        print("statut : {}".format(r.status_code))
        print(r.text)
        break
else:
        print("la queue est vide")


