# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

import dataset
import preprocessing
import imageutil as img
import models

checkpoint_path = "test_1_checkpoints/cp.ckpt"

def trainModel(trainIns, trainOuts, save=True, imgLimit=None):

    if imgLimit:
        trainIns = trainIns[:imgLimit]
        trainOuts = trainOuts[:imgLimit]

    train_imgs = img.loadJpegImgs(trainIns)
    train_imgs = np.asarray(train_imgs)
    train_imgs = train_imgs/255
    train_outputs = np.asarray(trainOuts)

    model = models.createFullyConnectedModel()

    # Create checkpoint callback
    cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1, period=5)

    # Train
    model.fit(train_imgs, train_outputs, epochs=50, callbacks = [cp_callback])

    # Saving model
    if save:
        model.save(models.FULLY_CONNECTED_PATH)

def testModel(testIns, testOuts, model=models.restoreFullyConnectedModel(), imgLimit=None):

    if imgLimit:
        testIns = testIns[:imgLimit]
        testOuts = testOuts[:imgLimit]

    test_imgs = img.loadJpegImgs(testIns)
    test_imgs = np.asarray(test_imgs)
    test_imgs = test_imgs/255
    test_outputs = np.asarray(testOuts)

    loss, acc = model.evaluate(test_imgs, test_outputs)
    print("Model accuracy (Test data): {:5.2f}%".format(100*acc))

# Load data
trainIns, trainOuts, testIns, testOuts, labels = preprocessing.getTrainingSets()

trainModel(trainIns, trainOuts, imgLimit=400)
testModel(testIns, testOuts, imgLimit=100)
