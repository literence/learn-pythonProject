import requests
#用于对字典列表排序
from operator import itemgetter
import pygal

#储存 API 调用的 url
#这个 url 是所有id
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
#执行调用并存储响应对象
r = requests.get(url)
#查看是否成功
print("Status Code:",r.status_code)

#转换为列表，要知道响应文本是字典还是列表，只需要把url在浏览器打开查看，
# 下面使用这些ID来创建一系列字典，其中每个字典都存储了一篇文章的信息
submission_ids = r.json()#返回的文件为包含ID的列表

#创建一个列表存储上述字典
submission_dicts = []

for submission_id in submission_ids[:30]:
    #对于每篇文章，都执行一个 API 调用
    #url包含id 的当前值，是指定id的url
    url = ('https://hacker-news.firebaseio.com/v0/item/'+str(submission_id)+'.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    #为当前处理的文章创建一个字典，并在其中存储文章的标题以及到其讨论页面的链接。
    submission_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id=' + str(submission_id),
        #在这个字典中存储了评论数。如果文章还没有评论，响应字典中将没有键'descendants'
        'comments':response_dict.get('descendants',0)
    }
    #将submission_dict 附加到submission_dicts 末尾
    submission_dicts.append(submission_dict)

    #根据评论数对字典列 表submission_dicts 进行排序，降序
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

    #遍历排序后的列表，对于每篇热门文章，都打印其三项信息：标题、到讨论页面的链接以及文章现有的评论数
    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])

        plot_dicts = []
        plot_dict = {
            'value':submission_dict['comments'],
            'label':str(submission_dict['title']),
            'xlink':submission_dict['link'],
        }
        plot_dicts.append(plot_dict)

#创建条形图
chart = pygal.Bar()
chart.add('',plot_dicts)
chart.render_to_file('hn_submissions.svg')




