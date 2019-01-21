# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 16:44
# @Author  : Matthew
# @Site    : 
# @File    : execute_ppi.py
# @Software: PyCharm
import tensorflow as tf
from GAT.models import GAT
from GAT.utils.process_ppi import *
import numpy as np
from GAT.utils.process import *
from GAT.utils.layers import *

dataset='ppi'


# training params
batch_size = 1
nb_epochs = 100000
patience = 100
lr = 0.005  # learning rate the
l2_coef = 0.0005  # weight decay
hid_units = [8] # numbers of hidden units per each attention head in each layer
n_heads = [8, 1] # additional entry for the output layer
residual = False
nonlinearity = tf.nn.elu
model = GAT


print('Dataset: ' + dataset)
print('----- Opt. hyperparams -----')
print('lr: ' + str(lr))
print('l2_coef: ' + str(l2_coef))
print('----- Archi. hyperparams -----')
print('nb. layers: ' + str(len(hid_units)))
print('nb. units per layer: ' + str(hid_units))
print('nb. attention heads: ' + str(n_heads))
print('residual: ' + str(residual))
print('nonlinearity: ' + str(nonlinearity))
print('model: ' + str(model))

