# ベースイメージとしてPython 3.8を使用
FROM python:3.8-slim

# 作業ディレクトリを設定
WORKDIR /app

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# pipをアップグレードし、依存関係をインストールするためのrequirements.txtをコピー
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# アプリケーションのソースコードをコピー
COPY ./ranking /app/

# Djangoの開発サーバーを起動
CMD python manage.py runserver 0.0.0.0:8000


