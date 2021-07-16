# 双线图  图例设置
import random
from matplotlib import pyplot as plt 
import matplotlib

x = range(11,31)
y_1 = [1,0,1,1,2,4,3,2,3,4,5,6,5,4,3,3,1,1,1,3]
y_2 = [1,0,2,3,2,1,3,2,3,4,1,2,5,2,3,0,1,0,1,0]
font = {
    'family' : 'MicroSoft YaHei',
    'weight' :  'bold',
    'size' : 14
}
matplotlib.rc('font',**font)

plt.figure(figsize=(20,8),dpi=80)

_xticks = [str(i)+'岁' for i in list(x)]

plt.xticks(x,_xticks)

plt.xlabel('岁数')
plt.ylabel('个数')
plt.title('我和同桌npy个数随年龄变化折线图')

plt.grid(alpha=0.4,linestyle='--') # 设置网格透明度
# 双线图 画两次，label参数是图例
plt.plot(x,y_1,label='自己',color='red',linestyle=':',linewidth=5,alpha=0.5) # 颜色可用rgb十六进制
plt.plot(x,y_2,label='同桌',color='cyan',linestyle='-.')
# 添加图例
plt.legend(loc='upper left') # loc参数调整图例位置，有十种位置可填数字0-10，或者用字母

plt.show()


# 拓展
# 可加图片水印，可添加文本注释，如标记最高最低点