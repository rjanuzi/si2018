import dataset
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Original size = 450 x 600

newHeight = 150
newWidth = 200
channels = 3
newSizeTensor = tf.constant([newHeight, newWidth])

def loadJpegImgTensor(imgName):
    return tf.image.decode_jpeg(dataset.loadImage(imgName), channels=3)

def loadTensorData(imgTensor):
    return tf.Session().run(imgTensor)

def resizeImg(imgTensor):
    imgTensor = imgTensor/255
    return loadTensorData(tf.image.resize_images(imgTensor, newSizeTensor, align_corners=True, preserve_aspect_ratio=True))

def loadPreparedImgsData(imgNameList, resize=True):
    imgsToLoad = len(imgNameList)
    imgs = []
    for i in range(imgsToLoad):
        if resize:
            imgs.append(resizeImg(loadJpegImgTensor(imgNameList[i])))
        else:
            imgs.append(loadTensorData(loadJpegImgTensor(imgNameList[i])))

        if i % 50 == 0:
            print('Loading imgs: %02f %s' % ( (i/imgsToLoad)*100., '%') )

    return imgs, newHeight, newWidth

def imgToTensor(imgData):
    print(imgData.shape)
    newShape = imgData.reshape((channels*newHeight*newWidth))
    print(newShape.shape)

    # imgTensor = tf.convert_to_tensor(imgData)
    # print(imgTensor)

def plotImg(imgData):
    plt.figure()
    plt.imshow(imgData)
    plt.grid(False)
    plt.show()

# imgs, height, width = loadPreparedImgsData(['ISIC_0026236', 'ISIC_0027573'], resize=True)
# imgToTensor(imgData)
# print(height)
# print(width)
# print(imgs[0].shape)
# print(imgs[1].shape)
# plotImg(imgs[0])
# plotImg(imgs[1])
