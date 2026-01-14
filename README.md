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

