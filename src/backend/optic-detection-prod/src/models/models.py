import tensorflow as tf
from tensorflow.keras import layers, regularizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Initialisation du modèle ResNet50 pré-entraîné de Keras
model = tf.keras.models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(512, 512, 3)))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))

model.add(layers.Conv2D(256, (3, 3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))

model.add(layers.Flatten())

model.add(layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.5))

model.add(layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.5))

model.add(layers.Dense(3, activation='softmax'))  # Modifier 5 en 3 pour correspondre au nombre de classes

# Compilation
model.compile(
    optimizer=tf.keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True),
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


# Obtenir le chemin absolu du répertoire parent
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construire le chemin relatif vers le dossier "dataset"
dataset_dir = os.path.join(base_dir, 'dataset')


# Changer le répertoire de travail
#os.chdir('/content/uv_projet_in4_2023/src/backend/optic-detection-prod/src')

# Changer le répertoire de travail
os.chdir('./')

# Obtenir le chemin absolu du répertoire parent
base_dir = os.path.dirname(os.getcwd())

# Construire le chemin relatif vers le dossier "dataset"
dataset_dir = os.path.join(base_dir, 'dataset')




train_generator = train_datagen.flow_from_directory(
    dataset_dir,
    target_size=(512, 512),
    batch_size=batch_size,
    subset='training',
    class_mode='categorical'
)

validation_generator = train_datagen.flow_from_directory(
    dataset_dir,
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

# Enregistrement des poids du modèle pour une utilisation future dans notre API
model.save('./model.h5')
