# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:42
# @Author  : Magic
# @Email   : hanjunm@haier.com
import codecs
import sys


def foo(file_correct,file_prediction,file_output):
    correct_data = open(file_correct,'r',encoding="UTF-8")
    prediction_data = open(file_prediction, 'r',encoding="UTF-8")
    correct_lines = correct_data.readlines()
    prediction_lines = prediction_data.readlines()
    num = 0
    outputer = open(file_output,"w",encoding="UTF-8")
    i = 0
    bad_case_num = 0
    for correct_line_one in correct_lines:
        correct_line_one_list = correct_line_one.strip().split("\t")
        if len(correct_line_one_list) == 2:
            prediction_line_one = prediction_lines[i].strip()
            i += 1
            prediction_line_one_list = prediction_line_one.split("\t")
            num += 1
            if correct_line_one_list[0] != prediction_line_one_list[0]:
                print(correct_line_one.strip()+"\t"+prediction_line_one)
                outputer.write(correct_line_one.strip()+"\t"+prediction_line_one+"\n")
                bad_case_num += 1
    print("bad_num:%d\ttotal_num:%d" % (bad_case_num,num))
    print("accuracy_rate:%f" % (1 - float(bad_case_num)/float(num)))
    outputer.write("bad_num:%d\ttotal_num:%d\n" % (bad_case_num,num))
    outputer.write("accuracy_rate:%f" % (1 - float(bad_case_num)/float(num)))
    outputer.close()


def find_bad_case_and_score(input_file, output_file):
    total_num = 0
    bad_case_num = 0
    with codecs.open(filename=input_file, mode='r', encoding='utf-8') as file:
        with codecs.open(filename=output_file, mode='w', encoding='utf-8') as fp:
            for line in file:
                total_num += 1
                lines = line.strip().split('\t')
                trueLable = lines[0].strip()
                predictLabel = lines[1].strip()
                text = lines[2].strip()
                if trueLable.split('=')[1] != predictLabel.split('=')[1]:
                    print(line.strip())
                    fp.write(line.strip() + '\n')
                    bad_case_num += 1

    print("bad_num:%d\ttotal_num:%d" % (bad_case_num, total_num))
    print("accuracy_rate:%f" % (1 - float(bad_case_num) / float(total_num)))



if __name__=="__main__":
    # print("main")
    # if len(sys.argv) != 4:
    #     print ('Usage: python input_name new_data_name output_name')
    #     exit(1)
    # #print(sys.argv[0])
    # foo(sys.argv[1], sys.argv[2], sys.argv[3])
    find_bad_case_and_score('./data/sweep', './data/sweep_check')
