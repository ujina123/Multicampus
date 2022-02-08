## register / login / logout
mymember folder

0. 시작
```
> django-admin startproject mymember
```

### settings.py <br>

 TEMPLATES 수정
```python
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES = [ 
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'], # 지정 해주고 해당 경로에 templates 폴더 생성
        ...
    },
]
```
<br>
DATABASE 연동 <br>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER' : 'root',
        'PASSWORD' :'Dldbwls0628',
        'HOST' : 'localhost',
        'PORT' : '3306'
    }
}
```

추가
```python
# login / logout 
LOGIN_REDIRECT_URL = '/result'
LOGOUT_REDIRECT_URL = '/'
```

### templates folder
**index.html**

```html
<h1>MyMember</h1>

<a href="register/">회원가입</a>
<br>
<a href="login/">로그인</a>
```

### Django Form 사용
**forms.py**<br>

```
UserCreationForm 이 가진 기본적인 필드 : username, password1, password2
password1 : 비밀번호 / password2 : 비밀번호 확인
```
```python
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyMemberForm(UserCreationForm): # 장고에 있는 UserCreationForm을 상속 받을 것이다.
    # UserCreationForm 이 가진 기본적인 필드 외의 필드를 추가하고 싶을 때
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta: # 위 클래스를 설명해 줄 수 있는 Meta class
        model = User
        fields = ('username','password1','password2','first_name','last_name','email')
```

### templates folder
**register.html**

as_table : 각 필드가 테이블 행으로 렌더링된다. 
```html
<h1>Register</h1>
<form action="." method="post">{% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit" value="회원가입">
</form>
```

**login.html**

```html
<form action="{% url 'login' %}" method="post">{% csrf_token %}
    ID : <input type="text" name="username">
    <br>
    PW : <input type="text" name="password">
    <br>
    <input type="submit" value="로그인">
</form>
```

**result.html**
```html
<h1>Hello, {{ user.username }}</h1>
<a href="/logout/">로그아웃</a>
```

### views.py
```python
from django.shortcuts import render, redirect
from .forms import MyMemberForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = MyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'register.html', {'form':MyMemberForm()})

def result(request):
    return render(request,'result.html')
```
`.is_valid()`: 데이터가 유효한지 아닌지를 검사 , True/False 의 Boolean 값을 가짐

### urls.py
```python
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # 같은 이름을 import 하면 충돌이 일어나기 때문에 별칭 지정

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('result/',views.result, name='result'),
]
```