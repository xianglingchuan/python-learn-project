# -*- coding: utf-8 -*-
# !/usr/bin/python
def f1(path):
    with open(path) as f:
        all_tag = 0 #记录所有的标记数
        loc_tag = 0 #记录真实的地址位置标记
        pred_loc_tag = 0; #记录预测的地理位置标记数
        correct_tag = 0; #记录正确的标记数
        correct_loc_tag = 0; #记录正确的地址位置标记数

        states = ['B', 'M', 'E', 'S'];
        for line in f:
            line = line.strip();
            if line == '' : continue;
            _, r, p = line.split()
            all_tag +=1;
            if r == p:
                correct_tag += 1;
                if r in states:
                    correct_loc_tag +=1;
            if r in states:loc_tag +=1;
            if p in states:pred_loc_tag +=1;
        loc_P = 1.0 * correct_loc_tag/pred_loc_tag
        loc_R = 1.0 * correct_loc_tag/loc_tag;
        print("loc_P:{0}, loc_R:{1}, loc_F1:{2}".format(loc_P, loc_R, (2*loc_P*loc_R)/(loc_P+loc_R)));


if __name__ == "__main__":
    f1("./data/test.rst");

#loc_P:0.9079811338204014, loc_R:0.8427467811158799, loc_F1:0.8741485999198683
#精确率:0.90, 召回率:0.84, f1值:0.84

