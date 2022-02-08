# pagination

### Create Pagination
**views.py** > index(request)
1. id를 기준으로 내림차순하여 객체 불러오기 
    ```python
   # MyBoard.objects.all() : MyBoard class를 가지고 장고에서 만든 manage 객체를 모두 불러온다.
    myboard = MyBoard.objects.all().order_by('-id')
    ```
2. 페이지 당 보여줄 게시물 개수 설정
    ```python
    # Paginator ( object_list , 페이지당 보여줄 게시물 개수 )
    paginator = Paginator(myboard,5)
    ```
3. GET 방식으로 받아온 정보를 'page'에 해당하는 value 불러와 페이지 번호를 리턴, 만약 없으면 페이지 번호 1로 리턴
    ```python
    # request.GET.get('key','default')
    page_num = request.GET.get('page',1)
    ```
4. 페이지에 맞는 모델 가져오기 
    ```python
    # get_page(num) : num 페이지를 가지고 온다.
    page_obj = paginator.get_page(page_num)  
    ```
5. 가져온 모델을 list의 값으로 index.html로 그려준다.(rendering)
    ```python
    render(request, 'index.html', {'list': page_obj})
    ```

<br>
   
**index.html**
```html
<!--처음으로-->
<a href="?page=1">처음</a>

<!--이전 페이지로-->
{% if list.has_previous %}
    <a href="?page={{ list.previous_page_number }}">이전</a>
{% else %}
    <a>이전</a>
{% endif %}

<!--페이징-->
{% for page_num in list.paginator.page_range %}
    {% if page_num == list.number %}
        <b>{{ page_num }}</b>
    {% else %}
        <a href="?page={{ page_num }}">{{ page_numm }}</a>
    {% endif %}
{% endfor %}

<!--다음 페이지-->
{% if list.has_next %}
    <a href="?page={{ list.next_page_number }}">다음</a>
{% else %}
    <a>다음</a>
{% endif %}

<!-- 끝으로 -->
<a href="?page={{ list.paginator.num_pages }}">끝</a>
<br><br>
```
<br>


<br>

### Method
```python
# 전체 페이지 범 # 
page_obj.count # <Page 1 of 20>
```
```python
# 페이지 개수
age_obj.paginator.num_pages # range(1,21)
```
```python
# 페이지 전체 범위 
page_obj.paginator.page_range
```
```python
# .has_next() : True if there’s a next page.
page_obj.has_next()

# .has_previous() : True if there’s a previous page.
page_obj.has_previous()
```
```python
# .next_page_number() , .previous_page_number() : 다음, 이전페이지 번호 반환
# 만약 번호가 없다면 InvalidPage 발생
try:  
    print(page_obj.next_page_number()) 
    print(page_obj.previous_page_number())
except:
    pass

print(page_obj.start_index()) # index of the first object on the page
print(page_obj.end_index()) # index of the last object on the page
```
