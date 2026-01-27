---
title: Devops Ml
emoji: 🚀
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
app_port: 8000
---

# devops-ml

## télécharger les dépendances
```bash
se mettre à la racine du projet

pip install --no-cache-dir -r api/requirements.txt
```

## lancer le serveur fastapi
```bash
uvicorn api.main:app --reload
```

## utiliser les APIs sur le swagger
```
http://127.0.0.1:8000/docs
```

## déploiment
Le backend a été déployé sur Huggingface space à l'adresse suivante
```
https://matyschampeyrol-devops-ml.hf.space

#pour acceder au swagger et tester l'api de classification de mail
https://matyschampeyrol-devops-ml.hf.space/docs
```





