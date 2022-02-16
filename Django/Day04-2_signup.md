# sign up

### createsuperuser
```
> python manage.py createsuperuser

username : admin
password : 1234
```

![img.png](imgs/loginerror.png)<br>
: 같은 이름 2개가 회원가입 되어 있을 경우, 위와 같은 에러 발생

<br>

### session ?
서버 하나에 여러 클라이언트가 접속할 때, 클라이언트 분별 하기 위해 각 정보를 session이 가지고 있다.

클라이언트가 필요로 하는 정보를 session에 담에 둔다. 