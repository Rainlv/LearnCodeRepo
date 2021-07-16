# 竖状条形图 .bar
import random
from matplotlib import pyplot as plt 
import matplotlib

font = {
    'family' : 'MicroSoft YaHei',
    'weight' :  'bold',
    'size' : 14
}
matplotlib.rc('font',**font)

plt.figure(figsize=(20,8),dpi=80)

x = ['战狼','变形金刚','摔跤吧!爸爸','加勒比海盗']
y = [56.01,12.06,15.66,45.69]

plt.xticks(rotation=90)

plt.bar(x,y,width=0.3)

plt.show()