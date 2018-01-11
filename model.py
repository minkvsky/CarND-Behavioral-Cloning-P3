import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import math

# data
DATA_PATH = 'data'
df = pd.read_csv(os.path.join(DATA_PATH, 'driving_log.csv'))
train_df, valid_df = train_test_split(df, test_size=0.2)

# constants
number_of_epochs = 8
batch_size = 64
steps_per_epoch = math.ceil(len(train_df) * 3 / batch_size)
validation_steps = math.ceil(len(valid_df) * 3 /batch_size)
learning_rate = 1e-3

# import for model
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, Lambda, Cropping2D
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from utils import image_resize, loss_plot
import utils

# model achitecture
model = Sequential()
model.add(Lambda(lambda x: (x /255.0) - 0.5, input_shape=(160,320,3)))
model.add(Cropping2D(cropping=((50, 20),(0, 0))))
model.add(Lambda(image_resize))

model.add(Conv2D(filters=24, kernel_size=(5,5), strides=(2,2), padding='valid', activation='relu'))

model.add(Conv2D(filters=36, kernel_size=(5,5), strides=(2,2), padding='valid', activation='relu'))

model.add(Conv2D(filters=48, kernel_size=(5,5), strides=(2,2), padding='valid', activation='relu'))

model.add(Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu'))

model.add(Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu'))


model.add(Flatten())
model.add(Dense(1164, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

model.summary()
model.compile(loss='mse', optimizer=Adam(learning_rate))
# output model.summary() to markdown
import time
start = time.time()
model_ver = '-'.join([str(x) for x in time.localtime(start)[:5]])
with open('tuning_param/model_summary_{}.md'.format(model_ver), 'w') as f:
    model.summary(print_fn=lambda x: f.write(x + '\n'))

# load data generator
train_gen = utils.generate_batch(train_df)
valid_gen = utils.generate_batch(valid_df)

# training
checkpointer = ModelCheckpoint(filepath='model.h5',
                               verbose=1, save_best_only=True)
hist = model.fit_generator(train_gen,
                    steps_per_epoch = steps_per_epoch,
                    validation_data=valid_gen,
                    validation_steps=validation_steps,
                    callbacks=[checkpointer],
                    epochs=number_of_epochs,
                    verbose=1)
# output hist
import pickle
with open('tuning_param/model_hist.p', 'wb') as f:
    pickle.dump(hist.history, f)
end = time.time()
print('time consume:{} min'.format((end - start)/60))

print('model ver:{}'.format(model_ver))
with open('tunning_records.md', 'a') as f:
    f.write('# {}'.format(model_ver))
# Visualize the training and validation loss of your neural network
loss_plot(hist, model_ver)
