#Bonus_Day005_Day006_Day007 - CNN MNIST dataset

"""Bonus_Day005_CNN_MNIST_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13qs4y3mFPDuqQ5RearJsIblwWem8k2D6

https://blog.paperspace.com/intro-to-optimization-momentum-rmsprop-adam/
"""

import keras

from keras.datasets import mnist
#MNIST dataset downloaded in image format and already converted to categorical data

(features_train, labels_train), (features_test, labels_test) = mnist.load_data() #60000/10000 - training and testing data

print(features_train.shape) #60000, 28, 28
print(labels_train.shape) #10000, 28, 28
print(features_test.shape) #60000,
print(labels_test.shape) #10000,

print(features_train[0].shape) #28, 28
print(features_train[0][0].shape) #28,

features_train[9]
features_train[12][0]

labels_train

features_test[0]

labels_test

features_train = features_train.reshape((60000, 28, 28, 1)) #reshaping - 60000 images, widht/height known. we have to provide depth-1

features_train.shape #60000, 28, 28, 1

features_train[0]

#feature scaling - min/max scaling, range: [0-1]
features_train = features_train.astype('float32') / 255

features_train[10]

#testing data - feature scaling
features_test.shape #10000, 28, 28
features_test = features_test.reshape((10000, 28, 28, 1))

features_test = features_test.astype('float32') / 255

features_test[0]

from tensorflow.keras.utils import to_categorical

labels_train = to_categorical(labels_train, num_classes=10, dtype='float32')
labels_test = to_categorical(labels_test, num_classes=10)

print(labels_train.shape)
labels_train[0]

print(labels_test.shape)
labels_test[0]

from keras import layers
from keras import models

model = models.Sequential() #empty sequential model - now going to add
model.add(layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (28, 28, 1))) #node, filter - 3*3/5*5, activation function, input shape of image - width*height*depth (depth --> grey-1, color-3)
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(16, (5, 5), activation = 'relu')) #Conv2D - fixed pixels for all images, for different pixel images we have to use Conv3D
model.add(layers.MaxPooling2D((2, 2)))

#Now, flattening after two times repeating convolution/max_pooling
model.add(layers.Flatten())

#ANN
model.add(layers.Dense(64, activation='relu')) #nodes,activation function
model.add(layers.Dense(10, activation='softmax')) #nodes - equal to number of classes which is from 0 to 9/last layer, activation function - softmax/multiclass classification

#Compiling - optimize it (rmsprop, adam), loss function, accuracy metrics
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(features_train, labels_train, epochs=50, batch_size=64)

test_loss, test_accuracy = model.evaluate(features_test, labels_test) #loss and accuracy

features_test[0].shape

print('Test accuracy is:',test_accuracy)

model.layers

type(features_train)

features_train[10].shape

testing_data = features_train[10].reshape(1,28,28,1)

testing_data.shape

import numpy as np
np.argmax(model.predict(testing_data), axis=-1) #for multi-class classification/softmax function
#Set axis=-1 means, extract largest indices in each row. Here we have only one row.

labels_train[10]

labels_train[10].argmax()

"""
Website for better understanding:
https://medium.com/coinmonks/handwritten-digit-prediction-using-convolutional-neural-networks-in-tensorflow-with-keras-and-live-5ebddf46dc8
"""

features_test.shape

test_data = features_test

predictions = np.argmax(model.predict(test_data), axis=-1) #for multi-class classification/softmax function

list(zip(predictions, labels_test.argmax(axis=1)))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test.argmax(axis=1), predictions) #10*10

print(cm)