import tensorflow as tf
from keras import datasets, layers, models
import keras
import numpy as np
from glob import glob
import os
from sklearn.model_selection import train_test_split

array = []
spectrograms = glob('/Users/michaellevins/Downloads/Data/spectrograms/*')

count = 0
features = []
labels = []
genres = ['pop', 'metal', 'disco', 'blues', 'reggae', 'classical', 'rock', 'hiphop', 'country', 'jazz']

for folder in spectrograms:
    genre = folder.split('_')[1]
    for filename in os.listdir(folder):
        with open(os.path.join(folder, filename), 'rb') as f:
            #print(f'filename type: {type(filename)} filename: {filename}')
            specType = filename.split('_')[1]
            if specType == 'mel':
                spec = np.load(f)
                features.append(spec)
                label = genres.index(genre)
                labels.append(label)
                count += 1

print(f'Saved {count} mel spectrograms')
np.random.shuffle(features)
np.random.shuffle(labels)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33)


mel_model = models.Sequential()
mel_model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(None, 128, 1293)))
mel_model.add(layers.MaxPooling2D((2, 2)))
mel_model.add(layers.Conv2D(64, (3, 3), activation='relu'))
mel_model.add(layers.MaxPooling2D((2, 2)))
mel_model.add(layers.Conv2D(64, (3, 3), activation='relu'))
mel_model.compile(
    optimizer=keras.optimizers.legacy.RMSprop(),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy()]
)

mel_model.fit(x=features_train, y=labels_train, verbose=1, validation_data=(features_test, labels_test), epochs=64, batch_size=32)
score = mel_model.evaluate(x=features_test, y=labels_test, verbose=0)
print(f'Accuracy: {str(score[1]*100)} %')
