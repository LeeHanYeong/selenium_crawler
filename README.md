# Selenium Crawler Project

selenium으로 crawling한 데이터를 django model에 맞게 class화 하여
최신순으로 보여준다.

### ENV

nginx <--> gunucorn <--> Django

poetry
```bash
[tool.poetry]
name = "poetry_test"
version = "0.1.0"
description = ""
authors = ["mingyu <rlaalsrbgk@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.6"
django = "<3"
selenium = "^3.141.0"
beautifulsoup4 = "^4.8.2"
pillow = "^7.0.0"
djangorestframework = "^3.11.0"
gunicorn = "^20.0.4"
psycopg2-binary = "^2.8.4"
[tool.poetry.dev-dependencies]
django-extensions = "^2.2.8"
jupyter = "^1.0.0"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```


`secret.json`

```json
{
  "SOCIAL": {

    "INSTAGRAM_EMAIL": "instagram email",
    "INSTAGRAM_PASSWORD": "instagram password",

    "TWITTER_EMAIL": "twitter email",
    "TWITTER_PASSWORD": "twitter password",

    "FACEBOOK_EMAIL": "facebook email",
    "FACEBOOK_PASSWORD": "facebook password"
  },

  "AWS": {
    "AWS_ACCESS_KEY_ROOT": "local pem location",
    "AWS_URL_CONNECT": "aws url",
    "AWS_ACCESS_KEY": "aws access key",
    "AWS_SECRET_ACCESS_KEY": "aws secret access key"
  }

}
```

### 배포
Dockerfile 사용

환경: AWS EC2

Database: AWS RDS postgresql

storage: AWS S3

### Site url
<!--### Site url-->
[http://pby.kr]
[http://parkboyoung.kr]
