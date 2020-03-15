## Telegram API Token 받기

텔레그렘 클라이언트에서 `@BotFather` 검색해 대화를 시작한다.

- `/newbot`: 새 봇 생성 요청
- ~ choose a **name** for your bot: 채팅창에 노출되는 이름 설정
- ~ choose a **username** for your bot: 봇의 ID

질문을 읽고 답변을 해 봇 생성이 완료되면 API token을 받을 수 있다.

## 서버에 배포
물건을 사기 전까지 알람을 받기 위해 [DigitalOcean](https://www.digitalocean.com)에 서버를 생성해 배포했다.

### Droplets 생성
- Image: Ubuntu 16.04.6 x64
- Plan: Standard, 5$/mo
- Volume: X
- Region: Singapore
- Auth: SSH Keys

### SSH 접속
[How to Connect to your Droplet with OpenSSH](https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/)
```shell
$ ssh root@203.0.113.0
```
### 서버 설정
`Python pip`를 설치한다.
```
$ sudo apt-get install python3-setuptools
$ sudo easy_install3 pip
```
프로젝트 파일을 업로드한다.
```shell
$ scp -r freitag-web-crawling-to-telegram root@203.0.113.0:/home/
```
pip를 이용해 python 패키지를 설치한다.
```shell
$ pip install -r requirements.txt
```

### Crontab 설정
[리눅스 크론탭(Linux Crontab) 사용법](https://jdm.kr/blog/2)
```shell
$ crontab -e
```
편집창이 뜨면 마지막에 추가한다.
```vi
* * * * * /usr/bin/python3 /home/freitag-web-crawling-to-telegram/app/freitag_web_parser.py
```