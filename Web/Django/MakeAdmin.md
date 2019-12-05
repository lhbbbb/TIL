# 관리자 계정

## 관리자 계정 만들기

* shell (git-bash) type에서 명령어 못침

### VSCode

1. 터미널 새로 열고 `python manage.py createsuperuser`

2. id, 비번 다 치고

3. 내가 만든 앱의 admin.py에서 article 사이트 등록

   ```python
   from .models import Article
   # Register your models here.
   admin.site.register(Article)
   ```

4. browser에서 localhost:8000/admin 으로 접속

