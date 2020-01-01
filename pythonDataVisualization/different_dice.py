from Die import Die
import pygal

D6 = Die()
#把默认的六个面修改成十个面
D10 = Die(10)

#掷筛子多次，并将结果储存在一个列表中
results = []
for roll_num in range(50000):
    result = D6.roll() + D10.roll()
    results.append(result)


# frequencies=[]
# for value in range(2,D6.num_sides+D10.num_sides+1):
#     #数出value出现了多少次
#     frequencie = results.count(value)
#     frequencies.append(frequencie)
#print(frequencies)

#用列表解析式替代上面的循环
frequencies=[results.count(value) for value in range(2,D6.num_sides+D10.num_sides+1)]

#可视化结果
hist = pygal.Bar()

hist.title = "Result of rolling  D6 and D10 1000 times"

#设置x轴刻度
labels=list(range(2,17))
hist.x_labels = [x for x in labels]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#把值添加到对应的刻度，引号中的值是图例
hist.add("D6+D10",frequencies )
hist.render_to_file("different_dice_visual.svg")

