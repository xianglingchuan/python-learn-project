# coding=utf-8
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

filename = "../../../resource/test.csv";
print (filename);

tips = pd.read_csv(filename);
print (tips.head);

print ("======= 选择(Select)=========");
rs = tips[['S.No', 'Name', 'Age', 'City']].head(5);
print (rs);

print ("======= WHERE条件 =========");
rs = tips[tips['Age']==28].head(5);
print (rs);

print ("======= 通过GroupBy分组 =========");
rs = tips.groupby('Age').size();
print (rs);

print ("======= 前N行 =========");
rs = tips[['S.No', 'Name', 'Age', 'City']].head(5);
print (rs);













