FROM python:3.10-slim

# Mettre à jour et installer les dépendances nécessaires, y compris nginx
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Collecter les fichiers statiques de Django
RUN python manage.py collectstatic --noinput

# Copier la configuration Nginx
COPY nginx.conf /etc/nginx/sites-enabled/default

# Copier le script de démarrage
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Exposer le port 80 pour Nginx
EXPOSE 80

# Commande pour démarrer les services
CMD ["/start.sh"]
