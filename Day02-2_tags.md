### APP 추가
`(multi) ~/tags >` python manage.py startapp 'AppName'

`(multi) ~/tags >` python manage.py startapp var <br>
    - var의 이름을 가진 app 생성

### TAGS
### 1. variables
**{{ variable }}** : 변수는 키를 값으로 매핑하는 사전과 같은 객체인 context에서 값을 출력한다. 
<br>
사전 조회, 속성 조회 및 목록 색인 조회는 점 표기법 (.)으로 구현된다.

##### 1) variables01
**templates > var folder > variables01.html**
```html
<!--서버(views.py)에서 리스트파일을 보낸다.-->
<h1>{{ lst.0 }}</h1> 
<p>{{ lst.1 }}</p>
```

**views.py**
```python
from django.shortcuts import render,redirect

def variables01(request):
    my_list = ['python','django','templates']
    return render(request,'var/variables01.html', {'lst': my_list})
```

##### 2) variables02
**templates > var folder > variables02.html**
```html
<h1>{{ dct.class }} 반 {{ dct.name }} 님 환영합니다.</h1> 
```
**views.py**
```python
from django.shortcuts import render,redirect

def variables02(request):
    my_dict = {'class':'multi', 'name':'hong-gd'}
    return render(request, 'var/variables02.html', {'dct':my_dict})
```

### 2. for loop
{% for _ in __ %} 제어문 <br> 
{% endfor %} 제어문 닫기

**templates > var folder > forloop.html**
```html
{% for i in number %}
<p>{{ i }}</p>
{% endfor %}
```
**views.py**

장고가 가진 기본 템플릿(.html)에서는 for문 범위지정이 안되서 views.py에서 범위를 지정 후, .html로 전달 
```python
from django.shortcuts import render,redirect

def for_loop(request):
    return render(request, 'var/forloop.html',{'number':range(1,21)})
```

### 3. if
##### 1) 기본 if문
**templates > var folder > if01.html**
```html
{% if user.id %}
<h1>Hello, {{ user.id }}</h1>
{% endif %}
```
**views.py**
 
```python
from django.shortcuts import render,redirect

def if01(request):
    return render(request, 'var/if01.html',{'user':{'id':'kim', 'job':'student'}})
```

##### 2) if / elif / else
**templates > var folder > if02.html**
' == ' 연산자 옆에 공백 필수!!
```html
{% if role == 'admin' %}
<h1>Admin Page</h1>
<a href="#">user list</a>
<a href="#">user delete</a>

{% elif role == 'manager' %}
<h1>Manage Page</h1>
<a href="#">user list</a>

{% else %}
<h1>User Page</h1>
<a href="#">my</a>

{% endif %}
```
**views.py**
 
```python
from django.shortcuts import render,redirect

def if02(request):
    return render(request, 'var/if02.html',{'role':'manage','id':'multi'})
```

### 4. href
**templates > var folder > href.html**
{% url 'index' %} : name이 index인 url로 가라 
```html
<a href="{% url 'index' %}">go index</a>
```
**views.py**
 
```python
from django.shortcuts import render,redirect

def href(request):
    return render(request, 'var/href.html')
```

### 5. get / post

**views.py**
 
```python
from django.shortcuts import render,redirect

def get_post(request):
    if request.method == 'GET':
        return render(request, 'var/get.html')
    elif request.method == 'POST':
        return render(request, 'var/post.html')
    else:
        return redirect('index')
```


## FILTERS

필터는 변수 및 태그 인수의 값을 변환한다. 

{'django':'the web framework for perfectionists with deadlines'}

서버에 저장된 값을 {{ django|title }} 을 적용 시키면 django의 값들이 title 형식의으로 렌더링 된다.

일부 필터는 인수를 취급하기도 한다. 
{{ mydate|date:"Y-m-d" }}

