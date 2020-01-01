from Die import Die
import pygal

#D6_1 = Die()
#D6_2 = Die()

#同是掷出两个D8骰子,两个相乘
#D8_1 = Die(8)
#D8_2 = Die(8)

#三个D6
D6_1 = Die()
D6_2 = Die()
D6_3 = Die()
results=[]
for roll_num in range(1000):
    result = D6_1.roll()+D6_2.roll()+D6_3.roll()
    #result = D8_1.roll()*D8_2.roll()
    results.append(result)

frequencies=[]
for value in range(3,D6_1.num_sides+D6_2.num_sides+D6_3.num_sides+1):
#for value in range(1,D8_1.num_sides*D8_2.num_sides):

    #数出value出现了多少次
    frequencie = results.count(value)
    frequencies.append(frequencie)

#可视化结果
hist = pygal.Bar()

hist.title = "Result of rolling two D6 dice 1000 times"

#设置x轴刻度
labels=list(range(3,19))
#labels = list(range(1,65))
hist.x_labels = [x for x in labels]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#把值添加到对应的刻度，引号中的值是图例
hist.add("D6+D6+D6",frequencies )
#hist.add("D8**2",frequencies)
hist.render_to_file("dice_visual.svg")