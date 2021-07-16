# 直方图

import random
from matplotlib import pyplot as plt 
import matplotlib

font = {
    'family' : 'MicroSoft YaHei',
    'weight' :  'bold',
    'size' : 14
}
matplotlib.rc('font',**font)
plt.figure(figsize=(20,10),dpi=80)

# 设置组距为3
bin_width = 3

# 生成250个100-130 的随机数
a = [random.randint(80,153) for i in range(250)]

# 计算组数  组数=极差/组距
num_bins = int((max(a)-min(a)/bin_width))

plt.hist(a,num_bins,density=True)  # density将纵坐标变成占比

plt.xticks(range(min(a),max(a),bin_width))

plt.grid()

plt.show()