# plateforme-de-code-a-la-demande

L'architecture est compose de deux acteurs:
- un commanditaires qui proposent des taches a executer
- un Worker qui choisissent les taches a executer

La plateforme est constituée de différents services d’infrastructure:
- Un service de publication des tâches
- Un service de stockage des codes à exécuter
- Un service de stockage des données associées aux codes à exécuter


Le fonctionnement:
1 Un commanditaire publie un ensemble de tâches réaliser.
2 Un worker va chercher sur la plateforme de publication un job à effectue:
  - Si le worker ne détient pas le code associé, il télécharge le code à exécuter.
  - Le worker installe et configure, si nécessaire, le code à exécuter.
  - Le worker télécharge,si nécessaire,les données nécessaires à l’exécution de la tâche choisie.
  - Le worker exécute le code en exploitant les données précédemment obtenues.
  - Le worker stocke le résultat obtenu sur le service de stockage des résultats.
3 Le commanditaire récupère le résultat obtenus.
 
