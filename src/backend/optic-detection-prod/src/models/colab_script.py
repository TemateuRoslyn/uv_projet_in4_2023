import os
from google.colab import drive, notebooks

# Cloner le dépôt Git
!git clone https://github.com/TemateuRoslyn/uv_projet_in4_2023.git

# Monte Google Drive pour accéder au dépôt
drive.mount('/content/drive')

# Navigue jusqu'au dossier contenant les modèles de détection d'optique dans le répertoire du projet cloné
%cd uv_projet_in4_2023/src/backend/optic-detection-prod/src

# Décompresse le jeu de données de détection d'optique
!unzip -q dataset.zip

# Exemple d'entraînement du modèle de détection optique
!python models/models.py
