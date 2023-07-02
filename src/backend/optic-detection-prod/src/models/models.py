import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from google.colab import files

# Initialisation du modèle ResNet50 pré-entraîné de Keras
resnet_model = tf.keras.applications.ResNet50(
    include_top=False,
    input_shape=[512, 512, 3],
    weights='imagenet'
)

# Congelation de l'ensemble des couches du modèle pré-entraîné ResNet50
for layer in resnet_model.layers:
    layer.trainable = False

# Ajout des couches Dense pour la classification à la fin du modèle
x = layers.Flatten()(resnet_model.output)
x = layers.Dense(2048, activation='relu')(x)
x = layers.Dropout(0.5)(x)
x = layers.BatchNormalization()(x)

x = layers.Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.01))(x)
x = layers.Dropout(0.5)(x)
x = layers.BatchNormalization()(x)

x = layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.01))(x)
x = layers.Dropout(0.5)(x)
x = layers.BatchNormalization()(x)

x = layers.Dense(256, activation='relu')(x)
x = layers.Dropout(0.5)(x)
x = layers.BatchNormalization()(x)

x = layers.Dense(128, activation='relu')(x)
x = layers.Dropout(0.5)(x)
x = layers.BatchNormalization()(x)

output_layer = layers.Dense(5, activation='softmax')(x)

# Création de notre modèle de reconnaissance de forme basée sur le ResNet50 et les couches de classification ajoutées
model = models.Model(resnet_model.input, output_layer)

# Compilation du modèle avec les paramètres nécessaires pour l'entraînement
model.compile(
    optimizer=tf.keras.optimizers.SGD(lr=0.01, decay=0.01),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Préparation de l'ensemble de données et des générateurs de données pour l'entraînement et la validation
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=90,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    vertical_flip=True,
    validation_split=0.3
)

batch_size = 16

train_generator = train_datagen.flow_from_directory(
    './../dataset',
    target_size=(512, 512),
    batch_size=batch_size,
    subset='training',
    class_mode='categorical'
)

validation_generator = train_datagen.flow_from_directory(
    './../dataset',
    target_size=(512, 512),
    batch_size=batch_size,
    subset='validation',
    class_mode='categorical'
)

# Entrainement du modèle à l'aide des données d'entraînement et des données de validation
model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=100,
    verbose=1
)

model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=100,
    verbose=1,
    steps_per_epoch=train_generator.n
)
# Enregistrement des poids du modèle pour une utilisation future dans notre API
model.save('./model.h5')
