from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 27, 22, 18]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)  # 第一个参数设置图片宽高，第二个设置点的像素大小

# 绘图
plt.plot(x, y)

# 设置x轴
plt.xticks(range(2, 26))  # 传个列表进去
# 设置坐标轴
plt.yticks(range(min(y), max(y) + 1, 2))
#绘制网格
plt.grid()
#设置描述信息
plt.xlabel('时间')
plt.ylabel('温度 单位(℃)')
plt.title('10点到12点每分钟气温变化情况')

# 保存
# plt.savefig('./t1.png')  # 保存为.scv矢量图放大不失真

# 展示图形
plt.show()
