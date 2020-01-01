#17-1

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
#存储API调用的URL
#url="https://api.github.com/search/repositories?q=language:python&sort=stars"

url="https://api.github.com/search/repositories?q=language:Go&sort=stars"
#使用requests 来执行调用,调用get() 并将URL传递给它，再将响应对象存储在 变量r 中
r = requests.get(url)

#响应对象包含一个名为status_code 的属性，它让我们知道请求是否成功了（状态码200表示请求成功）。
print("Status Code:",r.status_code)

#这个API返回JSON格式的信息，因此我们使用方法json() 将这些信息转换为一个Python字典
response_dict=r.json()

print(response_dict.keys())

#指出GitHub总共包含多少个Python仓库
print("Total repositories:",response_dict['total_count'])

#获取了多少个仓库repo_dicts=response_dict['items']
print("Repositories returned:",len(repo_dicts))

#研究第一个仓库有多少信息和包含哪些信息
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

names,stars,plot_dicts=[],[],[]
for repo_dict in repo_dicts:
	print("\nSelected information about first repository:")
	#项目的名称
	print('Name:', repo_dict['name'])
	#使用键owner 来访问 表示所有者的字典，再使用键key 来获取所有者的登录名
	print('Owner:', repo_dict['owner']['login'])
	#多少个star
	print('Stars:', repo_dict['stargazers_count'])
	#项目在GitHub仓库的URL
	print('Repository:', repo_dict['html_url'])
	#项目的创建时间
	print('Created:', repo_dict['created_at'])
	#最后更新时间
	print('Updated:', repo_dict['updated_at'])
	#打印仓库的描述
	print('Description:', repo_dict['description'])
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

	#生成工具提示
	plot_dict = {
		'value':repo_dict['stargazers_count'],
		'label':str(repo_dict['description']),
		'xlink': repo_dict['html_url']
	}
	plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)

#创建了一个Pygal类Config的实例，并将其命名为my_config
my_config = pygal.Config()

#在下面定制图表的外观
#让标签绕x轴旋转45度
my_config.x_label_rotation = 45
#隐藏了图例,因只在图表中绘制一个数据系列
my_config.show_legend = False
#标题大小
my_config.title_font_size = 24
#副标签是 x 轴上的项目名以及 y 轴上的大部分数字。主标签是 y 轴上为5000整数倍的刻度
#副标签字体大小
my_config.label_font_size = 14
#主标签字体大小
my_config.major_label_font_size = 18
#用truncate_label将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名）
my_config.truncate_label = 15
#隐藏图表中的水平线
my_config.show_y_guides = False	#自定义宽度，充分利用页面空间
my_config.width = 1000	chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')


