import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from scipy.stats import bernoulli

DATA_PATH = 'data'
def image_resize(image, dim = (64, 64)):
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
    from sklearn.utils import shuffle
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
    return img, steering

def image_random_process(img, steering):
    # random fliplr, sheer, rotation, gamma
    img, steering = random_fliplr(img, steering)
    img, steering = random_shear(img, steering)
    # img, steering = random_rotate(img, steering)
    img = random_gamma(img)
    return img, steering

def random_fliplr(img, steering, flipping_prob=0.5):
    """
    Based on the outcome of an coin flip, the image will be flipped.
    If flipping is applied, the steering angle will be negated.
    """

    head = bernoulli.rvs(flipping_prob)
    if head:
        return np.fliplr(img), -1 * steering
    else:
        return img, steering

def random_shear(img, steering, shear_range=200):
    rows, cols, ch = img.shape
    dx = np.random.randint(-shear_range, shear_range + 1)
    random_point = [cols / 2 + dx, rows / 2]
    pts1 = np.float32([[0, rows], [cols, rows], [cols / 2, rows / 2]])
    pts2 = np.float32([[0, rows], [cols, rows], random_point])
    dsteering = dx / (rows / 2) * 360 / (2 * np.pi * 25.0) / 6.0
    M = cv2.getAffineTransform(pts1, pts2)
    img = cv2.warpAffine(img, M, (cols, rows), borderMode=1)
    steering += dsteering
    return img, steering

def random_rotate(img, steering, rotation_amount=15):
    # will cost too much time
    angle = np.random.uniform(-rotation_amount, rotation_amount + 1)
    rad = (np.pi / 180.0) * angle
    return rotate(img, angle, reshape=False), steering + (-1) * rad

def random_gamma(img):
    # http://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/
    gamma = np.random.uniform(0.4, 1.5)
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    img = cv2.LUT(img, table)
    return(img)
