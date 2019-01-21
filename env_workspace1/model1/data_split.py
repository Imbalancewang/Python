# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 12:04
# @Author  : Magic
# @Email   : hanjunm@haier.com
import codecs
import os

import pandas as pd

from sklearn.utils import shuffle

from sklearn.model_selection import train_test_split

def data_split(filename):

    dataframe = pd.read_csv(filepath_or_buffer=filename, sep='\t', header=None, names=('category', 'text'))
    dataframe=shuffle(dataframe)
    x_train, x_test, y_train, y_test = train_test_split(dataframe.category, dataframe.text, test_size=0.3, random_state=42)
    train = pd.concat((x_train, y_train), axis=1, names=None)
    test = pd.concat((x_test, y_test), axis=1, names=None)
    with codecs.open('./data/train_data', 'w', 'utf-8') as file:
        file.write(train.to_csv(sep='\t', header=None, index=None))

    with codecs.open('./data/test_data', 'w', 'utf-8') as file:
        file.write(test.to_csv(sep='\t', header=None, index=None))


def one_classfication_data_split(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as file:
        with codecs.open(filename='./setSpeed', mode='w', encoding='utf-8') as f:
            with codecs.open(filename='./not_setSpeed', mode='w', encoding='utf-8') as fp:
                for line in file:
                    if line.startswith('setSpeed'):
                        f.write(line.strip() + '\n')
                    else:
                        fp.write(line.strip() + '\n')



if __name__ == '__main__':
    filename = os.path.join(os.path.dirname(__file__), 'data', 'predict_sterilizer_prob')
    data_split(filename)

    print(filename)

    dataframe = pd.read_csv(filepath_or_buffer='./data/train_data', sep='\t', names=('category', 'text'))
    print(dataframe.category.value_counts())

    print('*' * 50)

    dataframe = pd.read_csv(filepath_or_buffer='./data/test_data', sep='\t', names=('category', 'text'))
    print(dataframe.category.value_counts())

    print('*' * 50)

    dataframe = pd.read_csv(filepath_or_buffer='./data/predict_sterilizer_prob', sep='\t', names=('category', 'text'))
    print(dataframe.category.value_counts())

    # one_classfication_data_split(filename)
