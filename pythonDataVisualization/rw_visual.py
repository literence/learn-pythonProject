import matplotlib.pyplot as plt
from random_walk import RandomWalk

#放在循环中模拟多次随机漫步
while True:

	#创建一个RandomWalk实例
	rw=RandomWalk()

	#生成随机漫步点
	rw.fill_walk()

	#设置绘图窗口的尺寸
	plt.figure(dpi=128,figsize=(16,9))

	#设置一个数字列表,用来方便设置颜色映射
	point_numbers = list(range(rw.num_points))

	#传递给绘图函数,设置点的大小
	#plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor="None",s=1)

	#使用plot
	plt.plot(rw.x_values,rw.y_values,linewidth=1 )

	#突出起点和终点
	plt.scatter(0,0,c="green",edgecolors="None",s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c="red",edgecolors="None",s=100)
	
	#隐藏坐标轴
	plt.axis("off")

	#显示
	plt.show()

	

	keep_runing = input("Make another walk?(y/n):")
	if keep_runing == "n":
		break