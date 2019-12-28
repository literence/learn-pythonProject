import matplotlib.pyplot as plt

#默认x轴第一个数为0，为改变这种情况，手动设定输入值
input_values = [1,2,3,4,5]

#输出值
squares = [1,4,9,16,25]

#把x轴第一个数默认值改为1时增加实参，绘制折线图,设置线条粗细
plt.plot(input_values,squares,linewidth = 5)

#设置图表标题，文字大小
plt.title("Square Numbers",fontsize = 24)

#设置坐标轴的标签以及文字大小
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

#设置刻度的大小,参数表示设置两条轴
plt.tick_params(axis = "both",labelsize = 14)

#显示折线图
plt.show()

