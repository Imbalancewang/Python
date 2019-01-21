# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 17:11
# @Author  : Magic
# @Email   : hanjunm@haier.com
import codecs
import os
import pandas as pd


def discard_prob(filename):
    fp=codecs.open('./some',mode='w',encoding='utf-8')
    item=[]
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as file:
        for line in file:
            lines = line.split('\t')
            category, prob, text = lines[0].strip(), lines[1].strip(), lines[2].strip()
            item.append(category + '\t' + text)
    fp.write('\n'.join(item))
    fp.close()

def write_ablove_99(filename):
    predict_above_99 = codecs.open('./predict_above_99', mode='w', encoding='utf-8')
    predict_below_99 = codecs.open('./predict_below_99', mode='w', encoding='utf-8')

    above_99 = []
    below_99 = []

    with codecs.open(filename=filename, mode='r', encoding='utf-8') as file:
        for line in file:
            lines = line.split('\t')
            category, prob, text = lines[0].strip(), lines[1].strip(), lines[2].strip()
            if float(prob) > 0.99:
                above_99.append(category + '\t' + text)
            else:
                below_99.append(category + '\t' + text)

    predict_above_99.write('\n'.join(above_99))
    predict_below_99.write('\n'.join(below_99))

    predict_above_99.close()
    predict_below_99.close()


def test(filename):
    temp = []
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as file:
        for line in file:
            lines = line.split('\t')
            category = lines[0].strip()
            prob = lines[1].strip()
            text = lines[2].strip()
            temp.append(category + '\t' + text)
    with codecs.open('./data/test_1', 'w', 'utf-8') as file:
        file.write('\n'.join(temp))


def test2(filename):
    temp = []
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as file:
        for line in file:
            lines = line.split('\t')
            category = lines[0].strip()
            prob = lines[1].strip()
            text = lines[2].strip()
            temp.append(text)
    with codecs.open('./data/test_1', 'w', 'utf-8') as file:
        file.write('\n'.join(temp))


def view_distribution(filename):
    dataframe = pd.read_csv(filepath_or_buffer=filename, sep='\t', header=None, names=('category', 'text'))
    print(dataframe.category.value_counts())


def view_distinct_data():
    with codecs.open('./data/data_all', 'r', 'utf-8') as file:
        datas = [line.strip() for line in file]

    print('offe: ' + str(len(datas)))
    datas = set(datas)
    print('end: ' + str(len(datas)))


    # with codecs.open('./data/distinct', 'w', 'utf-8') as file:
    #     for data in list(datas):
    #         file.write(data + '\n')





if __name__ == '__main__':
    #filename = os.path.join(os.path.dirname(__file__), 'data', 'predict_data')
    #write_ablove_99("unmarked")
    discard_prob('purifier')
    # filename = os.path.join(os.path.dirname(__file__), 'data', 'predict_data')
    # test(filename)

    # filename = os.path.join(os.path.dirname(__file__), 'data', 'view_data')
    # view_distribution(filename)

    #view_distinct_data()

