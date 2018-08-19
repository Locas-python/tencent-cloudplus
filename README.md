# tencent-cloudplus

# 需求
1. 根据关键字获取腾讯云+相关文章
2. 获取内容：文章标题，文章id（拼接url），浏览量，点赞数
3. 将结果写入csv文件


# 分析

* 当点击页面的加载更多时，会触发post请求，并返回json数据
* 利用 fiddler 分析请求数据

> 第一次请求是请求第二页，但是将 pageNumber 设置为 1 也可以获取第一页的数据

# 运行效果

运行效果

![running](https://github.com/Locas-python/tencent-cloudplus/blob/master/runing.PNG?raw=true)

运行结果

![result](https://github.com/Locas-python/tencent-cloudplus/blob/master/result.PNG?raw=true)
