#-*- coding: utf-8 -*-
from keras.models import load_model
from margin_softmax import *
import numpy as np
maxlen = 32
def string2id(s):
    _ = [char2id.get(i, 1) for i in s[:maxlen]]
    _ = _ + [0] * (maxlen - len(_))
    return _

model = load_model('sim.model',{'sparse_amsoftmax_loss': sparse_amsoftmax_loss})
s=u"播放一首韩红的歌"
print model.predict(np.array([string2id(s)]))[0]
