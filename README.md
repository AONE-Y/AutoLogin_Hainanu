# 海南大学校园网自动登录脚本
userId、password和queryString如图所得，
![获取相应数据](https://img-blog.csdnimg.cn/20210409204407205.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0VvbV9f,size_16,color_FFFFFF,t_70)
只需填这三项即可，然后把.py文件放置服务器、或者路由器等运行即可

```python
python AutoLogin.py
```
(需要一直挂在后台,linux可以安装screen创建新窗口后运行后再关闭终端，这样不会终止终端运行的命令，相关安装方法，请百度），如果未安装requests模块，请先

```python
pip install requests
```

如果校园网掉线，大概一分钟内可以重新连接
