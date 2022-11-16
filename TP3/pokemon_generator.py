import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.layers import Conv2D, Conv2DTranspose, Input, Flatten, Dense, Lambda, Reshape
from keras import backend as K
from keras.models import Model
from keras.metrics import binary_crossentropy
import matplotlib.pyplot as plt
import os
from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()

IMAGES_QTY = 4
IMAGES_PATH = "TP3/data/pokemon_images/"
NUM_CHANNELS = 3 # RGB
IMAGE_SIZE = 96
INPUT_DIM = IMAGE_SIZE * IMAGE_SIZE * NUM_CHANNELS
FIRST_INTERMEDIATE_DIM = 1024
SECOND_INTERMEDIATE_DIM = 256
LATENT_DIM = 2

def sampling(args: tuple):
    z_mean, z_log_var = args
    print(z_mean)
    print(z_log_var)
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], LATENT_DIM), mean=0.)
    return z_mean + K.exp(z_log_var / 2) * epsilon  # h(z)

def read_pokemon_images():
    images = []
    for image_file_name in os.listdir(IMAGES_PATH):
        image = keras.preprocessing.image.load_img(IMAGES_PATH + image_file_name, target_size=(IMAGE_SIZE, IMAGE_SIZE))
        image = keras.preprocessing.image.img_to_array(image)
        image = image / 255.0
        images.append(image)

    images = np.array(images)
    # reshape so its a 4d array
    images = images.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, NUM_CHANNELS)
    print(images.shape)
    images = images.reshape((len(images), np.prod(images.shape[1:])))
    print(images.shape)


    # example of image
    # plt.figure(figsize=(10, 10))
    # plt.imshow(images[0][:, :, 0])
    # plt.show()

    return images


if __name__ == "__main__":
    # load input
    x_train = y_train = read_pokemon_images()

    # --------------------------- encoder ---------------------------
    x = Input(shape=(INPUT_DIM,), name="input")
    # intermediate layer
    h = Dense(FIRST_INTERMEDIATE_DIM, activation='relu', name="encoding")(x)
    # defining the mean of the latent space
    z_mean = Dense(LATENT_DIM, name="mean")(h)
    # defining the log variance of the latent space
    z_log_var = Dense(LATENT_DIM, name="log-variance")(h)
    # note that "output_shape" isn't necessary with the TensorFlow backend
    z = Lambda(sampling, output_shape=(LATENT_DIM,))([z_mean, z_log_var])
    # defining the encoder as a keras model
    encoder = Model(x, [z_mean, z_log_var, z], name="encoder")
    # print out summary of what we just did
    encoder.summary()

    # --------------------------- decoder --------------------------- 
    input_decoder = Input(shape=(LATENT_DIM,), name="decoder_input")
    # taking the latent space to intermediate dimension
    decoder_h = Dense(FIRST_INTERMEDIATE_DIM, activation='relu', name="decoder_h")(input_decoder)
    # getting the mean from the original dimension
    x_decoded = Dense(INPUT_DIM, activation='sigmoid', name="flat_decoded")(decoder_h)
    # defining the decoder as a keras model
    decoder = Model(input_decoder, x_decoded, name="decoder")
    decoder.summary()

    # --------------------------- VAE --------------------------- 
    # grab the output. Recall, that we need to grab the 3rd element our sampling z
    output_combined = decoder(encoder(x)[2])
    # link the input and the overall output
    vae = Model(x, output_combined)
    # print out what the overall model looks like
    vae.summary()
    def vae_loss(x: tf.Tensor, x_decoded_mean: tf.Tensor):
        # Aca se computa la cross entropy entre los "labels" x que son los valores 0/1 de los pixeles, y lo que salió al final del Decoder.
        xent_loss = INPUT_DIM * binary_crossentropy(x, x_decoded_mean) # x-^X
        kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
        vae_loss = K.mean(xent_loss + kl_loss)
        return vae_loss

    vae.compile(loss=vae_loss)
    vae.summary()

    vae.fit(x_train, x_train,
        epochs=300,
        batch_size=IMAGES_QTY)

    n = 5  # generate nxn samples
    figure = np.zeros((IMAGE_SIZE * n, IMAGE_SIZE * n, NUM_CHANNELS))

    #Create a Grid of latent variables, to be provided as inputs to decoder.predict
    #Creating vectors within range -5 to 5 as that seems to be the range in latent space
    grid_x = np.linspace(-5, 5, n)
    grid_y = np.linspace(-5, 5, n)[::-1]

    # decoder for each square in the grid
    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z_sample = np.array([[xi, yi]])
            x_decoded = decoder.predict(z_sample)
            image = x_decoded[0].reshape(IMAGE_SIZE, IMAGE_SIZE, NUM_CHANNELS)
            figure[i * IMAGE_SIZE: (i + 1) * IMAGE_SIZE,
                j * IMAGE_SIZE: (j + 1) * IMAGE_SIZE] = image

    plt.figure(figsize=(10, 10))
    fig_shape = np.shape(figure)
    figure = figure.reshape((fig_shape[0], fig_shape[1], fig_shape[2]))

    plt.imshow(figure)
    plt.show()  
