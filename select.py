# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 14:49
# @Author  : Matthew
# @Site    : 
# @File    : select.py
# @Software: PyCharm
import codecs


def write_ablove_99(filename):
    #predict_above_99 = codecs.open('./predict_above_99', mode='w', encoding='utf-8')
    predict_below_99 = codecs.open('./predict_below_999', mode='w', encoding='utf-8')

    above_99 = []
    below_99 = []

    with codecs.open(filename=filename, mode='r', encoding='utf-8') as file:
        for line in file:
            lines = line.split('\t')
            category, prob, text = lines[0].strip(), lines[1].strip(), lines[2].strip()
            below_99.append(category + '\t' + text)

    predict_below_99.write('\n'.join(below_99))

    predict_below_99.close()



def write_ablove_999(filename):
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


if __name__=="__main__":
    write_ablove_999("unmarked")


