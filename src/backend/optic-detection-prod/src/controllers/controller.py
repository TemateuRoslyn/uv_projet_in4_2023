import numpy as np
import tensorflow as tf
import cv2

# Charger le modèle ResNet-50 enregistré sous forme de fichier h5 (après entrainement du modèle)
model = tf.keras.models.load_model('./../models/model.h5')

# Mapping des classes avec les étiqettes
CLASS_MAPPING = {
    0: "aucune maladie oculaire détectée",
    1: "cataracte",
    2: "glaucome",
    3: "rétinopathie diabétique",
    4: "autre"
}

# Fonction pour la reconnaissance de forme de l'image soumise par l'utilisateur
def detect_disease_from_image(image):
    # Chargement de l'image soumise par l'utilisateur
    img_np = np.fromfile(image, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    # Prétraitement de l'image
    image = cv2.resize(img, (512, 512))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)
    # Passage de l'image dans le réseau de neurones pour la reconnaissance de forme
    prediction = model.predict(image)[0]
    # Extraction de la classe avec la plus haute probabilité
    class_idx = np.argmax(prediction)
    disease = CLASS_MAPPING[class_idx]

    return disease
