# 관리자 계정

관련 작업은 VSCode에서 진행한다.

## 관리자 계정 만들기

관리자 계정을 만들기 위해선 VSCode 상의 터미널 창에서 명령어를 입력해야 한다.

1. 터미널 새로 열고 `python manage.py createsuperuser`

2. id, 비밀번호를 입력한 후

3. 내가 만든 앱의 admin.py에서 article 사이트 등록

   ```python
   from .models import Article
   # Register your models here.
   admin.site.register(Article)
   ```

4. browser에서 localhost:8000/admin 으로 접속

