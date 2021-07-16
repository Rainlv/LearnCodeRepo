# 散点图绘制 .scatter
import random
from matplotlib import pyplot as plt 
import matplotlib

x_1 = range(1,32)
x_2 = range(51,81)
y_1 = [21,20,21,21,22,24,30,22,30,31,25,26,25,24,30,31,31,21,21,30,21,22,20,15,13,16,12,10,8,6,8]
y_2 = [21,20,22,30,31,21,30,31,30,31,21,22,25,22,30,31,21,20,21,20,21,22,16,18,14,12,10,5,4,10]
font = {
    'family' : 'MicroSoft YaHei',
    'weight' :  'bold',
    'size' : 14
}
matplotlib.rc('font',**font)

plt.figure(figsize=(20,10),dpi=80)

# 调整x轴
_x = list(x_1) + list(x_2)
_xticks = ['10月{}日'.format(i) for i in x_1 ]
_xticks += ['11月{}日'.format(i-50) for i in x_2]
plt.xticks(_x[::3],_xticks[::3],rotation=45)

plt.scatter(x_1,y_1,label='10月份')
plt.scatter(x_2,y_2,label='11月份')

plt.xlabel('时间')
plt.ylabel('温度')

plt.legend()

plt.grid()

plt.show()