# 使用するPythonのベースイメージを指定
FROM python:3.8

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルrequirements.txtをコンテナ内にコピー
COPY ./requirements.txt /app/

# 依存関係をインストール
RUN pip install -r requirements.txt

# プロジェクトのファイルをコンテナ内の作業ディレクトリにコピー
COPY ./ranking /app/
