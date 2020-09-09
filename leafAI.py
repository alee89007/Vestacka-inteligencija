import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import tensorflow
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.metrics import confusion_matrix
import numpy

data="leaf.csv"
names=['class', 'specimen-number', 'eccentricity', 'aspect-ratio', 'elongation', 'solidity', 'stochastic-convexity', 'isoperimetric-factor', 'maximal-indentation-depth', 'lobedness', 'average-intensity', 'average-contrast', 'smoothness', 'third-moment', 'uniformity', 'entropy']
dataset=pd.read_csv(data, names=names)

#podela podataka na test i train
array=dataset.values
X=array[:,0:15]
Y=array[:,0]

X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2)
print(dataset.values)
