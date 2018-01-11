from sklearn.utils import shuffle
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

DATA_PATH = 'data'
def image_resize(image, dim = (66, 200)):
    # resize image for using in cnn
    # use like this or you will get error when you load model
    import tensorflow as tf
    resized = tf.image.resize_images(image, dim)
    return(resized)

def loss_plot(hist, model_ver):
    # Visualize the training and validation loss of your neural network
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.savefig('tuning_param/model_loss_{}.jpg'.format(model_ver))

def generate_batch(df, batch_size=64):

    while 1:
        shuffle(df)
        for offset in range(0, len(df), batch_size):
            batch_df = df[offset:offset+batch_size]
            images = []
            steerings = []
            for i in range(len(batch_df)): # len(batch_df) but not batch_size
                img, steering = image_random_read(batch_df, i)
                img, steering = image_random_process(img, steering)
                images.append(img)
                steerings.append(steering)

            X_train = np.array(images)
            y_train = np.array(steerings)
            yield shuffle(X_train, y_train)

def image_random_read(batch_df, i):
    # random select one of center, left, right
    STEERING_COEFFICIENT = 0.2
    rnd_image = np.random.randint(0, 3)
    if rnd_image == 0:
        img_path = batch_df.iloc[i]['left'].strip()
        steering = batch_df.iloc[i]['steering'] + STEERING_COEFFICIENT
    elif rnd_image == 1:
        img_path = batch_df.iloc[i]['center'].strip()
        steering = batch_df.iloc[i]['steering']
    else:
        img_path = batch_df.iloc[i]['right'].strip()
        steering = batch_df.iloc[i]['steering'] - STEERING_COEFFICIENT
    img = cv2.imread(DATA_PATH + '/' + img_path)
    return((img, steering))

def image_random_process(img, steering):
    # random fliplr, sheer, gamma
    return(img, steering)
