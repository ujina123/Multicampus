# DataBase

### mysql table 확인
```
[ sqlite3 일때 : 파이참 터미널 ]
(multi) ~ myboard > sqlite3 [databaseName].sqlite3   <br>
sqlite > .table

sqlite > .exit  (mysql 나가기)
```

```
[ terminal ]
> cd /usr/local/mysql/bin/
> ./mysql -u root -p   
> use mysql
> show tables;
```

### mysqlclient 설치
방법1 ) pip install mysqlclient <br>
방법2 ) conda install mysqlclient <br>
방법3 ) conda install -c quantopian mysqlclient <br>

### mysql 비밀번호 변경
```
[ terminal ] 
> alter user 'root'@'localhost' identified with mysql_native_password by '1234';
> alter user 'root'@'%' identified with mysql_native_password by '1234';
```


### mysql 사용설정
settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER' : 'root',
        'PASSWORD' : 'Dldbwls0628',
        'HOST' : 'localhost',
        'PORT' : '3306'
    }
}
```

### (Terminal) 모델 객체 생성 
https://arotein.tistory.com/25 <br>
`(multi) ~ myboard >`python manage.py makemigrations 'appName' <br>
`(multi) ~ myboard >`python manage.py migrate 

### 서버 실행 
`(multi) ~ myboard >`python manage.py runserver 

---
## 전체 코드 정리 
만드는 순서 : template (.html) -> view (views.py) -> url (urls.py)

#### 1. poject 및 app 생성
project 하나 생성 하면, 자동으로 project와 동일한 이름을 가진 app이 생성된다. 
```
> Django-admin startproject 'projectName'
```
추가적으로 app 생성 하고 싶을 때,
```
> python manage.py startapp 'appName'
```
<br>

#### 2. setting.py 에서 database 연동 설정
settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER' : 'root',
        'PASSWORD' : 'Dldbwls0628',
        'HOST' : 'localhost',
        'PORT' : '3306'
    }
}
```
<br>

#### 3. create model object 
models.py
```python
from django.db import models

class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=1000)
    mydate = models.DateTimeField()

    def __str__(self):
        return str({'myname': self.myname, 'mytitle': self.mytitle,
                    'mycontent': self.mycontent, 'mydate': self.mydate})

```

<br>

#### 4. templates file > index.html 
기본 틀 만들어주기
```python
<h1>Hello, {{ request.session.myname | default:"Django" }} with mysql</h1>

<table border="1">
    <col width="50"/>
    <col width="100"/>
    <col width="500"/>
    <col width="100"/>
    <tr>
        <th>번호</th>
        <th>작성자</th>
        <th>제목</th>
        <th>작성일</th>
    </tr>
    {% if not list %}
        <tr>
            <th colspan="4">----------작성된 글이 없습니다----------</th>
        </tr>
    {% else %}
        {% for data in list %}
            <tr>
                <td>{{ data.id }}</td>
                <td>{{ data.myname }}</td>
                <td><a href="{% url 'detail' data.id %}">{{ data.mytitle }}</a></td>
                <td>{{ data.mydate|date:"Y-m-d" }}</td>
            </tr>
        {% endfor %}
    {% endif %}
    <tr>
        <td colspan="4" align="right">
            <input type="button" value="글작성" onclick="location.href='{% url 'insert' %}'" />
        </td>
    </tr>
</table>
```
<br>

#### 5. makemigrtion
```
> python manage.py makemigrtions 'appName'
> python manage.py migrate
```

<br>

#### 6.  templates file 
insert.html 
```python
<h1>Insert</h1>

<form action="{% url 'insert' %}" method="post">{% csrf_token %}
    <table border="1">
        <tr>
            <th>작성자</th>
            <td><input type="text" name="myname" /></td>
        </tr>
        <tr>
            <th>제목</th>
            <td><input type="text" name="mytitle" /></td>
        </tr>
        <tr>
            <th>내용</th>
            <td><textarea rows="10" cols="60" name="mycontent"></textarea></td>
        </tr>

        <tr>
            <td colspan="2" align="right">
                <input type="button" value="취소" onclick="location.href='{% url 'index' %}'" />
                <input type="submit" value="글작성"/>
            </td>
        </tr>
    </table>
</form>
```
detail.html 
```python
<h1>Detail</h1>

<table border="1">
    <tr>
        <th>작성자</th>
        <td><input type="text" value="{{ dto.myname }}" readonly /></td>
    </tr>
    <tr>
        <th>제목</th>
        <td><input type="text" value="{{ dto.mytitle }}" readonly /></td>
    </tr>
    <tr>
        <th>내용</th>
        <td><textarea rows="10" cols="60" readonly>{{ dto.mycontent }}</textarea></td>
    </tr>
    <tr>
        <td colspan="2" align="right">
            <input type="button" value="목록" onclick="location.href='{% url 'index' %}'" />
            <input type="button" value="수정" onclick="location.href='{% url 'update' dto.id %}'" />
            <input type="button" value="삭제" onclick="location.href='{% url 'delete' dto.id %}'" />
        </td>
    </tr>
</table>
```

update.html
```python
<h1>Update</h1>

<form action="{% url 'update' dto.id %}" method="post"> {% csrf_token %}
    <table border="1">
        <tr>
            <th>작성자</th>
            <td><input type="text" value="{{ dto.myname }}" readonly /></td>
        </tr>
        <tr>
            <th>제목</th>
            <td><input type="text" name="mytitle" value="{{ dto.mytitle }}" /></td>
        </tr>
        <tr>
            <th>내용</th>
            <td><textarea rows="10" cols="60" name="mycontent">{{ dto.mycontent }}</textarea></td>
        </tr>
        <tr>
            <td colspan="2" align="right">
                <input type="button" value="취소" onclick="location.href='{% url 'detail' dto.id %}'" />
                <input type="submit" value="수정" />
            </td>
        </tr>
    </table>
</form>
```
#### 7. views.py
```python
from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all().order_by('-id')})


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def insert(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    else:
        myname = request.POST['myname']
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']

        result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

        if result:
            return redirect('index')
        else:
            return redirect('insertform')


def update(request, id):
    if request.method == 'GET':
        return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})
    else:
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']

        myboard = MyBoard.objects.filter(id=id)
        result_title = myboard.update(mytitle=mytitle)
        result_content = myboard.update(mycontent=mycontent)

        if result_title + result_content == 2:
            return redirect(f'/detail/{id}')
        else:
            return redirect(f'/updateform/{id}')


def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect(f'/detail/{id}')

```
#### 8. urls.py
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
```