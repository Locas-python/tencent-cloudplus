import requests
from lxml import etree
import json, re, time, random, sys
from pprint import pprint
import csv

'''
根据关键字获取腾讯云+相关文章
获取内容：文章标题，文章id（拼接url），浏览量，点赞数
将结果写入csv文件

----------

当点击页面的加载更多时，会触发post请求，并返回json数据
利用 fiddler 分析请求数据

第一次请求是请求第二页，但是将 pageNumber 设置为 1 也可以获取第一页的数据

'''

# 提示用户输入关键字，默认为 爬虫
if len(sys.argv) == 2:
    query = sys.argv[1]
elif len(sys.argv) == 1:
    query = '爬虫'
else:
    exit(f'Usage: {sys.argv[0]} [搜索关键字]')

url = 'https://cloud.tencent.com/developer/services/ajax/search?action=SearchList'  # 异步（post）请求链接
article_url_origin = 'https://cloud.tencent.com/developer/article/' # 和获取的文章 id 拼接完整文章链接
pageNumber = 1 # post请求数据：第N页
getAticleNumber = 0 # 计算已获取的文章数

with open(f'腾讯云加社区-{query}.csv', 'w') as file:
    csv_writer = csv.writer(file, lineterminator='\n')
    while True:
        data = {"action":"SearchList","payload":{"pageNumber":pageNumber,"q":query,"searchTab":"article"}}
        res = requests.post(url, json=data)
        result = json.loads(res.text)

        # 当请求的页数无效时（超过实际），该值为 0 
        if result['data']['total'] == 0:
            break

        # 提取每篇文章的 标题、id、点赞数、浏览量
        articles = result['data']['list']
        for article in articles:
            article = article['article']
            article_id = article['id']
            title = article['title']
            like = article['likeCount']
            view = article['viewCount']
    
            # 清洗数据
            title = re.subn('</?em>', '', title)[0]
            link = article_url_origin + str(article_id)

            print(title, article_id, view, like)
            print('-' * 79)
            csv_writer.writerow((title, link, view, like))

        getAticleNumber += len(result['data']['list'])
        print('total:', result['data']['total'], 'get:', getAticleNumber)
        pageNumber += 1 # 请求下一页
        time.sleep(random.randint(4, 10)/10) # 随机延迟 0.4 ~ 1 秒