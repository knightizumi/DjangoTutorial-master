# Django

Python 網頁開發框架之一

- [Django](https://www.djangoproject.com/)
- [Wiki](https://zh.wikipedia.org/wiki/Django)
- [研習講義](http://ntub-django.arthurc.me/)
- [Django Note](https://github.com/arthurc0102/Note/tree/master/School/NTUB/IRC/class_2016.10.11_to_2016.11.08)

```shell
$ python
$ print("Hello World")

# 執行Python檔 -> python <檔案名稱>.py
$ python C:\Users\user\Desktop\main.py
$ cls # 清空shell
```

## Python基礎語法
```python
# 基本型別
# x = 60 # Int
# y = 'Hello' # String
# z = True # Bool

# print(x)
# print(y)
# print(z)

# 流程控制-選擇-IF
# if z:
#     print(x)
#     print(y)

# print(z)

# if x > 60:
#     print('及格')
# elif x < 60:
#     print('不及格')
# else: # x == 60
#     print('剛好壓線')

# 集合型別-LIST(類似陣列)
a = [1, 2, 3, 4, 5] #List
# print(a)
# print(a[0])
# print(a[:3]) # 到 3 之前
# print(a[3:])
# print(a[::2]) # list[開始:結束:間隔]

for i in a:
    print(i)
```

## Django基本操作
```shell
# pip -> python package管理工具
$ pip list
# Install Django
$ pip install Django

$ django-admin
$ cd Desktop
$ cd FirstDjango

# 建立django專案
# django-admin startproject <專案名稱>
$ django-admin startproject FirstDjango

# 建立django專案 核心目錄
# django-admin startproject <名稱> <路徑>
# . -> 當前目錄下
$ django-admin startproject core .
$ dir # 目前目錄

# 啟動開發用即時Server
$ python manage.py runserver #預設127.0.0.8:8000
$ ctrl c # 停止server
```
- 整理版
```shell
$ cd Desktop

$ mkdir Django0315

$ cd Django0315

$ pip install Django

$ django-admin startproject core .

$ python manage.py runserver
```

## core
manage.py django指令程式
```shell
__pycache__ #django 快取檔
__init__.py #將目錄設為python package
settings.py #django 設定檔
urls.py #django網站路由設定
wsgi.py
```

## Django設定檔簡單說明
```python
# 是否開啟除錯模式
DEBUG=<Bool>

# DEBUG=False要設定允許的IP或Domain
ALLOWED_HOSTS = []

# 安裝django套件或功能
INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
]

# 語系
LANGUAGE_CODE = 'zh-hant'
# 時區
TIME_ZONE = 'Asia/Taipei'
```

## Django Database
```shell
# 安裝 ipython
$ pip install django ipython

# 依照 python 定義的 models 被 makemigrate 後產生的檔案(遷移紀錄檔)，對資料庫進行資料表的新增或是修改
$ python manage.py migrate

# 建立超級專案使用者
$ python manage.py createsuperuser
# 範例密碼 P@ssWord

# 執行 server
$ python manage.py runserver
# http://127.0.0.1:8000/admin/
# urls.py -> 修改admin page url
```

## Django Admin Page

- URL: ``http://127.0.0.1:8000/admin/``

- 修改admin page url --- urls.py
```python
urlpatterns = [
   path('hello-admin/', admin.site.urls),
]
# http://127.0.0.1:8000/hello-admin/
```

## Django hello world

1. 新增 views.py 在 core/

2. 修改 views.py
```python
from dajngo.http import HttpResponse

def root(request):
    # pass 不做事
    return HttpResponse('Hello World!')
    # s = '<h1>Hello World!</h1>'
    # return HttpResponse(str(s))
```

3. 修改 urls.py
```python
from .views import root
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', root)
]
```

## Django架構圖

![「tibame django」的圖片搜尋結果](https://i.ytimg.com/vi/W40mDCqWyYo/maxresdefault.jpg)