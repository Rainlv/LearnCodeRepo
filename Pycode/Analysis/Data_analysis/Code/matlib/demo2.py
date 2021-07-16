# 绘画温度时间分布图 折线图  .plot
#     字体设置
import random
from matplotlib import pyplot as plt 
import matplotlib

x = range(0, 120)
y = [random.randint(20,35) for i in range(120)]

font = {
    'family' : 'MicroSoft YaHei',
    'weight' :  'bold',
    'size' : 14
}
matplotlib.rc('font',**font) # 改字体

plt.figure(figsize=(20,8),dpi=80)

time_x = ['10点{}分'.format(i) for i in range(60)]
time_x += ['11点{}分'.format(i) for i in range(60)]

plt.xticks(list(x)[::3], time_x[::3], rotation=45)  # rotation参数调整x轴旋转度数

plt.xlabel('时间')
plt.ylabel('温度 单位(℃)')
plt.title('10点到12点每分钟气温变化情况')

plt.plot(x, y)

plt.show()