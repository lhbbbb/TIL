# DjangoDay1

## 2019.09.11

from django.shortcuts import get_object_or_404

telegram

getMe

getUpdates

sendMessage



## ngrok

다운로드 받고 ~ 루트에 ngrok.exe 옮기면 된다

cmd 창

ngrok version 확인

`ngrok --version`

`ngrok http 8000`

1. webhook 설정
   * setWebhook
   * https://api.telegram.org/bot<token>/setWebhook?url=https://1f1cc93f.ngrok.io/<token>

security 때문에 s추가 => url=https:

2. webhook 정보조회
   * getWebhookInfo
3. webhook 삭제
   * deleteWebhook

### Tips

https://github.com/sspy21/todochatbot