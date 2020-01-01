from Die import Die
import pygal
import matplotlib.pyplot as plt

D6 = Die()

#投掷几次骰子，把结果存在列表当中
# results=[]
# for roll_num in range(1000):
#     result = D6.roll()
#     results.append(result)

#用列表解析式替代上面的循环
results=[D6.roll() for roll_num in range(1000)]

#print(results)

#分析结果
# frequencies=[]
# for value in range(1,D6.num_sides+1):
#     #数出value出现了多少次
#     frequencie = results.count(value)
#     frequencies.append(frequencie)

#用列表解析式替代上面的循环
frequencies = [results.count(value) for value in range(1,D6.num_sides+1)]

#print(frequencies)

#可视化结果
hist = pygal.Bar()

hist.title = "Result of rolling a D6 1000 times"

#设置x轴刻度
hist.x_labels = ["1","2","3","4","5","6"]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#把值添加到对应的刻度，引号中的值是图例
hist.add("D6",frequencies )
hist.render_to_file("die_visual.svg")


x=[1,2,3,4,5,6]
plt.plot(x,frequencies)
plt.show()

plt.scatter(x,frequencies)
plt.show()