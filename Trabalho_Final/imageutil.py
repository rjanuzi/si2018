import dataset

import tensorflow as tf

import matplotlib.pyplot as plt

def loadJpegImg(imgName):
    return tf.Session().run(tf.image.decode_jpeg(dataset.loadImage(imgName), channels=3))

def loadJpegImgs(imgNameList):
    ses = tf.Session()
    imgs = []
    imgsToLoad = len(imgNameList)
    for i in range(imgsToLoad):
        imgs.append(ses.run(tf.image.decode_jpeg(dataset.loadImage(imgNameList[i]), channels=3)))

        if i % 50 == 0:
            print('Loading imgs: %02f %s' % ( (i/imgsToLoad)*100., '%') )

    return imgs

def plotImg(imgData):
    plt.figure()
    plt.imshow(imgData)
    plt.grid(False)
    plt.show()
