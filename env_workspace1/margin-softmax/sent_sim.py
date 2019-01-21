#! -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from tqdm import tqdm
import json
from keras.models import Model
from keras.layers import *
from keras.constraints import unit_norm
from margin_softmax import *
from keras.callbacks import Callback
from keras.utils import plot_model

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

#data[2] = data[1].apply(string2id)
#train_data = data[data[0] < num_train_groups]
#train_data = train_data.sample(frac=1)
#x_train = np.array(list(train_data[2]))
#y_train = np.array(list(train_data[0])).reshape((-1,1))
#valid_data = data[data[0] >= num_train_groups]
## 正式模型，基于GRU的分类器
#x_in = Input(shape=(maxlen,))
#x_embedded = Embedding(len(chars)+2,
#                       word_size)(x_in)
#x = recurrent.GRU(word_size)(x_embedded)
#x = Lambda(lambda x: K.l2_normalize(x, 1))(x)
#pred = Dense(num_train_groups,
#             use_bias=False,
#             kernel_constraint=unit_norm())(x)

#encoder = Model(x_in, x) # 最终的目的是要得到一个编码器
#model = Model(x_in, pred) # 用分类问题做训练

#model.compile(loss=sparse_amsoftmax_loss,
#              optimizer='adam',
#              metrics=['sparse_categorical_accuracy'])

#history = model.fit(x_train,
#                    y_train,
#                    batch_size=batch_size,
#                    epochs=epochs,
#                    callbacks=[])

#encoder.save("sim1.model")
from keras.models import load_model
models = load_model('sim1.model',{'sparse_amsoftmax_loss': sparse_amsoftmax_loss})
s=u"我想听周杰伦的歌"
s1 = u"红烧肉怎么做"
a = models.predict(np.array([string2id(s1)]))[0]
b =  models.predict(np.array([string2id(s)]))[0]
print np.dot(a,b)
