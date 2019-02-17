# -*- coding: utf-8 -*-
# !/usr/bin/python
#数据读取
def get_content(path):
    with open(path, 'r', encoding='gbk', errors='ignore') as f:
        content = '';
        for l in f:
            l = l.strip();
            content += l;
        return content;

#高频词统计函数，输入是一个词的数组
def get_TF(words, topK =10):
    tf_dic = {};
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) +1;
    return sorted(tf_dic.items(), key=lambda x:x[1], reverse=True)[:topK]


def stop_words(path):
    with open(path) as f:
        return [l.strip() for l in f];

def main():
    import glob;
    import random;
    import jieba;

    files = glob.glob("./data/news/c000013/*.txt");
    corpus = [get_content(x) for x in files];

    #添加自定义词典
    #每一行为三个部分，词语，词频(可省略)、词性(可省略)
    jieba.load_userdict("./data/user_dict.utf8");

    sample_inx = random.randint(0, len(corpus));
    print("sample_inx:",sample_inx);
    #split_words = list(jieba.cut(corpus[sample_inx]));
    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words("./data/stop_words.utf8")]
    print("样本之一:"+corpus[sample_inx]);
    print("样本分词效果:"+'/'.join(split_words));
    print("样本的topK(10)词："+str(get_TF(split_words)));

main();