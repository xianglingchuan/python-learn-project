import spacy;
nlp = spacy.load("en");
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion');
print ("==================================================\n\t");
print (doc);
print ("==================================================\n\t");

doc = nlp("The big grey dog ate all of the chocalate,but fortunately he wasn't sick!");
print (doc);


# 利用空格分开
print ("==================================================");
print ("利用空格分开");
print ("==================================================\n\t");
print(doc.text.split());



# 利用token的.orth_方法，可以识别标点符号
print ("\r\n==================================================");
print ("利用token的.orth_方法，可以识别标点符号");
print ("==================================================");
print([token.orth_ for token in doc])



# 带下划线的方法返回字符、不带下划线的方法返回数字
print ("\r\n==================================================");
print ("带下划线的方法返回字符、不带下划线的方法返回数字");
print ("==================================================");
print([(token, token.orth_, token.orth) for token in doc])




# 分词，去除标点和空格
print ("\r\n==================================================");
print ("分词，去除标点和空格");
print ("==================================================");
print([token.orth_ for token in doc if not token.is_punct | token.is_space])




# 标准化到基本形式
print ("\r\n==================================================");
print ("标准化到基本形式");
print ("==================================================");
practice = "practice practiced practicing"
nlp_practice = nlp(practice)
print([word.lemma_ for word in nlp_practice])

# 词性标注 可以使用.pos_ 和 .tag_方法访问粗粒度POS标记和细粒度POS标记
print ("\r\n==================================================");
print ("词性标注 可以使用.pos_ 和 .tag_方法访问粗粒度POS标记和细粒度POS标记");
print ("==================================================");
doc2 = nlp("Conor's dog's toy was hidden under the man's sofa in the woman's house")
pos_tags = [(i, i.tag_) for i in doc2]
print(pos_tags)





# 's 的标签被标记为 POS.可以利用这个标记提取所有者和他们拥有的东西
print ("\r\n==================================================");
print ("'s 的标签被标记为 POS.可以利用这个标记提取所有者和他们拥有的东西");
print ("==================================================");
owners_possessions = []
for i in pos_tags:
    if i[1] == "POS":
        owner = i[0].nbor(-1)
        possession = i[0].nbor(1)
        owners_possessions.append((owner, possession))
print(owners_possessions)



# 简化代码
print ("\r\n==================================================");
print ("简化代码");
print ("==================================================");
print([(i[0].nbor(-1), i[0].nbor(1)) for i in pos_tags if i[1] == "POS"])


# 实体识别 PERSON 是不言自明的；NORP是国籍或宗教团体；GGPE标识位置（城市、国家等等）；DATE 标识特定的日期或日期范围， ORDINAL标识一个表示某种类型的顺序的单词或数字。
print ("\r\n==================================================");
print ("实体识别 PERSON 是不言自明的；NORP是国籍或宗教团体；GGPE标识位置（城市、国家等等）；DATE 标识特定的日期或日期范围， ORDINAL标识一个表示某种类型的顺序的单词或数字。");
print ("==================================================");
wiki_obama = """Barack Obama is an American politician who served as the 44th President of the United States from 2009 to 2017. He is the first African American to have served as president, as well as the first born outside the contiguous United States."""
nlp_obama = nlp(wiki_obama)
print([(i, i.label_, i.label) for i in nlp_obama.ents])


# 将文章分成句子
print ("\r\n==================================================");
print ("将文章分成句子");
print ("==================================================");
for ix, sent in enumerate(nlp_obama.sents,1):
    print("Sentence number {}:{}".format(ix,sent))