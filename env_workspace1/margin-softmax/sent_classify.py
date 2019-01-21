#! -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from tqdm import tqdm
import json
import keras
from keras.models import Model
from keras.layers import *
from keras.constraints import unit_norm
from keras.constraints import max_norm
from margin_softmax import *
from keras.callbacks import Callback
from keras.utils import plot_model
from keras import optimizers
from keras.callbacks import LambdaCallback
from keras.callbacks import ModelCheckpoint
#import matplotlib.pyplot as plt

num_train_groups = 8 # 前9万组问题拿来做训练
maxlen = 32
batch_size = 100
min_count = 3
word_size = 256
epochs = 1 # amsoftmax需要25个epoch，其它需要20个epoch


data = pd.read_csv('train_test.csv',encoding="utf-8", header=None, delimiter=',')
def strQ2B(ustring): # 全角转半角
    rstring = ''
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288: # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring

data[1] = data[1].apply(strQ2B)
data[1] = data[1].str.lower()

#chars is the dictionary which contains the sum of each letter and word??

chars = {}
for s in tqdm(iter(data[1])):
    for c in s:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1

# 0: padding标记
# 1: unk标记
chars = {i:j for i,j in chars.items() if j >= min_count}
id2char = {i+2:j for i,j in enumerate(chars)}
char2id = {j:i for i,j in id2char.items()}

def string2id(s):
    _ = [char2id.get(i, 1) for i in s[:maxlen]]
    _ = _ + [0] * (maxlen - len(_))
    return _

data[2] = data[1].apply(string2id)
train_data = data[data[0] < num_train_groups]
train_data = train_data.sample(frac=1)
x_train = np.array(list(train_data[2]))
y_train = np.array(list(train_data[0])).reshape((-1,1))
valid_data = data[data[0] >= num_train_groups]#???????????????
# 正式模型，基于GRU的分类器a
x_in = Input(shape=(maxlen,))
x_embedded = Embedding(len(chars)+2,
                       word_size)(x_in)
x = recurrent.GRU(word_size,return_sequences=True)(x_embedded)
#x1 = recurrent.GRU(word_size,go_backwards =True)(x_embedded)
#x = concatenate([x, x1]) 
x = Dropout(0.25)(x)
merged = Attention(150)(x)
merged = Dense(256, activation="relu")(merged)
merged = Dropout(0.25)(merged)
merged = BatchNormalization()(merged)
x = Lambda(lambda x: K.l2_normalize(x, 1))(merged)
pred = Dense(num_train_groups,
             use_bias=False,
             kernel_constraint=unit_norm())(x)

model = Model(x_in, pred) # 用分类问题做训练
adam = optimizers.Adam(lr=0.001,beta_1=0.9,beta_2=0.999,epsilon=1e-8)
model.compile(loss=sparse_amsoftmax_loss,
              optimizer=adam,
              metrics=['sparse_categorical_accuracy'])

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='sparse_categorical_accuracy', patience=50, verbose=2)

# callback on_train_run as a Class
class Mylogger(keras.callbacks.Callback):
    def on_train_begin(self,logs=None):
        print('On_train_begin')
        # model.summary()
        print(keras.utils.layer_utils.print_summary(self.model))



# callback tensorboard           
tbCallBack = keras.callbacks.TensorBoard(log_dir='./Graph', 
                                         histogram_freq=0, 
                                         write_graph=True, 
                                         write_images=True)


checkpoint = ModelCheckpoint(filepath='thisModel.h5',monitor='sparse_categorical_accuracy',mode='auto' ,save_best_only='True')
model_history = model.fit(x_train,
                    y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    validation_split=0.05,
                    callbacks=[Mylogger(),tbCallBack,early_stopping])


#score = model.evaluate(x_train, y_train, verbose=0)
#print('Test score:', score[0])
#print('Test accuracy:', score[1])
s=u"我想听周杰伦的歌"
s1 = u"给我来一首周杰伦的歌"
s2 = u"打开回家模式"
s3 = u"空调室外机漏水怎么办"
s4 = u"帮我空调换成除湿吧"
a = model.predict(np.array([string2id(s1)]))[0]
b =  model.predict(np.array([string2id(s)]))[0]
c =  model.predict(np.array([string2id(s2)]))[0]
d =  model.predict(np.array([string2id(s3)]))[0]
e = model.predict(np.array([string2id(s4)]))[0]
print a
print b
print c
print d
print e
print np.dot(a,b)
