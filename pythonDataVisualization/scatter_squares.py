import matplotlib.pyplot as plt

#绘制一对x和y坐标,实参s设置点的尺寸
#设置为红色点
plt.scatter(2,4,c="red",s=200)

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.show()

#绘制一系列点
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.show()

#自动计算数据
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# 传递实参删除数据点的轮廓
#设置颜色
plt.scatter(x_values,y_values,c=(0,0.5,0.5),edgecolor="None",s=40)

#设置坐标轴取值范围
plt.axis([0,1100,0,1100000])

plt.show()

#colormap
x_values = list(range(1001))
y_values = [x**2 for x in x_values] 
plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Blues,edgecolor='none', s=40)
plt.show()