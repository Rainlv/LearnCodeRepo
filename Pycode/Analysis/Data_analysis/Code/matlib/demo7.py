# 多列竖向条形图 多次绘制
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

x= ['猩球崛起','敦刻尔克','蜘蛛侠','战狼2']
y_1 = [15746,312,4497,319]
y_2 = [12357,156,2045,168]
y_3 = [2358,398,2358,362]
# 设置三日影片的坐标偏移，使不重合
bar_width = 0.2
x_1=list(range(len(x)))
x_2=[i+bar_width for i in x_1]
x_3=[i+bar_width*2 for i in x_1]

plt.bar(x_1,y_1,width=bar_width,label='9月14日')
plt.bar(x_2,y_2,width=bar_width,label='9月15日')
plt.bar(x_3,y_3,width=bar_width,label='9月16日')
#设置x轴刻度
plt.xticks(x_2,x)

plt.legend()

plt.xlabel('影片名')
plt.ylabel('当日票房')

plt.show()