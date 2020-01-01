#15-5
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self,num_points=5000):
        """初始化随机漫步属性"""

        #随机漫步次数
        self.num_points = num_points

        #用列表存储随机漫步经过的点，从0开始
        self.x_values = [0]
        self.y_values = [0]

    #看看改动数据有何影响
    def get_step(self):
        #direction = choice([1,-1])
        direction = choice([1])
        distance = choice([0,1,2,3,4,5])
        step = direction*distance
        return step

    def fill_walk(self):
        #"计算随机漫步包含的所有点"

        ##不断漫步，直到列表到达指定的长度
        #while len(self.x_values)<self.num_points:
        #    #我们使用choice([1, -1]) 给x_direction 选择一个值，
        #    #结果要么是表示向右走的1，要么是表示向左走的-1
        #    x_direction = choice([1,-1])

        #    # 随机地选择一个0~4之间的整数，告诉Python 沿指定的方向走多远
        #    # 通过包含0，我们不仅能够沿两个轴移动，还能够沿y轴移动
        #    x_distance = choice([0,1,2,3,4])

        #    #将移动方向乘以移动距离，以确定沿 x 和 y 轴移动的距离。
        #    #如果x_step 为正，将向右移动，为负将向左移动，而为零将垂直移动
        #    x_step = x_direction*x_distance

        #    #同理y
        #    y_direction = choice([1,-1])
        #    y_distance = choice([0,1,2,3,4])
        #    y_step = y_direction*y_distance


        while len(self.x_values)<self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            #如果x_step 和y_step 都为零，则意味着原地踏步，我们拒绝这样的情况，接着执行下一次循环
            if x_step==0 and y_step==0:
                continue

            #为获取漫步中下一个点的 x 值，我们将x_step 与x_values 中的最后一个值相加
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1]+y_step

            #获得下一个点的 x 值和 y 值后，我们将它们分别附加到列表x_values 和y_values 的末尾
            self.x_values.append(next_x)
            self.y_values.append(next_y)