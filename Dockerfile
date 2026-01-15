# Utiliser une image Python officielle
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY api/requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code dans le conteneur
COPY . .

# Exposer le port sur lequel ton API va tourner
EXPOSE 8000

# Commande par défaut pour lancer ton API
CMD ["python", "api/main.py"]
