##  file up & down load

### updowm project

0. updown project 생성
```
> django-admin startproject updown 
```

1. settings.py > TEMPLATES 수정 <br>
templates 위치 잡기 
```python
'DIRS' : [BASE_DIR/'templates'] # 여러 파일들을 리스트로 지정할 수 있지만, templates라는 폴더로 여러 파일을 관리할 거라서 이렇게 지정해줄 수 있다. 
```


2. settings.py  <br>
```python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```
장고에서 파일 업,다운로드를 제공하는 기본적인 폴더는 media 라고 부른다. 
```python
# 파일 맨 밑에 코드 추가
MEDIA_URL = '/media/' # 경로
MEDIA_ROOT = BASE_DIR/'media' # 파일 업로드 시, 해당 폴더에 저장됨
```
<br>
+ media 폴더, templates 폴더 만들어주기 


3. templates folder <br>

3-1. index.html
```html
<form action="/upload/" method="post" enctype="multipart/form-data">{% csrf_token %}
    <input type="file" name="uploadfile">
    <br>
    <input type="submit" value="업로드">
</form>
```
![img.png](imgs/updown_index.png)

[ enctype 종류 ] 
- `multipart/form-data` :  파일, 이미지를 서버로 전송할 경우 사용
- `text/plain` : 인코디을 하지 않은 문자상태로 전송한다. 
- `application/www-form-urlencoded` : default, 폼 데이터는 서버로 전송되기 전에 URL-Encode 된다. 

<br>

3-2. download.html
```html
<h1>File Download</h1>
<input type="button" value="다운로드" onclick="location.href='/download/{{ filename }}'">
```
![img_1.png](imgs/updown_download.png)

<br>

4. views.py <br>

```python
from django.shortcuts import render, HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def index(request):
    return render(request, 'index.html')

def upload_process(request):
    upload_file = request.FILES['uploadfile'] # .FILES['Name'] : 전달된 파일(Name)을 받아 온다.
    # print(upload_file) # 업로드 파일명 반환
    # print(type(upload_file)) # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    
    uploaded = default_storage.save(upload_file.name, ContentFile(upload_file.read()))
    # print(uploaded) # 업로드파일명_???.파일타입 <class 'str'>
    # print(type(uploaded)) # [08/Feb/2022 23:17:16] "POST /upload/ HTTP/1.1" 200 260
    
    return render(request, 'download.html',{'filename':uploaded})

def download_process(request, filename):
    response = HttpResponse(default_storage.opne(filename).read())
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
```
`default_storage(  )` : 이전에 만들어 둔 media root를 찾아준다. 
<br>
`ContentFile( upload_file.read() )` : upload_file을 읽어온다. 
<br><br>
`HttpResponse(  )`: 
<br>
`response['Content-Disposition']` : 


<br>

5. urls.py
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload/',views.upload_process),

    path('download/<str:filename>', views.download_process),
]
```


업로드가 된다면 media 폴더 안에 업로드 한 파일들이 저장되어 있을 것이다!