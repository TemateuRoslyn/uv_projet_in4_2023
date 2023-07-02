import tensorflow as tf
from tensorflow.keras import models, layers, regularizers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import files


# Initialisation du modèle ResNet50 pré-entraîné de Keras
model = models.Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(512, 512, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(5, activation='softmax'))

# Compilation
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

# Enregistrement des poids du modèle pour une utilisation future dans notre API
model.save('./model.h5')

# Téléchargement des poids
files.download('./model.h5')
